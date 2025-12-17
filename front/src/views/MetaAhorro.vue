<script setup>
import { ref } from 'vue'; // Importante importar ref
import Menu from '@/components/MenuBar2.vue';
import Options from '@/components/OptionsBar.vue';
import Meta from '@/components/Meta.vue';

// 1. Datos iniciales con formato de fecha correcto (como Strings)
const metas = ref([
    { title: 'Año Nuevo', inicio: '2025-10-25', fin: '2025-12-25', ahorro: 5000, progreso: 2000 },
    { title: 'Cumpleaños', inicio: '2025-12-10', fin: '2026-05-03', ahorro: 8000, progreso: 0 }
]);

const mostrarModal = ref(false);

// 2. Objeto para la nueva meta
const nuevaMeta = ref({
    title: '',
    inicio: '',
    fin: '',
    ahorro: 0,
    progreso: 0
});

function abrirModal() {
    // Reiniciar el formulario al abrir
    nuevaMeta.value = { title: '', inicio: '', fin: '', ahorro: 0, progreso: 0 };
    mostrarModal.value = true;
}

function guardarMeta() {
    if (nuevaMeta.value.title && nuevaMeta.value.ahorro > 0) {
        // Agregamos la nueva meta al arreglo reactivo
        metas.value.push({ ...nuevaMeta.value });
        
        // Cerramos el modal
        mostrarModal.value = false;
        console.log("Meta de ahorro guardada");
    }
}
</script>

<template>
    <Menu />
    
    <div class="home-container">
        <Options />

        <div class="home">
            <h3>Metas de Ahorro</h3>
            
            <button class="btn-primary" @click="abrirModal">Agregar Meta de Ahorro</button>
            
            <div class="metas">
                <Meta 
                    v-for="(meta, index) in metas" 
                    :key="index" 
                    :title="meta.title" 
                    :ahorro="meta.ahorro" 
                    :progreso="meta.progreso"
                    :inicio="meta.inicio"
                    :fin="meta.fin"
                />
            </div>
        </div>
    </div>

    <div v-if="mostrarModal" class="modal-overlay" @click.self="mostrarModal = false">
        <div class="modal-content">
            <h3>Crear Nueva Meta</h3>

            <div class="form-section">
                <form class="form" @submit.prevent="guardarMeta" autocomplete="off">
                    <div class="grid-form">
                        <div class="form-group">
                            <label>Nombre de la Meta:</label>
                            <input v-model="nuevaMeta.title" type="text" placeholder="Ej. Viaje a la playa" required>
                        </div>  
                        <div class="form-group">
                                <label>Fecha Inicio:</label>
                                <input v-model="nuevaMeta.inicio" type="date" required>
                        </div>
                        <div class="form-group">
                                <label>Fecha Fin:</label>
                                <input v-model="nuevaMeta.fin" type="date" required>
                            </div>

                        <div class="form-group">
                            <label>Monto Objetivo ($):</label>
                            <input v-model.number="nuevaMeta.ahorro" type="number" min="1" required>
                        </div>
                    </div>

                    <div class="buttons">
                        <button type="button" class="btn-cancel" @click="mostrarModal = false">Cancelar</button>
                        <button type="submit" class="btn-primary">Agregar Meta</button>
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
}

.home {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #334155;
    padding: 40px;
}

.btn-primary {
    align-self: flex-end;
}

.metas {
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

/* Estilos del Modal */
.modal-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.4);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-content {
    background: white;
    padding: 25px;
    border-radius: 15px;
    width: 450px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
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

</style>