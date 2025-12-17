<script setup>
import { ref, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();
const mobileMenuOpen = ref(false);

const nombre = computed(() => {
    // Aquí podrías obtener el nombre del usuario desde un store o API
    return 'Usuario';
});

function isActive(path) {
    return route.path === path;
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
        <div class="profile" :class="{ open: mobileMenuOpen }">
            <img src="@/assets/images/avatar.png" alt="Mi Perfil" class="avatar-profile" />
            <p>{{ nombre }}</p>
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

.profile {
    display: flex;
    flex-direction: column;
    align-self: center;
    gap: 1rem;
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
