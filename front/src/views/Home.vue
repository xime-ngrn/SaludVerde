<script setup>
import Menu from '@/components/MenuBar2.vue';
import Options from '@/components/OptionsBar.vue';

</script>

<template>
    <Menu />
    
    <div class="home-container">
        <Options />

        <div class="home">
            <p>Bienvenido a SaludVerde</p>
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
    text-align: center;
    margin-top: 2rem;
    font-size: 1.5rem;
    color: #334155;
}


</style>