<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const mobileMenuOpen = ref(false);
const profileMenuOpen = ref(false);

const nombre = computed(() => {
    return 'Usuario';
});

function isActive(path) {
    const currentRoute = router.currentRoute.value;
    return currentRoute.path === path;
}

// 2. Lógica para abrir/cerrar el menú del perfil
function toggleProfileMenu() {
    profileMenuOpen.value = !profileMenuOpen.value;
}

// 4. Funciones de navegación
function verUsuario() {
    profileMenuOpen.value = false;
    router.push('/usuario');
}

function cerrarSesion() {
    profileMenuOpen.value = false;
    // Lógica para cerrar la sesión (limpiar tokens, store, etc.)
    // alert('Sesión cerrada'); 
    router.push('/login'); // Redirige a la página de inicio de sesión
}

// Función `nosotros` (asumiendo que faltaba)
function nosotros() {
    // Si necesitas hacer algo antes de redirigir a /nosotros
    router.push('/nosotros');
}

</script>

<template>
    <header class="menu-bar">
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
                        Aprende de Inversiones
                    </router-link>
                </li>
                <li>
                    <a
                        class="menu"
                        :class="{ active: isActive('/nosotros') }"
                        @click="nosotros(); mobileMenuOpen = false"
                    >
                        <img src="@/assets/images/equipo.png" class="nav-icon" />
                        Sobre Nosotros
                    </a>
                </li>
            </ul>
        </nav>
        
        <div class="profile-wrapper">
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
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    position: relative;
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
    display: block;
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
button {
    max-width: 75%;
    margin: 5px 0;
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
