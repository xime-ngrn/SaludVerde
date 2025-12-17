<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    title: String,
    content: String,
    date: String,
    link: String
});

function openLink() {
    if (props.link) {
        window.open(props.link, '_blank');
    }
}

function abrirModal() {
    
}

</script>

<template>
    <div class="card" @click="abrirModal">
        <div class="header">
            <img src="@/assets/images/tip.png" alt="Card Image" class="card-image"/>
            <h3 class="card-title">{{ props.title }}</h3>
        </div>
        <p class="card-content">{{ props.content }}</p>
        <button class="btn-primary" v-if="props.link" @click="openLink">Leer más</button>
        <p class="card-date">{{ props.date }}</p>
    </div>
</template>

<style scoped>
.card {
    background: radial-gradient(#ffffff 0%, var(--color-2) 100%);
    border-radius: 18px;
    padding: 28px 24px 20px 24px;
    box-shadow: 0 6px 24px rgba(60, 120, 60, 0.12);
    transition: transform 0.18s, box-shadow 0.18s, background 0.18s;
    border: 1px solid var(--color-1);
    max-width: 350px;
    margin: 18px auto;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    min-height: 340px;
}
.header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin-bottom: 18px;
}
.card-image {
    width: 72px;
    height: 72px;
    object-fit: cover;
    border-radius: 50%;
    margin-bottom: 12px;
    border: 2px solid var(--color-1);
    box-shadow: 0 2px 8px rgba(60, 120, 60, 0.08);
}
.card-title {
    font-size: 1.35rem;
    font-weight: 800;
    margin-bottom: 8px;
    text-align: center;
    letter-spacing: 0.5px;
}
.card-content {
    font-size: 1.08rem;
    color: #4e5d4e;
    line-height: 1.7;
    margin-bottom: 10px;
    padding: 15px;
    text-align: center;
    flex: 1;
}
.card-footer {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 12px;
    position: absolute;
    right: 18px;
    bottom: 20px;
}
.card-date {
    font-size: 0.92rem;
    color: var(--color-3);
    font-style: italic;
    letter-spacing: 0.2px;
    text-align: right;
    margin: 0;
}
.btn-primary {
    margin-bottom: 15px;
}
</style>