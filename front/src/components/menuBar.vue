<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import Cookies from 'js-cookie'
import { isAuthenticated, getAuthToken, clearAuthCookies } from '@/utils/cookies'

const router = useRouter()
const route = useRoute()

const mobileMenuOpen = ref(false)
const profileMenuOpen = ref(false)

const cookies = ref(false)
const nombre = ref('')

onMounted(() => {
  cookies.value = isAuthenticated()
  nombre.value = getAuthToken() || ''
})

function toggleProfileMenu() {
  profileMenuOpen.value = !profileMenuOpen.value
}

function isActive(path) {
  return route.path === path
}

function inicio(){
    router.push('/')
}
function iniciarSesion(){
    router.push('/login')
}
function registrarse(){
    router.push('registro')
}
function verUsuario(){
    router.push('/usuario')
}

function cerrarSesion(){
    clearAuthCookies()
    cookies.value = false
    router.push('/')
}

</script>


<template>
    <header class="menu-bar">
        <div class="logo-container">
            <img src="@/assets/images/logo.png" alt="Logo" class="logo" @click="inicio" />
            <button class="mobile-menu-btn" @click="mobileMenuOpen = !mobileMenuOpen">
                <span :class="{ open: mobileMenuOpen }">&#9776;</span>
            </button>
        </div>
        <nav class="menu-container" :class="{ open: mobileMenuOpen }">
            <ul>
                <li>
                    <router-link
                        to="/finanzas"
                        class="menu"
                        :class="{ active: isActive('/finanzas') }"
                        @click="mobileMenuOpen = false"
                    >
                        <img src="@/assets/images/bolsa-de-dinero1.png" class="nav-icon" />
                        Tips de finanzas personales
                    </router-link>
                </li>
                <li>
                    <router-link
                        to="/blog"
                        class="menu"
                        :class="{ active: isActive('/blog') }"
                        @click="mobileMenuOpen = false"
                    >
                        <img src="@/assets/images/blog.png" class="nav-icon" />
                        Blog
                    </router-link>
                </li>
                <li>
                    <router-link
                        to="/inversiones"
                        class="menu"
                        :class="{ active: isActive('/inversiones') }"
                        @click="mobileMenuOpen = false"
                    >
                        <img src="@/assets/images/money-up.png" class="nav-icon" />
                        Aprende de inversiones
                    </router-link>
                </li>
                <li>
                    <router-link
                        to="/nosotros"
                        class="menu"
                        :class="{ active: isActive('/nosotros') }"
                        @click="mobileMenuOpen = false"
                    >
                        <img src="@/assets/images/equipo.png" class="nav-icon" />
                        Sobre nosotros
                    </router-link>
                </li>
            </ul>
        </nav>


        <div class="inicio" :class="{ open: mobileMenuOpen }" v-if="!cookies">
            <button class="btn-primary" @click="iniciarSesion">Iniciar Sesión</button>
            <button class="btn-secondary" @click="registrarse">Regístrate</button>
        </div>

        <div class="profile-wrapper" v-if="cookies">
            <div class="profile" @click="toggleProfileMenu">
                <img src="@/assets/images/avatar.png" alt="Mi Perfil" class="avatar-profile" />
                <p>{{ nombre }}</p>
            </div>
            
            <div v-if="profileMenuOpen" class="profile-dropdown">
                <button @click="verUsuario" class="btn-primary">
                    Ver Perfil
                </button>
                <button @click="cerrarSesion" class="btn-cancel">
                    Cerrar Sesión
                </button>
            </div>
        </div>
    </header>
</template>

<style scoped>
.menu-bar {
    background-color: var(--color-1);
    padding: 1rem 2.5rem;
    width: 100%;
    max-height: 120px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
}

.logo-container {
    display: flex;
    align-items: center;
    position: relative;
}

.logo {
    width: 90px;
    height: 90px;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.3s, background 0.3s;
    border-radius: 16px;
}

.logo:hover, .logo:focus {
    transform: scale(1.12) rotate(-2deg);
    background: rgba(79, 209, 196, 0.18);
    box-shadow: 0 4px 16px rgba(79,209,196,0.18);
    outline: none;
}

.mobile-menu-btn {
    display: none;
    background: none;
    border: none;
    font-size: 2rem;
    margin-left: 1rem;
    cursor: pointer;
    color: #fff;
}

.mobile-menu-btn span.open {
    color: var(--color-2);
}

.nav-icon {
    width: 28px;
    height: 28px;
    filter: drop-shadow(0 1px 2px rgba(0,0,0,0.10));
}

.menu-container {
    flex-grow: 1;
    margin-left: 2.5rem;
    transition: max-height 0.3s, opacity 0.3s;
}

.menu-container ul {
    list-style: none;
    display: flex;
    justify-content: center;
    gap: 2.5rem;
    align-items: center;
    margin: 0;
    padding: 0;
}

.menu-container li {
    margin: 0;
    padding: 0;
    max-width: 180px;
}

.menu-container a,
.menu-container .menu,
.menu-container .router-link-active {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    font-size: 1.08rem;
    font-weight: 600;
    color: #fff;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 12px;
    transition: background 0.2s, color 0.2s;
}

.menu-container .active,
.menu-container .router-link-exact-active {
    background: var(--color-2, #4fd1c4);
    color: #222;
}

.inicio {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.profile {
    width: 200px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    justify-content: flex-end;
    text-align: center;
    margin-left: 60px;
}

.avatar-profile {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    border: 2px solid var(--color-2, #4fd1c4);
    box-shadow: 0 2px 8px rgba(0,0,0,0.10);
    object-fit: cover;
    background: #fff;
}

.profile p {
    margin: 0;
    padding: 0;
    font-size: 1.08rem;
    font-weight: 600;
    color: #fff;
    white-space: nowrap;
}

.profile-dropdown {
    position: absolute;
    top: 70%;
    right: -5%;
    transform: translateX(-50%);
    width: 200px;
    margin-top: 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-radius: 5px;
    background-color: rgba(255, 255, 255, 0.7);
    padding: 10px 0;
}

@media (max-width: 900px) {
    .menu-bar {
        flex-direction: column;
        align-items: stretch;
        padding: 1rem;
        min-height: unset;
    }
    .logo-container {
        justify-content: space-between;
    }
    .mobile-menu-btn {
        display: block;
    }
    .menu-container,
    .inicio {
        max-height: 0;
        opacity: 0;
        overflow: hidden;
        transition: max-height 0.3s, opacity 0.3s;
    }
    .menu-container.open,
    .inicio.open {
        max-height: 500px;
        opacity: 1;
    }
    .menu-container ul {
        flex-direction: column;
        gap: 1.2rem;
    }
    .inicio {
        justify-content: flex-end;
        margin-top: 1rem;
    }
    .logo {
        margin-bottom: 0.5rem;
    }
}
</style>
