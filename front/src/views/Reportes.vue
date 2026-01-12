<script setup>
import { ref, onMounted } from 'vue';
import Menu from '@/components/MenuBar.vue';
import Options from '@/components/OptionsBar.vue';
import Reporte from '@/components/Reporte.vue';
import { getAuthToken } from '@/utils/cookies';
import axios from 'axios';

const reportes = ref([]);
const currentUser = getAuthToken();
const error = ref('');

const fetchReportes = async () => {
    try {
        const response = await axios.get(`api/obtenerReportes?username=${currentUser}`);
        
        // 🔧 CORREGIDO: Procesar los datos para calcular ingresos y gastos
        reportes.value = response.data.reportes.map(reporte => ({
            idReporte: reporte.Id_reporte, // 🔧 AGREGADO: ID del reporte
            title: reporte.Nombre,
            gastos: reporte.total_gastos || 0,
            ingresos: reporte.total_ingresos || 0
        }));
        
        console.log("Reportes cargados:", reportes.value);
    } catch (e) {
        error.value = 'Error al cargar los reportes.';
        console.error("Error cargando reportes", e);
    }
};

onMounted(fetchReportes);

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

async function guardarReporte() {
    if (!nuevoReporte.value.title.trim()) {
        alert('El título es obligatorio');
        return;
    }

    try {
        // 🔧 AGREGADO: Guardar el reporte en el backend
        const response = await axios.post('api/crearReporte', {
            username: currentUser,
            nombre: nuevoReporte.value.title
        });

        console.log("Reporte creado:", response.data);
        
        // Recargar reportes
        await fetchReportes();
        
        // Cerrar modal
        mostrarModal.value = false;
    } catch (e) {
        console.error("Error al crear reporte", e);
        alert('Error al crear el reporte');
    }
}
</script>

<template>
    <Menu />
    
    <div class="home-container">
        <Options />

        <div class="home">
            <div class="header">
                <h3>Reportes Mensuales</h3>
                <button class="btn-primary" @click="abrirModal">+ Nuevo Reporte</button>
            </div>
            
            <span v-if="error" class="error">{{ error }}</span>
            
            <div class="reportes">
                <Reporte 
                    v-for="reporte in reportes" 
                    :key="reporte.idReporte"
                    :idReporte="reporte.idReporte"
                    :title="reporte.title" 
                    :gastos="reporte.gastos" 
                    :ingresos="reporte.ingresos" 
                />
                
                <div v-if="reportes.length === 0" class="empty-state">
                    <p>No hay reportes aún</p>
                    <button class="btn-primary" @click="abrirModal">Crear primer reporte</button>
                </div>
            </div>
        </div>
    </div>

    <div v-if="mostrarModal" class="modal-overlay" @click.self="mostrarModal = false">
        <div class="modal-content">
            <h3>Nuevo Reporte</h3>

            <div class="form-section">
                <form class="form" @submit.prevent="guardarReporte" autocomplete="off">
                    <div class="grid-form">
                        <div class="form-group full-width">
                            <label>Mes / Título:</label>
                            <input 
                                v-model="nuevoReporte.title" 
                                type="text" 
                                placeholder="Ej. Enero 2026" 
                                required
                                class="form-control"
                            >
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
    color: #334155;
    padding: 40px;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
}

.header h3 {
    font-size: 1.5rem;
}

.reportes {
    flex-grow: 1;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: flex-start;
    align-content: flex-start;
    overflow-y: auto;
    max-height: calc(100vh - 200px);
}

.empty-state {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
    padding: 60px 20px;
    color: #64748b;
}

.error {
    color: #e74c3c;
    margin-bottom: 20px;
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

.modal-content h3 {
    margin-bottom: 20px;
}

.form-section {
    width: 100%;
}

.form {
    width: 100%;
}

.grid-form {
    display: grid;
    grid-template-columns: 1fr;
    gap: 18px;
}

.form-group {
    display: flex;
    flex-direction: column;
}

.full-width {
    grid-column: 1 / -1;
}

label {
    font-weight: 600;
    margin-bottom: 6px;
    font-size: 0.95rem;
}

.form-control {
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
    gap: 10px;
}

@media (max-width: 900px) {
    .home-container {
        flex-direction: column;
        overflow-y: auto;
    }

    .home {
        padding: 20px;
    }

    .header {
        flex-direction: column;
        gap: 15px;
        align-items: stretch;
    }
    
    .reportes {
        justify-content: center;
    }
}
</style>