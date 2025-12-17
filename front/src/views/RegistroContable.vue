<script setup>
import { ref } from 'vue';
import Menu from '@/components/MenuBar2.vue';
import Options from '@/components/OptionsBar.vue';

const form = ref({
    titulo: '',
    fecha: '',
    mes: '',
    monto: '',
    categoria: '',
    tipo: ''
});

const message = ref('');

function submitForm(e) {
    e.preventDefault();
    // Basic validation
    if (
        !form.value.titulo ||
        !form.value.fecha ||
        !form.value.mes ||
        !form.value.monto ||
        !form.value.categoria ||
        !form.value.tipo
    ) {
        message.value = 'Por favor, completa todos los campos.';
        return;
    }
    // Simulate submit
    message.value = 'Registro agregado correctamente.';
    // Reset form
    form.value = {
        titulo: '',
        fecha: '',
        mes: '',
        monto: '',
        categoria: '',
        tipo: ''
    };
}
</script>

<template>
    <Menu />
    <div class="home-container">
        <Options />
        <div class="home">
            <h3>Agregar Registro Contable</h3>
            <div class="registro">
                <form @submit="submitForm" autocomplete="off">
                    <div>
                        <label for="titulo">Título</label>
                        <input v-model="form.titulo" type="text" id="titulo" name="titulo" required />
                    </div>
                    <div>
                        <label for="fecha">Fecha</label>
                        <input v-model="form.fecha" type="date" id="fecha" name="fecha" required />
                    </div>
                    <div>
                        <label for="mes">Mes</label>
                        <select v-model="form.mes" id="mes" name="mes" required>
                            <option disabled value="">Selecciona un mes</option>
                            <option value="enero">Enero</option>
                            <option value="febrero">Febrero</option>
                            <option value="marzo">Marzo</option>
                            <option value="abril">Abril</option>
                            <option value="mayo">Mayo</option>
                            <option value="junio">Junio</option>
                            <option value="julio">Julio</option>
                            <option value="agosto">Agosto</option>
                            <option value="septiembre">Septiembre</option>
                            <option value="octubre">Octubre</option>
                            <option value="noviembre">Noviembre</option>
                            <option value="diciembre">Diciembre</option>
                        </select>
                    </div>
                    <div>
                        <label for="monto">Monto</label>
                        <input v-model="form.monto" type="number" id="monto" name="monto" min="0" step="0.01" required />
                    </div>
                    <div>
                        <label for="categoria">Categoría</label>
                        <select v-model="form.categoria" id="categoria" name="categoria" required>
                            <option disabled value="">Selecciona una categoría</option>
                            <option value="alimentacion">Alimentación</option>
                            <option value="servicios">Servicios</option>
                            <option value="transporte">Transporte</option>
                            <option value="educacion">Educación</option>
                        </select>
                    </div>
                    <div>
                        <label for="tipo">Tipo</label>
                        <select v-model="form.tipo" id="tipo" name="tipo" required>
                            <option disabled value="">Selecciona un tipo</option>
                            <option value="ingreso">Ingreso</option>
                            <option value="gasto">Gasto</option>
                        </select>
                    </div>
                    <button type="submit">Agregar Registro</button>
                </form>
                <div v-if="message" class="message">{{ message }}</div>
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
    font-size: 1.5rem;
    color: #334155;
    overflow: hidden;
    padding: 20px;
    box-sizing: border-box;
}
.registro {
    background: #ffffff;
    padding: 20px;
    border-style: dashed;
    border-color: var(--color-1);
    border-radius: 12px;
    width: 100%;
    max-width: 800px; /* Aumenta el ancho máximo para acomodar 2 columnas */
    margin-top: 20px;
    box-sizing: border-box;
}
.registro form {
    display: grid;
    /* Define la cuadrícula para 2 columnas de igual ancho */
    grid-template-columns: 1fr 1fr;
    /* Espacio entre las columnas y las filas */
    gap: 20px;
}
.registro form > div {
    margin-bottom: 0; /* Lo gestiona el 'gap' del grid */
}
/* Asegura que el botón de envío ocupe ambas columnas */
.registro form button[type="submit"] {
    grid-column: 1 / -1; /* Ocupa desde la primera hasta la última columna */
    width: auto;
}
.registro label {
    display: block;
    margin-bottom: 0.25rem;
    font-size: 1rem;
}
.registro input,
.registro select {
    width: 100%;
    padding: 0.5rem;
    font-size: 1rem;
    border-radius: 6px;
    border: 1px solid #cbd5e1;
    box-sizing: border-box;
}
button[type="submit"] {
    background: var(--color-1, #38bdf8);
    color: #fff;
    border: none;
    border-radius: 6px;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    cursor: pointer;
    margin-top: 1rem;
}
.message {
    margin-top: 1rem;
    color: #16a34a;
    font-size: 1rem;
}

/* Media Query para hacer el formulario de 1 columna en pantallas pequeñas */
@media (max-width: 600px) {
    .registro form {
        grid-template-columns: 1fr; /* Una sola columna en dispositivos pequeños */
    }
}
</style>