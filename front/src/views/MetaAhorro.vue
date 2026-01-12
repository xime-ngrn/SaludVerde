<script setup>
import { ref, onMounted } from 'vue';
import Menu from '@/components/MenuBar.vue';
import Options from '@/components/OptionsBar.vue';
import Meta from '@/components/Meta.vue';
import { getAuthToken } from '@/utils/cookies';
import axios from 'axios';

const metas = ref([]);
const currentUser = getAuthToken();
const mostrarModal = ref(false);

const nuevaMeta = ref({ title: '', inicio: '', fin: '', ahorro: 0 });

const fetchMetas = async () => {
    try {
        const res = await axios.get(`http://127.0.0.1:5000/obtenerMetas?username=${currentUser}`);
        metas.value = res.data;
    } catch (e) { console.error("Error al cargar metas", e); }
};

const guardarMeta = async () => {
    try {
        await axios.post('http://127.0.0.1:5000/agregarMeta', {
            ...nuevaMeta.value,
            username: currentUser
        });
        mostrarModal.value = false;
        fetchMetas();
    } catch (e) { alert("Error al guardar"); }
};

onMounted(fetchMetas);
</script>

<template>
    <Menu />
    <div class="home-container">
        <Options />
        <div class="home">
            <h3>Metas de Ahorro</h3>
            <button class="btn-primary" @click="mostrarModal = true">Agregar Meta de Ahorro</button>
            <div class="metas">
                <Meta 
                    v-for="meta in metas" 
                    :key="meta.idMeta" 
                    :idMeta="meta.idMeta"
                    :title="meta.title" 
                    :ahorro="meta.ahorro" 
                    :progreso="meta.progreso"
                    :inicio="meta.inicio"
                    :fin="meta.fin"
                />
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