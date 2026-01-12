<script setup>
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { setAuthCookies } from '@/utils/cookies';

const router = useRouter();

const generalError = ref('');

function regresar() {
    router.push('/salud-verde');
}

const username = ref('')
const password = ref('')
const loading = ref(false)

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

const iniciar = async () => {
  loading.value = true
  generalError.value = ''
  
  try {
    const response = await axios.post('api/login', {
        username: username.value,
        password: password.value
    })

    setAuthCookies(response.data.user.username, response.data.user.nombres)

    router.push('/home');
  } catch (error) {
    console.log("--- ERROR COMPLETO ---");
    console.log("Status:", error.response?.status); // Ver si es 404, 500, etc.
    console.log("Data:", error.response?.data);     // Ver el mensaje que envió Flask
    console.log("Config:", error.config);           // Ver a qué URL intentó ir
    generalError.value = error.response?.data?.message || 'Error de conexión';
  } finally {
    loading.value = false
  }
}
</script>

<template>
    <div class="container">
        <div class="signin-container">
            <h2>Inicio de sesión</h2>
            <p class="subtitle">Bienvenido de vuelta, ingresa tus datos para iniciar sesión.</p>

            <div class="form-section">
                <form class="form" @submit.prevent="iniciar" autocomplete="off" >
                    <div class="grid-form">
                        <div class="form-group">
                            <label for="username">Nombre de usuario</label>
                            <input
                                type="text"
                                id="username"
                                class="form-control"
                                v-model="username"
                                autocomplete="username"
                                required
                            />
                        </div>
                        <div class="form-group">
                            <label for="password">Contraseña</label>
                            <input
                                type="password"
                                id="password"
                                class="form-control"
                                v-model="password"
                                autocomplete="current-password"
                                required
                            />
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
