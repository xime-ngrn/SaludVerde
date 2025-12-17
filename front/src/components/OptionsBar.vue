<script>

</script>

<template>
    <div class="menu-container">
        <p>Opciones</p>

        <div class="router">
            <router-link to="/" class="menu-option">Inicio</router-link>
            <router-link to="/" class="menu-option">Registro Contable</router-link>
            <router-link to="/" class="menu-option">Reportes</router-link>
            <router-link to="/" class="menu-option">Meta de Ahorro</router-link>
        </div>
    </div>
</template>

<style scoped>
.menu-container {
    display: flex;
    flex-direction: column;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.menu-container p {
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 15px;
    color: #2c3e50;
}
.router {
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.menu-option {
    text-decoration: none;
    color: #3498db;
    font-size: 1rem;
    transition: color 0.2s;
}
.menu-option:hover {
    color: #2980b9;
    position: relative;
}
.menu-option:hover::after {
    content: "";
    display: block;
    position: absolute;
    left: 0;
    bottom: -2px;
    width: 100%;
    height: 2px;
    background: #2980b9;
    border-radius: 1px;
}
</style>