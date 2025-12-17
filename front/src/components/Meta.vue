<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
    title: { type: String, required: true },
    ahorro: { type: Number, required: true },
    progreso: { type: Number, required: true },
    inicio: { type: [Date, String], required: true },
    fin: { type: [Date, String], required: true }
});

const isModalOpen = ref(false);

// Función para formatear fechas de manera legible
const formatDate = (date) => {
    if (!date) return '--';
    const d = new Date(date);
    return d.toLocaleDateString('es-ES', { day: '2-digit', month: '2-digit', year: 'numeric' });
};

// Cálculo del ahorro necesario por mes
const ahorroPorMes = computed(() => {
    const start = new Date(props.inicio);
    const end = new Date(props.fin);
    const months = (end.getFullYear() - start.getFullYear()) * 12 + (end.getMonth() - start.getMonth());
    return months > 0 ? (props.ahorro / months).toFixed(2) : props.ahorro;
});

// Porcentaje de progreso
const porcentajeProgreso = computed(() => {
    return ((props.progreso / props.ahorro) * 100).toFixed(0) + '%';
});
</script>

<template>
    <div class="meta-card-preview" @click="isModalOpen = true">
        <img src="@/assets/images/meta.png" alt="Icon" class="reporte-icon" />
        <h4>{{ props.title }}</h4>
    </div>

    <div v-if="isModalOpen" class="modal-overlay" @click.self="isModalOpen = false">
        <div class="meta-card-detail">
            <div class="header-modal">
                <h2 class="modal-title">Meta de Ahorro</h2>
                <button class="close-btn" @click="isModalOpen = false">X</button>
            </div>
            
            <hr>

            <div class="modal-body">
                <div class="info-column">
                    <p><strong>Título:</strong> {{ props.title }}</p>
                    <p><strong>Monto de Ahorro:</strong> $ {{ props.ahorro }}</p>
                    <p><strong>Inicio:</strong> {{ formatDate(props.inicio) }}</p>
                    <p><strong>Término:</strong> {{ formatDate(props.fin) }}</p>
                    <p><strong>Objetivo:</strong> {{ props.title }}</p>
                </div>
                
                <div class="deposit-column">
                    <div class="deposited-box">
                        <span>Depositado:</span>
                        <div class="deposited-value">$ {{ props.progreso }}</div>
                    </div>
                </div>
            </div>

            <hr></hr>

            <div class="modal-footer">
                <div class="footer-stats">
                    <span>Progreso: <strong>{{ porcentajeProgreso }}</strong></span>
                    <span>Ahorro por Mes: <strong>$ {{ ahorroPorMes }}</strong></span>
                </div>
                <div class="total-badge">
                    Ahorro Total: $ {{ props.progreso }}
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
/* Card original */
.meta-card-preview {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 16px;
    background-color: #ffffff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 200px;
    cursor: pointer;
    transition: transform 0.2s;
}
.meta-card-preview:hover {
    transform: scale(1.02);
}

/* Estilos del Modal basados en la imagen */
.modal-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.4);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.meta-card-detail {
    background: white;
    border: 4px dashed var(--color-1); /* Borde punteado azul */
    border-radius: 50px;
    padding: 30px 50px;
    width: 600px;
    position: relative;
    color: #1e293b;
}

.header-modal {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
}

h2 {
    margin-bottom: 0;
    font-size: 1.4rem;
}

.close-btn {
    position: absolute;
    right: -10px;
    top: -5px;
    background: none;
    border: none;
    font-size: 1.5rem;
    font-weight: bold;
    cursor: pointer;
}
.close-btn:hover {
    color: #e53e3e;
}


.modal-body {
    display: flex;
    justify-content: space-between;
}

.info-column p {
    margin: 15px 0;
    font-size: 1.1rem;
}

.info-column strong {
    font-weight: 800;
}

/* Caja de depositado (Derecha) */
.deposited-box {
    border: 2px solid #c6f6d5;
    border-radius: 20px;
    padding: 20px;
    width: 220px;
    height: 200px;
    display: flex;
    flex-direction: column;
    font-weight: bold;
    font-size: 1.2rem;
}

.deposited-value {
    margin-top: auto;
    text-align: center;
    font-size: 1.5rem;
}

/* Footer y Badge */
.modal-footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
}

.footer-stats {
    width: 100%;
    display: flex;
    justify-content: space-between;
    font-size: 1.1rem;
    color: #64748b;
}

.total-badge {
    border: 2px solid #c6f6d5;
    background-color: white;
    border-radius: 15px;
    padding: 8px 30px;
    font-size: 1.2rem;
    font-weight: bold;
    color: #000;
    width: fit-content;
}

.reporte-icon {
    width: 50px;
    margin-bottom: 10px;
}

hr {
    margin: 1.2rem;
}
</style>