<script setup>
import Menu from '@/components/MenuBar2.vue';
import Options from '@/components/OptionsBar.vue';
import Tip from '@/components/Tip.vue';

</script>

<template>
    <Menu />
    
    <div class="home-container">
        <Options />

        <div class="home">
            <Tip />
            
        </div>
    </div>
</template>

<style scoped>
.home-container {
    display: flex;
    flex-direction: row;
    background: #f8fafc;
    min-height: 100vh;
    height: 100vh;
    max-height: 100vh;
    overflow: hidden;
}
.home {
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    font-size: 1.5rem;
    color: #334155;
    overflow: hidden;
    padding: 40px;
}
</style>