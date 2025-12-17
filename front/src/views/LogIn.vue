<script setup>
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const form = reactive({
    username: '',
    password: ''
});
const errors = reactive({
    username: '',
    password: ''
});
const generalError = ref('');

function regresar() {
    router.push('/salud-verde');
}

function validar() {
    errors.username = '';
    errors.password = '';
    let valid = true;
    if (!form.username) {
        errors.username = 'El usuario es obligatorio.';
        valid = false;
    }
    if (!form.password) {
        errors.password = 'La contraseña es obligatoria.';
        valid = false;
    }
    return valid;
}

function iniciar() {
    generalError.value = '';
    if (!validar()) return;
    // Simulación de autenticación
    if (form.username === 'admin' && form.password === 'admin') {
        router.push('/home');
    } else {
        generalError.value = 'Usuario o contraseña incorrectos.';
    }
}
</script>

<template>
    <div class="container">
        <div class="signin-container">
            <h2>Inicio de sesión</h2>
            <p class="subtitle">Bienvenido de vuelta, ingresa tus datos para iniciar sesión.</p>
            <div class="form-section">
                <form class="form" @submit.prevent="iniciar" autocomplete="off">
                    <div class="grid-form">
                        <div class="form-group">
                            <label for="username">Nombre de usuario</label>
                            <input
                                type="text"
                                id="username"
                                class="form-control"
                                v-model="form.username"
                                autocomplete="username"
                                required
                            />
                            <span v-if="errors.username" class="error">{{ errors.username }}</span>
                        </div>
                        <div class="form-group">
                            <label for="password">Contraseña</label>
                            <input
                                type="password"
                                id="password"
                                class="form-control"
                                v-model="form.password"
                                autocomplete="current-password"
                                required
                            />
                            <span v-if="errors.password" class="error">{{ errors.password }}</span>
                        </div>
                    </div>
                    <span v-if="generalError" class="general-error">{{ generalError }}</span>
                    <div class="buttons">
                        <button class="btn-cancel" @click="regresar" type="button">Cancelar</button>
                        <button class="btn-primary" type="submit">Iniciar Sesión</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<style scoped>
.container {
    background-color: var(--color-2);
    width: 100vw;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.signin-container {
    max-width: 500px;
    margin: 40px auto;
    padding: 30px;
    background: rgba(255, 255, 255, 0.7);
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}

h2 {
    text-align: center;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    opacity: 0.9;
    margin-bottom: 20px;
}

.form-section {
    width: 100%;
}

.form {
    width: 100%;
}

.grid-form {
    display: grid;
    grid-template-columns: 1fr;
    gap: 18px 0;
}

.form-group {
    display: flex;
    flex-direction: column;
    position: relative;
}

label {
    font-weight: 600;
    margin-bottom: 6px;
}

.form-control {
    padding: 10px;
    border-radius: 6px;
    border: 1px solid #bbb;
    font-size: 1rem;
    background: #fff;
    color: #333;
}

.form-control:focus {
    border-color: #4ea5ff;
    outline: none;
    box-shadow: 0 0 6px rgba(78, 165, 255, 0.6);
}

.error {
    color: #e74c3c;
    font-size: 0.85rem;
    margin-top: 4px;
    position: absolute;
    bottom: -18px;
    left: 0;
}

.general-error {
    display: block;
    color: #e74c3c;
    text-align: center;
    margin: 10px 0;
    font-size: 0.95rem;
}

.buttons {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-top: 25px;
}

@media (max-width: 600px) {
    .signin-container {
        max-width: 95vw;
        padding: 18px;
    }
    .error {
        position: static;
        margin-bottom: 8px;
    }
}
</style>
