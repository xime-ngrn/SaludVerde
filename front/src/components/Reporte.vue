<script setup>
import { ref } from 'vue';

const props =defineProps({
    title: {
        type: String,
        required: true
    },
    gastos: {
        type: Number,
        required: true
    },
    ingresos: {
        type: Number,
        required: true
    }
});
</script>

<template>
    <div class="reporte">
        <img src="@/assets/images/reporte.png" alt="Reporte Icon" class="reporte-icon" />
        <h4>{{ props.title }}</h4>
    </div>

</template>

<style scoped>
.reporte {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 16px;
    margin: 16px;
    background-color: #ffffff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 200px;
}
img.reporte-icon {
    width: 48px;
    height: 48px;
    margin-bottom: 12px;
}
</style>