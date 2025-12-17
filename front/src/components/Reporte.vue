<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
    title: { type: String, required: true },
    gastos: { type: Number, required: true },
    ingresos: { type: Number, required: true }
});

const isModalOpen = ref(false);

// Datos de ejemplo para la tabla (puedes pasarlos por props después)
const detalles = [
    { titulo: 'Tareas Vendidas', ingreso: 169, gasto: null },
    { titulo: 'Gasto Semanal', ingreso: 323, gasto: null },
    { titulo: 'Dulces Semana 1', ingreso: 65, gasto: null },
    { titulo: 'Desayuno', ingreso: null, gasto: 96 },
    { titulo: 'Cena Romántica', ingreso: null, gasto: 321 },
    { titulo: 'Transporte', ingreso: null, gasto: 54 },
];

const totalBalance = computed(() => props.ingresos - props.gastos);
</script>

<template>
    <div class="reporte" @click="isModalOpen = true">
        <img src="@/assets/images/reporte.png" alt="Icon" class="reporte-icon" />
        <h4>{{ props.title }}</h4>
    </div>

    <div v-if="isModalOpen" class="modal-overlay" @click.self="isModalOpen = false">
        <div class="modal-container">
            
            <div class="report-card-detail">
                <button class="close-btn" @click="isModalOpen = false">X</button>

                <h2 class="report-title">{{ props.title }}/2025</h2>

                <table class="report-table">
                    <thead>
                        <tr>
                            <th>Título</th>
                            <th>Ingreso</th>
                            <th>Gasto</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(item, index) in detalles" :key="index">
                            <td>{{ item.titulo }}</td>
                            <td>{{ item.ingreso ? '$ ' + item.ingreso : '' }}</td>
                            <td>{{ item.gasto ? '$ ' + item.gasto : '' }}</td>
                        </tr>
                        <tr class="subtotal-row">
                            <td></td>
                            <td>$ {{ props.ingresos }}</td>
                            <td>$ {{ props.gastos }}</td>
                        </tr>
                    </tbody>
                </table>

                <div class="total-badge">
                    Total: $ {{ totalBalance }}
                </div>
            </div>

            <div class="modal-actions">
                <button class="btn-primary">
                    Exportar a Excel
                </button>
            </div>
        </div>
    </div>
</template>

<style scoped>
/* Estilos de la Tarjeta Original */
.reporte {
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
.reporte:hover { 
    transform: scale(1.02); 
}

.modal-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-container {
    display: flex;
    flex-direction: column;
    gap: 20px;
    align-items: center;
}

.report-card-detail {
    background: white;
    border: 4px dashed var(--color-1);
    border-radius: 40px;
    padding: 40px;
    width: 500px;
    position: relative;
    color: #334155;
}

.close-btn {
    position: absolute;
    top: 25px; right: 30px;
    background: none; border: none;
    font-size: 1.5rem; font-weight: bold;
    cursor: pointer;
}
.close-btn:hover {
    color: #e53e3e;
}

img.reporte-icon {
    width: 48px;
    height: 48px;
    margin-bottom: 12px;
}

.report-title {
    margin-bottom: 20px;
    font-size: 1.4rem;
}

/* Tabla de Reporte */
.report-table {
    width: 100%;
    border-collapse: collapse;
}
.report-table th {
    text-align: left;
    padding-bottom: 10px;
    font-size: var(--text-subtitle-2);
}
.report-table td {
    padding: 8px 0;
    border-bottom: 2px solid #3b82f6;
    font-size: var(--text-small);
}
.report-table tr td:first-child { width: 50%; }

.subtotal-row td {
    border-bottom: none;
    padding-top: 15px;
    font-size: var(--text-small);
}

/* Badge de Total */
.total-badge {
    margin: 20px auto 0;
    border: 2px solid #000;
    border-radius: 15px;
    padding: 10px 30px;
    width: fit-content;
    font-size: 1.3rem;
    font-weight: bold;
}

/* Botones Inferiores */
.modal-actions {
    display: flex;
    gap: 15px;
    width: 100%;
}

.btn-primary {
    flex: 1;
}
</style>