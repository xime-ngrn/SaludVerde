<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const form = ref({
    name: '',
    lastname: '',
    age: '',
    vocacion: '',
    gender: '',
    username: '',
    email: '',
    password: ''
});

const errors = ref({});

function regresar() {
    router.push('/salud-verde');
}

function validateForm() {
    errors.value = {};
    if (!form.value.name) errors.value.name = 'Nombre requerido';
    if (!form.value.lastname) errors.value.lastname = 'Apellido requerido';
    if (!form.value.age || form.value.age <= 0) errors.value.age = 'Edad válida requerida';
    if (!form.value.vocacion) errors.value.vocacion = 'Vocación requerida';
    if (!form.value.gender) errors.value.gender = 'Selecciona género';
    if (!form.value.username) errors.value.username = 'Usuario requerido';
    if (!form.value.email || !/\S+@\S+\.\S+/.test(form.value.email)) errors.value.email = 'Correo válido requerido';
    if (!form.value.password || form.value.password.length < 6) errors.value.password = 'Mínimo 6 caracteres';
    return Object.keys(errors.value).length === 0;
}

function registrar() {
    if (!validateForm()) return;
    // Aquí iría la llamada a la API para registrar el usuario
    console.log('Usuario registrado', form.value);
    router.push('/home');
}
</script>

<template>
    <div class="container">
        <div class="register-container">
            <h2>Registro</h2>
            <p class="subtitle">Bienvenido, completa los siguientes datos.</p>

            <div class="form-section">
                <form class="form" @submit.prevent="registrar" autocomplete="off">
                    <div class="grid-form">
                        <div class="form-group">
                            <label for="name">Nombre</label>
                            <input type="text" id="name" class="form-control" v-model="form.name" />
                            <span v-if="errors.name" class="error">{{ errors.name }}</span>
                        </div>
                        <div class="form-group">
                            <label for="lastname">Apellido</label>
                            <input type="text" id="lastname" class="form-control" v-model="form.lastname" />
                            <span v-if="errors.lastname" class="error">{{ errors.lastname }}</span>
                        </div>
                        <div class="form-group">
                            <label for="age">Edad</label>
                            <input type="number" id="age" class="form-control" v-model="form.age" min="1" />
                            <span v-if="errors.age" class="error">{{ errors.age }}</span>
                        </div>
                        <div class="form-group">
                            <label for="vocacion">Vocación</label>
                            <input type="text" id="vocacion" class="form-control" v-model="form.vocacion" />
                            <span v-if="errors.vocacion" class="error">{{ errors.vocacion }}</span>
                        </div>
                        <div class="form-group">
                            <label for="gender">Género</label>
                            <select id="gender" v-model="form.gender" class="form-control">
                                <option value="">Selecciona</option>
                                <option value="male">Masculino</option>
                                <option value="female">Femenino</option>
                                <option value="other">Otro</option>
                            </select>
                            <span v-if="errors.gender" class="error">{{ errors.gender }}</span>
                        </div>
                        <div class="form-group">
                            <label for="username">Nombre de usuario</label>
                            <input type="text" id="username" class="form-control" v-model="form.username" />
                            <span v-if="errors.username" class="error">{{ errors.username }}</span>
                        </div>
                        <div class="form-group">
                            <label for="email">Correo electrónico</label>
                            <input type="email" id="email" class="form-control" v-model="form.email" />
                            <span v-if="errors.email" class="error">{{ errors.email }}</span>
                        </div>
                        <div class="form-group">
                            <label for="password">Contraseña</label>
                            <input type="password" id="password" class="form-control" v-model="form.password" />
                            <span v-if="errors.password" class="error">{{ errors.password }}</span>
                        </div>
                    </div>

                    <p class="notice">
                        Al registrarte, aceptas los Términos y Condiciones y nuestro
                        <RouterLink :to="{ path: '/aviso-privacidad' }" class="link" active-class="active-link">
                            Aviso de Privacidad
                        </RouterLink>.
                    </p>

                    <div class="buttons">
                        <button class="btn-cancel" @click="regresar" type="button">Cancelar</button>
                        <button class="btn-primary" type="submit">Registrarse</button>
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

.register-container {
    max-width: 900px;
    margin: 40px auto;
    padding: 30px;
    background: rgba(255, 255, 255, 0.7);
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}

h2 {
    text-align: center;
    margin-bottom: 10px;
    font-size: 1.8rem;
    font-weight: bold;
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
    grid-template-columns: 1fr 1fr;
    gap: 18px 24px;
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
    background: #ffffff;
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

.notice {
    margin-top: 15px;
    font-size: 0.7rem;
    opacity: 0.9;
    grid-column: 1 / -1;
}

.link {
    color: var(--color-1);
    font-weight: bold;
    font-size: 0.7rem;
    text-decoration: underline;
    transition: 0.3s;
}

.link:hover {
    opacity: 0.7;
}

.buttons {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-top: 25px;
}

.cancel:hover {
    background: #b3b3b3;
}

.primary {
    background: #4ea5ff;
    color: white;
}

.primary:hover {
    background: #1d8bfd;
}

/* Responsive for mobile */
@media (max-width: 600px) {
    .grid-form {
        grid-template-columns: 1fr;
    }

    .error {
        position: static;
        margin-bottom: 8px;
    }
}
</style>
