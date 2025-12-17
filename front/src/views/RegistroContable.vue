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

            <div class="container">
                <div class="form-section">
                    <form class="form" @submit="submitForm" autocomplete="off">
                        <div class="grid-form">
                            <div class="form-group">
                                <label for="titulo">Título</label>
                                <input v-model="form.titulo" type="text" id="titulo" class="form-control" name="titulo" required />
                            </div>
                            <div class="form-group">
                                <label for="fecha">Fecha</label>
                                <input v-model="form.fecha" type="date" id="fecha" class="form-control" name="fecha" required />
                            </div>
                            <div class="form-group">
                                <label for="mes">Registro</label>
                                <select v-model="form.mes" id="mes" class="form-control" name="mes" required>
                                    <option disabled value="">Selecciona un Registro</option>
                                    <option value="mayo">Mayo</option>
                                    <option value="junio">Junio</option>
                                    <option value="julio">Julio</option>
                                    <option value="agosto">Agosto</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="monto">Monto</label>
                                <input v-model="form.monto" type="number" id="monto" class="form-control" name="monto" min="0" step="0.01" required />
                            </div>
                            <div class="form-group">
                                <label for="categoria">Categoría</label>
                                <select v-model="form.categoria" id="categoria" class="form-control" name="categoria" required>
                                    <option disabled value="">Selecciona una categoría</option>
                                    <option value="alimentacion">Alimentación</option>
                                    <option value="servicios">Servicios</option>
                                    <option value="transporte">Transporte</option>
                                    <option value="educacion">Educación</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="tipo">Tipo</label>
                                <select v-model="form.tipo" id="tipo" class="form-control" name="tipo" required>
                                    <option disabled value="">Selecciona un tipo</option>
                                    <option value="ingreso">Ingreso</option>
                                    <option value="gasto">Gasto</option>
                                </select>
                            </div>
                        </div>
                        
                        <div class="buttons">
                            <button type="submit" class="btn-primary">Agregar Registro</button>
                        </div>
                    </form>
                    <div v-if="message" class="message">{{ message }}</div>
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

.form-control:focus {
    border-color: #4ea5ff;
    outline: none;
    box-shadow: 0 0 6px rgba(78, 165, 255, 0.6);
}

.error {
    color: #e74c3c;
    font-size: 0.85rem;
    margin-top: 4px;
    position: absolute;
    bottom: -18px;
    left: 0;
}

.general-error {
    display: block;
    color: #e74c3c;
    text-align: center;
    margin: 10px 0;
    font-size: 0.95rem;
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
}

@media (max-width: 600px) {
    .registro form {
        grid-template-columns: 1fr; /* Una sola columna en dispositivos pequeños */
    }
}
</style>