<script setup>
import { ref, computed, onMounted } from 'vue';
import Menu from '@/components/MenuBar.vue';
import Options from '@/components/OptionsBar.vue';
import Tip from '@/components/Tip.vue';
import axios from 'axios';
import { getAuthToken } from '@/utils/cookies';
import { Bar, Pie, Line, Doughnut, Radar } from 'vue-chartjs';
import {
    Chart as ChartJS, Title, Tooltip, Legend, BarElement, 
    CategoryScale, LinearScale, ArcElement, PointElement, LineElement, Filler, RadialLinearScale
} from 'chart.js';

// Registro único de componentes
ChartJS.register(
    Title, Tooltip, Legend, BarElement, CategoryScale, 
    LinearScale, ArcElement, PointElement, LineElement, Filler, RadialLinearScale
);

const currentUser = getAuthToken();

const stats = ref({
    ingresosPorCategoria: { labels: [], values: [] },
    progresoMetas: [],
    historicoGastos: { meses: [], montos: [] },
    gastosPorCategoria: { labels: [], values: [] },
    comparativaMensual: { nombres: [], ingresos: [], gastos: [] },
    distribucionRadar: { labels: [], values: [] } 
});

// 1. Gráfico de Metas (Barras Apiladas)
const metasChartData = computed(() => ({
    labels: stats.value.progresoMetas.map(m => m.objetivo),
    datasets: [
        { label: 'Ahorrado $', backgroundColor: '#10b981', data: stats.value.progresoMetas.map(m => m.actual) },
        { label: 'Faltante $', backgroundColor: '#e2e8f0', data: stats.value.progresoMetas.map(m => m.faltante) }
    ]
}));

// 2. Gráfico de Fuentes de Ingreso (Pie)
const ingresosChartData = computed(() => ({
    labels: stats.value.ingresosPorCategoria.labels,
    datasets: [{
        backgroundColor: ['#34d399', '#3b82f6', '#fbbf24', '#f87171', '#a78bfa'],
        data: stats.value.ingresosPorCategoria.values
    }]
}));

// 3. Gráfico de Histórico (Line)
const historicoChartData = computed(() => ({
    labels: stats.value.historicoGastos.meses,
    datasets: [{
        label: 'Gastos Mensuales',
        borderColor: '#f87171',
        backgroundColor: 'rgba(248, 113, 113, 0.2)',
        data: stats.value.historicoGastos.montos,
        fill: true,
        tension: 0.4
    }]
}));

// Gráfico de Gastos por Categoría (Dona)
const gastosCatChartData = computed(() => ({
    labels: stats.value.gastosPorCategoria.labels,
    datasets: [{
        label: 'Gastado $',
        backgroundColor: ['#f87171', '#fb923c', '#fbbf24', '#f472b6', '#a78bfa'],
        hoverOffset: 4,
        data: stats.value.gastosPorCategoria.values
    }]
}));

const comparativaChartData = computed(() => ({
    labels: stats.value.comparativaMensual.nombres,
    datasets: [
        {
            label: 'Ingresos $',
            backgroundColor: '#10b981', // Verde
            data: stats.value.comparativaMensual.ingresos
        },
        {
            label: 'Gastos $',
            backgroundColor: '#f87171', // Rojo
            data: stats.value.comparativaMensual.gastos
        }
    ]
}));

const radarChartData = computed(() => ({
    labels: stats.value.distribucionRadar.labels,
    datasets: [{
        label: 'Perfil de Gastos',
        data: stats.value.distribucionRadar.values,
        backgroundColor: 'rgba(59, 130, 246, 0.2)', // Azul transparente
        borderColor: '#3b82f6',
        pointBackgroundColor: '#3b82f6',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: '#3b82f6'
    }]
}));

const radarOptions = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        r: {
            angleLines: { display: true },
            suggestedMin: 0
        }
    }
};

const fetchData = async () => {
    stats.value.ingresosPorCategoria.labels = [];
    stats.value.gastosPorCategoria.labels = [];
    
    try {
        const res = await axios.get(`http://127.0.0.1:5000/obtenerEstadisticas?username=${currentUser}`);
        stats.value = res.data;
    } catch (e) {
        console.error("Error al cargar estadísticas:", e.response?.data || e.message);
    }
};

onMounted(fetchData);

const stackOptions = { responsive: true, maintainAspectRatio: false, scales: { x: { stacked: true }, y: { stacked: true } } };
const chartOptions = { responsive: true, maintainAspectRatio: false };
</script>

<template>
    <Menu />
    <div class="home-container">
        <Options />
        <div class="home">
            <Tip />
            
            <div class="dashboard-grid">
                <div class="chart-card" v-if="stats.ingresosPorCategoria.labels.length > 0">
                    <h4>Fuentes de Ingreso</h4>
                    <div class="chart-wrapper">
                        <Pie :data="ingresosChartData" :options="chartOptions" />
                    </div>
                </div>

                <div class="chart-card" v-if="stats.gastosPorCategoria.labels.length > 0">
                    <h4>Gastos Recientes</h4>
                    <div class="chart-wrapper">
                        <Doughnut :data="gastosCatChartData" :options="chartOptions" />
                    </div>
                </div>

                <div class="chart-card" v-if="stats.progresoMetas.length > 0">
                    <h4>Progreso de Metas</h4>
                    <div class="chart-wrapper">
                        <Bar :data="metasChartData" :options="stackOptions" />
                    </div>
                </div>
                <div class="chart-card">
                    <h4>Análisis de Perfil (Categorías)</h4>
                    <div class="chart-wrapper">
                        <Radar :data="radarChartData" :options="radarOptions" />
                    </div>
                </div>

                <div class="chart-card wide" v-if="stats.comparativaMensual.nombres.length > 0">
                    <h4>Ingresos vs Gastos por Reporte</h4>
                    <div class="chart-wrapper">
                        <Bar :data="comparativaChartData" :options="chartOptions" />
                    </div>
                </div>

                <!--
                <div class="chart-card wide" v-if="stats.historicoGastos.meses.length > 0">
                    <h4>Histórico de Gastos</h4>
                    <div class="chart-wrapper">
                        <Line :data="historicoChartData" :options="chartOptions" />
                    </div>
                </div>
                -->

                <div v-if="stats.progresoMetas.length === 0 && stats.ingresosPorCategoria.labels.length === 0" class="loading">
                    No hay datos suficientes para generar gráficos. ¡Comienza registrando movimientos!
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.home-container {
    display: flex;
    background: #f8fafc;
    height: 100vh;
}
.home {
    flex: 1;
    overflow-y: auto; /* Permitir scroll si hay muchos gráficos */
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.dashboard-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    width: 100%;
}

.chart-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.chart-card.wide {
    grid-column: span 2;
}

.chart-wrapper {
    height: 250px;
    position: relative;
}

h4 {
    font-size: 1.1rem;
    margin-bottom: 15px;
    color: #475569;
    text-align: center;
}
</style>