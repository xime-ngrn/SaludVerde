<script setup>
import { ref } from 'vue';
import Menu from '@/components/MenuBar2.vue';
import Options from '@/components/OptionsBar.vue';
import Reporte from '@/components/Reporte.vue';

const reportes = ref([
    { title: 'Mayo', gastos: 1200, ingresos: 3000 },
    { title: 'Junio', gastos: 3500, ingresos: 9000 },
    { title: 'Julio', gastos: 15000, ingresos: 36000 },
    { title: 'Agosto', gastos: 2000, ingresos: 3800 }
]);

const mostrarModal = ref(false);
const nuevoReporte = ref({
    title: '',
    gastos: 0,
    ingresos: 0
});

function abrirModal() {
    nuevoReporte.value = { title: '', gastos: 0, ingresos: 0 };
    mostrarModal.value = true;
}

function guardarReporte() {
    if (nuevoReporte.value.title) {
        // Agregamos una copia del objeto al arreglo reactivo
        reportes.value.push({ ...nuevoReporte.value });
        
        mostrarModal.value = false;
        
        console.log("Reporte agregado correctamente");
    }
}

</script>

<template>
    <Menu />
    
    <div class="home-container">
        <Options />

        <div class="home">
            <h3>Reportes Mensuales</h3>

            <button class="btn-primary" @click="abrirModal">Agregar Reporte</button>
            
            <div class="reportes">
                <Reporte v-for="(reporte, index) in reportes" :key="index" :title="reporte.title" :gastos="reporte.gastos" :ingresos="reporte.ingresos" />
            </div>
        </div>
    </div>

    <div v-if="mostrarModal" class="modal-overlay" @click.self="mostrarModal = false">
        <div class="modal-content">
            <h3>Nuevo Reporte</h3>

            <div class="form-section">
                <form class="form" @submit.prevent="guardarReporte" autocomplete="off">
                    <div class="grid-form">
                        <div class="form-group">
                            <label>Mes / Título:</label>
                            <input v-model="nuevoReporte.title" type="text" placeholder="Ej. Septiembre" required>
                        </div>
                        <div class="form-group">
                            <label>Ingresos ($):</label>
                            <input v-model.number="nuevoReporte.ingresos" type="number" min="0">
                        </div>
                        <div class="form-group">
                            <label>Gastos ($):</label>
                            <input v-model.number="nuevoReporte.gastos" type="number" min="0">
                        </div>
                    </div>

                    <div class="buttons">
                        <button type="button" class="btn-cancel" @click="mostrarModal = false">Cancelar</button>
                        <button type="submit" class="btn-primary">Guardar Reporte</button>
                    </div>
                </form>
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
    overflow-y: auto;
}
.home {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 1.5rem;
    color: #334155;
    padding: 40px;
}
.reportes {
    flex-grow: 1;
    padding: 20px;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    align-content: flex-start;
    font-size: 1.5rem;
    color: #334155;
    overflow-y: auto;
    height: auto;
    max-height: 100vh;
}
.btn-primary {
    align-self: flex-end;
}

.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 2000;
}

.modal-content {
    background: white;
    padding: 30px;
    border-radius: 12px;
    width: 400px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

.form-section {
    width: 100%;
}

.form {
    width: 100%;
}

.grid-form {
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

.buttons {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    margin-top: 25px;
}

@media (max-width: 900px) {
    .home-container {
        flex-direction: column; /* Mobile: OptionsBar arriba de Home */
        overflow-y: auto; /* El scroll lo manejará el container principal */
    }

    /* 💡 Ocultar OptionsBar para mobile. 
       Esto usualmente se maneja haciendo el Options un componente de menú de hamburguesa. */
    .options-bar {
        /* Para simular que Options se convierte en una barra horizontal o se oculta. 
           Si no lo vas a ocultar, asegúrate de que no tenga un 'width' fijo. */
        width: 100%;
        min-height: auto;
        /* display: none; */ 
    }

    .home {
        padding: 10px;
        /* En mobile, puede ser mejor que los reportes ocupen todo el ancho para una mejor lectura. */
        justify-content: center; 
    }
    
    /* Si el componente Reporte no es flexible, hazlo 100% de ancho en mobile. */
    /* Aquí necesitarías saber la clase raíz del componente Reporte. 
       Ejemplo: .reporte-card { width: 100%; } */
}
</style>