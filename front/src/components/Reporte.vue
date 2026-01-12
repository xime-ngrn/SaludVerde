<script setup>
import { ref, computed } from 'vue';
import axios from 'axios';
import jsPDF from 'jspdf';
import autoTable from 'jspdf-autotable';

const props = defineProps({
    idReporte: { type: Number }, // Nuevo prop
    title: { type: String, required: true },
    gastos: { type: Number, required: true },
    ingresos: { type: Number, required: true }
});

const detalles = ref([]);
const isModalOpen = ref(false);

const fetchDetalles = async () => {
    try {
        const res = await axios.get(`http://127.0.0.1:5000/obtenerDetallesReporte?id=${props.idReporte}`);
        detalles.value = res.data; // Registros de la tabla 'Registro'
    } catch (e) {
        console.error("Error al obtener detalles", e);
    }
};

const abrirDetalles = () => {
    isModalOpen.value = true;
    if (props.idReporte) fetchDetalles();
};

const totalBalance = computed(() => props.ingresos - props.gastos);

const exportToPDF = () => {
    const doc = new jsPDF();
    doc.setFontSize(18);
    doc.text(`Reporte Mensual: ${props.title}`, 14, 22);
    
    doc.setFontSize(11);
    doc.setTextColor(100);
    doc.text(`Generado el: ${new Date().toLocaleDateString()}`, 14, 30);

    const tableData = detalles.value.map(item => [
        item.titulo,
        item.ingreso ? `$${item.ingreso}` : '-',
        item.gasto ? `$${item.gasto}` : '-'
    ]);

    autoTable(doc, {
        startY: 40,
        head: [['Título', 'Ingreso', 'Gasto']],
        body: tableData,
        foot: [['TOTALES', `$${props.ingresos}`, `$${props.gastos}`]],
        theme: 'striped',
        headStyles: { fillColor: [59, 130, 246] },
        footStyles: { fillColor: [241, 245, 249], textColor: [0, 0, 0], fontStyle: 'bold' }
    });

    const finalY = doc.lastAutoTable.finalY + 10;
    doc.setFontSize(14);
    doc.setTextColor(totalBalance.value >= 0 ? 0 : 200, 0, 0);
    doc.text(`Balance Total: $${totalBalance.value}`, 14, finalY);

    doc.save(`Reporte_${props.title.replace(/\s+/g, '_')}.pdf`);
};
</script>

<template>
    <div class="reporte" @click="abrirDetalles">
        <img src="@/assets/images/reporte.png" alt="Icon" class="reporte-icon" />
        <h4>{{ props.title }}</h4>
    </div>

    <div v-if="isModalOpen" class="modal-overlay" @click.self="isModalOpen = false">
        <div class="modal-container">
            
            <div class="report-card-detail">
                <button class="close-btn" @click="isModalOpen = false">X</button>

                <h2 class="report-title">{{ props.title }}</h2>

                <table class="report-table">
                    <thead>
                        <tr>
                            <th>Título</th>
                            <th>Ingreso</th>
                            <th>Gasto</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-if="detalles.length === 0">
                            <td colspan="3">No hay movimientos en este mes.</td>
                        </tr>
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

                <div class="total-badge" :class="totalBalance >= 0 ? 'positivo' : 'negativo'">
                    Balance: $ {{ totalBalance }}
                </div>
            </div>

            <div class="modal-actions">
                <button class="btn-primary" @click="exportToPDF">
                    Exportar a PDF
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
.total-badge.positivo {
    background-color: #d1fae5;
    border-color: #10b981;
    color: #065f46;
}
.total-badge.negativo {
    background-color: #fee2e2;
    border-color: #ef4444;
    color: #991b1b;
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