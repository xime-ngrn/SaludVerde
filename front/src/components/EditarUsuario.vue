<script setup>
import { reactive, ref } from 'vue';

const form = reactive ({
    name: 'Juan',
    lastname: 'Pérez',
    age: 20,
    vocacion: 'Estudiante',
    gender: 'Hombre',
    username: 'Juan23',
    email: 'juan.perez@example.com',
    password: ''
});
const errors = ref({});

const emit = defineEmits(['close']);

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

const submitEdit = () => {
    // Aquí puedes añadir validación antes de emitir
    if(!validateForm()){
        emit('error')
        return
    }

    console.log("Usuario actualizado: ", form.value)
    emit('close');
};

function regresar() {
    emit('close');
}

</script>

<template>
    <div class="modal-overlay" @click.self="emit('close')">
        <div class="modal-content">
            <h3>Modificar Información</h3>
            
            <div class="form-section">
                <form class="form" @submit.prevent="submitEdit" autocomplete="off">
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
                    </div>

                    <div class="buttons">
                        <button class="btn-cancel" @click="regresar" type="button">Cancelar</button>
                        <button class="btn-primary" type="submit" @click="submitEdit">Modificar Información</button>
                    </div>
                </form>

            </div>
        </div>
    </div>
</template>

<style scoped>
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    background: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    width: 90%;
    max-width: 450px;
    transition: transform 0.3s ease-out;
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
    max-width: 300px;
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
    font-size: 0.65rem;
    margin: 4px;
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

.buttons {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-top: 25px;
}
</style>