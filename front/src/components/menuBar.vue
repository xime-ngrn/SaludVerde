<script setup>
import router from '@/router';

function inicio() {
    router.push('/');
}
function iniciarSesion() {
    router.push('/login');
}

function registrarse() {
    router.push('/registro');
}

function nosotros() {
    router.push('/nosotros');
}
</script>

<template>
    <header class="menu-bar">
        <div class="logo-container">
            <img src="@/assets/images/logo.png" alt="Logo" class="logo" @click="inicio" />   
        </div>
        <nav class="menu-container">
            <ul>
                <li>
                    <router-link to="/finanzas" class="menu">
                        <img src="@/assets/images/bolsa-de-dinero1.png" class="nav-icon" />
                        Aprende de finanzas personales
                    </router-link>
                </li>

                <li>
                    <router-link to="/blog" class="menu">
                        <img src="@/assets/images/blog.png" class="nav-icon" />
                        Blog
                    </router-link>
                </li>

                <li>
                    <router-link to="/inversiones" class="menu">
                        <img src="@/assets/images/money-up.png" class="nav-icon" />
                        Aprende de Inversiones
                    </router-link>
                </li>

                <li>
                    <a class="menu" @click="nosotros">
                        <img src="@/assets/images/equipo.png" class="nav-icon" />
                        Sobre Nosotros
                    </a>
                </li>
            </ul>
        </nav>
        <div class="inicio">
            <button class="btn-primary" @click="iniciarSesion">Iniciar Sesión</button>
            <button class="btn-secondary" @click="registrarse">Regístrate</button>
        </div>

    </header>
</template>

<style scoped>
.menu-bar {
    background-color: var(--color-1);
    padding: 1rem 1rem;
    width: 100%;
    max-height: 120px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: nowrap;
}

.logo-container {
    display: flex;
    align-items: center;
}

.logo {
    width: 100px;
    height: 100px;
    cursor: pointer;
    transition:
        border-color 0.35s ease,
        background-color 0.35s ease,
        box-shadow 0.35s ease,
        transform 0.2s ease;
}

.logo:focus {
    outline: none;
    box-shadow: 0 0 0 3px #4fd1c4b1;
}

.logo:hover {
    transform: scale(1.15);
    background: rgba(79, 209, 196, 0.25);
    backdrop-filter: blur(4px);
    border-radius: 16px;
}

.nav-icon {
    width: 30px;
    height: 30px;
}

.menu-container {
    flex-grow: 1;
    margin-left: 2rem;
}

.menu-container ul {
    list-style: none;
    display: flex;
    justify-content: space-around;
    gap: 2rem;
    align-items: center;
}
.menu-container li {
    margin: 0;
    padding: 0;
    max-width: 150px;
}
.menu-container a,
.menu-container .menu {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 18px;
    font-weight: bold;
    color: white;
    text-decoration: none;
}

.inicio {
    display: flex;
    align-items: center;
}
.inicio button {
    margin-left: 1rem;
}
</style>
