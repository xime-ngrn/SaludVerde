<script setup>
    
</script>

<template>
    <div class="menu-container">
        <h2>Bienvenido</h2>

        <div class="router">
            <router-link to="/home" class="menu-option">Inicio</router-link>
            <router-link to="/registro-contable" class="menu-option">Registro Contable</router-link>
            <router-link to="/reportes" class="menu-option">Reportes</router-link>
            <router-link to="/meta-ahorro" class="menu-option">Meta de Ahorro</router-link>
        </div>
    </div>
</template>

<style scoped>
/* ... Tus estilos base se mantienen igual ... */

.menu-container {

    display: flex;
    flex-direction: column;
    padding: 20px;
    background-color: var(--color-2);
    border-radius: 15px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.router {
    display: flex;
    flex-direction: column;
    gap: 40px;
    margin-top: 20px;
    margin-left: 15px;
}

.menu-option {
    position: relative;
    text-decoration: none;
    color: #34495e;
    font-size: 1rem;
    padding-bottom: 4px;
    transition: color 0.3s ease;
}

/* 💡 ESTADO ACTIVO: Esta es la clase que Vue Router activa por ti */
.menu-option.router-link-active {
    color: var(--color-1); /* Cambia el color del texto cuando está seleccionado */
    font-weight: bold;
}

/* 💡 LINEA SUBRAYADA ACTIVA: Reutilizamos tu efecto de ::after */
.menu-option.router-link-active::after {
    width: 100%; /* La línea se queda fija al 100% */
}

/* --- Efectos de línea (tus estilos originales mejorados) --- */
.menu-option::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: 0;
    width: 0%;
    height: 2px;
    background: var(--color-1);
    transition: width 0.3s ease;
}

.menu-option:hover::after {
    width: 100%;
}

h2 {
    color: #34495e;
}
</style>