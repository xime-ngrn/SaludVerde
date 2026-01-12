<script setup>
import { reactive, ref, onMounted } from 'vue';

const props = defineProps({
    initialData: Object
});

const errors = ref({});

const emit = defineEmits(['close', 'update-profile', 'error']);

const form = reactive({
    nombre: props.initialData.nombre || '',
    apellido: props.initialData.apellido || '',
    edad: props.initialData.edad || '',
    vocacion: props.initialData.vocacion || '',
    username: props.initialData.username || '',
    email: props.initialData.email || '',
});

function validateForm() {
    errors.value = {};
    if (!form.nombre) errors.value.name = 'Nombre requerido';
    if (!form.apellido) errors.value.lastname = 'Apellido requerido';
    if (!form.edad || form.edad <= 0) errors.value.age = 'Edad válida';
    if (!form.username) errors.value.username = 'Usuario requerido';
    if (!form.email) errors.value.email = 'Email requerido';
    if(!form.vocacion) errors.value.vocacion = 'Vocación requerida';
    return Object.keys(errors.value).length === 0;
}

const submitEdit = () => {
    if(!validateForm()){
        return;
    }
    emit('update-profile', { ...form });
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
                            <input type="text" id="name" class="form-control" v-model="form.nombre" />
                            <span v-if="errors.name" class="error">{{ errors.name }}</span>
                        </div>
                        <div class="form-group">
                            <label for="lastname">Apellido</label>
                            <input type="text" id="lastname" class="form-control" v-model="form.apellido" />
                            <span v-if="errors.lastname" class="error">{{ errors.lastname }}</span>
                        </div>
                        <div class="form-group">
                            <label for="age">Edad</label>
                            <input type="number" id="age" class="form-control" v-model="form.edad" min="1" />
                            <span v-if="errors.age" class="error">{{ errors.age }}</span>
                        </div>
                        <div class="form-group">
                            <label for="vocacion">Vocación</label>
                            <input type="text" id="vocacion" class="form-control" v-model="form.vocacion" />
                            <span v-if="errors.vocacion" class="error">{{ errors.vocacion }}</span>
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