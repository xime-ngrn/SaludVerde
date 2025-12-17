<script setup>
import { ref } from 'vue';

const images = import.meta.glob('@/assets/images/*.png', { eager: true, import: 'default' });

const tips = ref([
    {
        id: 1,
        text: 'Ahorrar al menos el 20% de tus ingresos mensuales puede ayudarte a construir un fondo de emergencia sólido y alcanzar tus metas financieras a largo plazo.',
        image: images['/src/assets/images/bolsa-de-dinero1.png']
    },
    {
        id: 2,
        text: 'Crear un presupuesto mensual te permite tener un mejor control de tus gastos y te ayuda a identificar áreas donde puedes ahorrar más.',
        image: images['/src/assets/images/goals.png']
    },
    {
        id: 3,
        text: 'Invertir en una cuenta de ahorro con intereses compuestos puede hacer que tu dinero crezca significativamente con el tiempo.',
        image: images['/src/assets/images/money-up.png']
    },
    {
        id: 4,
        text: 'Pagar tus deudas con tasas de interés altas primero puede ahorrarte dinero a largo plazo y mejorar tu salud financiera. ¡No te arriesgues a pagar intereses de más!',
        image: images['/src/assets/images/dar-dinero.png']
    },
    {
        id: 5,
        text: 'Invertir en un seguro de vida te permitirá proteger a tu familia en caso de que algo te suceda.',
        image: images['/src/assets/images/grupo-de-edad.png']
    },
    {
        id: 6,
        text: 'Revisar y ajustar tu presupuesto regularmente te ayudará a mantenerte en el camino hacia tus objetivos financieros.',
        image: images['/src/assets/images/organizacion.png']
    }
]);

    const randomIndex = Math.floor(Math.random() * tips.value.length);
    const selectedTip = tips.value[randomIndex];
</script>

<template>
    <div class="tip">
        <img :src="selectedTip.image" />

        <div class="tip-text">
            <h4>¿Sabías que...?</h4>
            <p>{{ selectedTip.text }}</p>
        </div>
    </div>
</template>

<style scoped>
.tip {
    width: 80%;
    max-height: 180px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
    background-color: rgba(236, 240, 241, 0.4   );
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin: 30px 10px;
}
img {
    width: 100px;
    height: 100px;
}
.tip-text {
    max-width: 600px;
    margin-left: 20px;
}
</style>