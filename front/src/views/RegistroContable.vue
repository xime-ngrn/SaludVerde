<script setup>
import { ref, reactive, computed, onMounted, watch } from 'vue';
import axios from 'axios';
import Menu from '@/components/MenuBar.vue';
import Options from '@/components/OptionsBar.vue';
import { getAuthToken } from '@/utils/cookies';

const currentUser = getAuthToken();

const isActive = ref(false); // false = Gasto, true = Ingreso   
const message = ref('');

const catIngresos = ref([]);
const catGastos = ref([]);
const reportes = ref([]);

const fetchReportes = async () => {
    try {
        const response = await axios.get(`http://127.0.0.1:5000/obtenerReportes?username=${currentUser}`);
        reportes.value = response.data.reportes;
        console.log("Reportes disponibles:", reportes.value);
    } catch (e) {
        console.error("Error cargando reportes", e);
    }
};

const fetchCategorias = async () => {
    try {
        const [resIngresos, resGastos] = await Promise.all([
            axios.get('http://127.0.0.1:5000/categorias?tipo=ingreso'),
            axios.get('http://127.0.0.1:5000/categorias?tipo=gasto')
        ]);

        catIngresos.value = resIngresos.data.categorias;
        catGastos.value = resGastos.data.categorias;
    } catch (e) {
        console.error("Error cargando categorías", e);
    }
};

onMounted(() => {
    fetchCategorias();
    fetchReportes();
});

const categoriasFiltradas = computed(() => {
    return isActive.value ? catIngresos.value : catGastos.value;
});

watch(isActive, () => {
    form.categoria = '';
    errors.categoria = null;
});

const initialForm = {
    titulo: '',
    fecha: '',
    monto: '',
    categoria: '',
    descripcion: '',
    reporte: '', // ID del reporte seleccionado
    modoAsignacion: 'automatico' // 'automatico' o 'manual'
};
const form = reactive({ ...initialForm });

const errors = reactive({
    titulo: null,
    fecha: null,
    monto: null,
    categoria: null,
    descripcion: null,
    reporte: null
});

const clearError = (field) => {
    errors[field] = null;
    message.value = '';
};

const reporteSugerido = computed(() => {
    if (!form.fecha) return '';
    const fecha = new Date(form.fecha + 'T00:00:00'); // Evita problemas de zona horaria
    const mes = String(fecha.getMonth() + 1).padStart(2, '0');
    const anio = fecha.getFullYear();
    return `Reporte ${mes}-${anio}`;
});

function validate() {
    let isValid = true;
    Object.keys(errors).forEach(key => errors[key] = null);

    if (!form.titulo.trim()) {
        errors.titulo = 'El concepto es obligatorio';
        isValid = false;
    }
    if (!form.fecha) {
        errors.fecha = 'Selecciona una fecha';
        isValid = false;
    }
    if (!form.monto || form.monto <= 0) {
        errors.monto = 'Ingresa un monto válido';
        isValid = false;
    }
    if (!form.categoria) {
        errors.categoria = 'Selecciona una categoría';
        isValid = false;
    }

    // 🔧 NUEVO: Validar reporte si es modo manual
    if (form.modoAsignacion === 'manual' && !form.reporte) {
        errors.reporte = 'Selecciona un reporte';
        isValid = false;
    }

    return isValid;
}

async function agregarRegistro(e) {
    e.preventDefault();
    if (!validate()) return;

    try {
        const payload = {
            username: currentUser,
            tipo: isActive.value ? 0 : 1,

            titulo: form.titulo,
            fecha: form.fecha,
            monto: parseFloat(form.monto),

            /**
             * 🔧 CATEGORÍA POR ID:
             * Enviamos el ID numérico que capturamos del value del select.
             */
            id_categoria: parseInt(form.categoria),

            descripcion: form.descripcion || ''
        };

        if (form.modoAsignacion === 'manual') {
            payload.id_reporte = parseInt(form.reporte);
        }

        const response = await axios.post('http://127.0.0.1:5000/agregarRegistroContable', payload);

        message.value = response.data.message || '¡Registro agregado correctamente!';

        // Resetear formulario y recargar datos
        Object.assign(form, initialForm);
        await fetchReportes();

        setTimeout(() => { message.value = ''; }, 3000);

    } catch (error) {
        console.error("Error al agregar registro", error);
        message.value = error.response?.data?.message || 'Error al intentar guardar.';
    }
}
</script>

<template>
    <Menu />
    <div class="home-container">
        <Options />

        <div class="home">
            <h3>Agregar Registro Contable</h3>

            <div class="container">
                <div class="form-section">
                    <form class="form" @submit="agregarRegistro" autocomplete="off">
                        <div class="grid-form">
                            <div class="form-group">
                                <label>Tipo:</label>
                                <button type="button" class="btn-tipo" @click="isActive = !isActive"
                                    :class="{ 'btn-active': isActive, 'btn-inactive': !isActive }">
                                    {{ isActive ? 'Ingreso' : 'Gasto' }}
                                </button>
                            </div>

                            <div class="form-group">
                                <label for="titulo">Concepto:</label>
                                <input v-model="form.titulo" @input="clearError('titulo')" type="text" id="titulo"
                                    :class="['form-control', { 'is-invalid': errors.titulo }]" />
                                <span v-if="errors.titulo" class="error">{{ errors.titulo }}</span>
                            </div>

                            <div class="form-group">
                                <label for="fecha">Fecha:</label>
                                <input v-model="form.fecha" @change="clearError('fecha')" type="date" id="fecha"
                                    :class="['form-control', { 'is-invalid': errors.fecha }]" />
                                <span v-if="errors.fecha" class="error">{{ errors.fecha }}</span>
                            </div>

                            <div class="form-group">
                                <label for="monto">Monto:</label>
                                <input v-model.number="form.monto" @input="clearError('monto')" type="number" id="monto"
                                    :class="['form-control', { 'is-invalid': errors.monto }]" step="0.01" />
                                <span v-if="errors.monto" class="error">{{ errors.monto }}</span>
                            </div>

                            <div class="form-group">
                                <label for="categoria">Categoría:</label>
                                <select v-model="form.categoria" @change="clearError('categoria')" id="categoria"
                                    :class="['form-control', { 'is-invalid': errors.categoria }]">
                                    <option disabled value="">Selecciona una categoría</option>
                                    <option v-for="cat in categoriasFiltradas" :key="cat[0]" :value="cat[0]">
                                        {{ cat[1] }}
                                    </option>
                                </select>
                                <span v-if="errors.categoria" class="error">{{ errors.categoria }}</span>
                            </div>

                            <!-- 🔧 NUEVO: Selector de modo de asignación -->
                            <div class="form-group">
                                <label>Asignación de Reporte:</label>
                                <div class="radio-group">
                                    <label class="radio-label">
                                        <input type="radio" v-model="form.modoAsignacion" value="automatico" />
                                        <span>Automático <small v-if="reporteSugerido">({{ reporteSugerido
                                                }})</small></span>
                                    </label>
                                    <label class="radio-label">
                                        <input type="radio" v-model="form.modoAsignacion" value="manual" />
                                        <span>Manual</span>
                                    </label>
                                </div>
                            </div>

                            <div class="form-group" v-if="form.modoAsignacion === 'manual'">
                                <label for="reporte">Reporte:</label>
                                <select v-model="form.reporte" @change="clearError('reporte')" id="reporte"
                                    :class="['form-control', { 'is-invalid': errors.reporte }]">
                                    <option disabled value="">Selecciona un reporte</option>
                                    <option v-for="rep in reportes" :key="rep.Id_reporte" :value="rep.Id_reporte">
                                        {{ rep.Nombre }}
                                    </option>
                                </select>
                                <span v-if="errors.reporte" class="error">{{ errors.reporte }}</span>
                            </div>

                            <div class="form-group" :class="{ 'full-width': form.modoAsignacion === 'automatico' }">
                                <label for="descripcion">Descripción:</label>
                                <textarea v-model="form.descripcion" @input="clearError('descripcion')" id="descripcion"
                                    placeholder="Escribe una descripción"
                                    :class="['form-control', { 'is-invalid': errors.descripcion }]"></textarea>
                                <span v-if="errors.descripcion" class="error">{{ errors.descripcion }}</span>
                            </div>
                        </div>
                        <div class="buttons">
                            <button type="submit" class="btn-primary">Agregar Registro</button>
                        </div>
                    </form>

                    <Transition name="fade">
                        <div v-if="message" class="message">{{ message }}</div>
                    </Transition>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.home-container {
    display: flex;
    flex-direction: row;
    background: #f8fafc;
    min-height: 100vh;
    height: 100vh;
    max-height: 100vh;
    overflow: hidden;
}

.home {
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #334155;
    overflow: hidden;
    padding: 20px;
    box-sizing: border-box;
    padding: 40px;
}

.container {
    width: 80%;
    margin: 40px auto;
    padding: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.7);
    border-radius: 12px;
    border-style: dashed;
    border-color: var(--color-1);
}

.form-section {
    width: 100%;
}

.form {
    width: 100%;
}

.grid-form {
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px 24px;
}

.form-group {
    display: flex;
    flex-direction: column;
    position: relative;
}

.form-group.full-width {
    grid-column: 1 / -1;
}

label {
    font-weight: 600;
    margin-bottom: 6px;
}

.form-control {
    max-width: 300px;
    padding: 10px;
    border-radius: 6px;
    border: 1px solid #bbb;
    font-size: 1rem;
    background: #ffffff;
    color: #333;
}

textarea.form-control {
    min-height: 80px;
    resize: vertical;
    font-family: inherit;
    max-width: 100%;
}

.form-control:focus {
    border-color: #4ea5ff;
    outline: none;
    box-shadow: 0 0 6px rgba(78, 165, 255, 0.6);
}

.is-invalid {
    border-color: #e74c3c !important;
}

.error {
    color: #e74c3c;
    font-size: 0.85rem;
    margin-top: 4px;
    position: absolute;
    bottom: -18px;
    left: 0;
}

.radio-group {
    display: flex;
    flex-direction: row;
    gap: 8px;
}

.radio-label {
    display: flex;
    align-items: left;
    gap: 8px;
    cursor: pointer;
    font-weight: normal;
}

.radio-label input[type="radio"] {
    cursor: pointer;
    width: auto;
}

.radio-label small {
    color: #64748b;
    font-size: 0.85rem;
}

.buttons {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-top: 25px;
}

.message {
    margin-top: 1rem;
    color: #16a34a;
    font-size: 1rem;
    text-align: center;
    padding: 10px;
    border-radius: 6px;
    background: #d1fae5;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}

.btn-tipo {
    max-width: 300px;
    padding: 10px;
    border-radius: 6px;
    cursor: pointer;
    border: 1px solid #bbb;
    transition: background 0.3s;
    font-size: 1rem;
}

.btn-active {
    background-color: var(--color-2);
    color: rgb(33, 32, 32);
}

.btn-inactive {
    background-color: var(--fondo-2);
    color: rgb(33, 32, 32);
}

@media (max-width: 600px) {
    .grid-form {
        grid-template-columns: 1fr;
    }

    .form-group.full-width {
        grid-column: 1;
    }
}
</style>