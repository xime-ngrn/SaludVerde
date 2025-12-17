<script>

</script>

<template>
    <div class="menu-container">
        <h2>Bienvenido</h2>

        <div class="router">
            <router-link to="/home" class="menu-option">Inicio</router-link>
            <router-link to="/registro-contable" class="menu-option">Registro Contable</router-link>
            <router-link to="/reportes" class="menu-option">Reportes</router-link>
            <router-link to="/" class="menu-option">Meta de Ahorro</router-link>
        </div>
    </div>
</template>

<style scoped>
.menu-container {
    display: flex;
    width: 30%;
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
}
.menu-option::before {
    content: "";
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
    height: 2px;
    z-index: 0;
}
.menu-option::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: 0;
    width: 0%;
    height: 2px;
    color: var(--color-2);
    background: var(--color-1);
    transition: width 0.3s ease;
    z-index: 1;
}

.menu-option:hover::after {
    width: 100%;
}

h2 {
    color: #34495e;
}
</style>