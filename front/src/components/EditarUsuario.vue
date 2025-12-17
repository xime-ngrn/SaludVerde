<script setup>
import { ref } from 'vue';

const props = defineProps({
    initialData: Object,
});

const emit = defineEmits(['close', 'update-profile']);

// Crea una copia reactiva de los datos para editar en el formulario
const editData = ref({ ...props.initialData });

const submitEdit = () => {
    // Aquí puedes añadir validación antes de emitir
    emit('update-profile', editData.value);
    // El 'close' se llama dentro de handleUpdate del componente padre
};

function regresar() {
    
}

</script>

<template>
    <div class="modal-overlay" @click.self="emit('close')">
        <div class="modal-content">
            <h3>Modificar Información</h3>
            
            <form @submit.prevent="submitEdit">
                <div>
                    <label for="nombre">Nombre</label>
                    <input id="nombre" v-model="editData.nombre" required />
                </div>
                <div>
                    <label for="email">Email</label>
                    <input id="email" type="email" v-model="editData.email" required />
                </div>
                <div>
                    <label for="vocacion">Vocación</label>
                    <input id="vocacion" type="text" />
                </div>
                <div>
                    <label for="edad">Edad</label>
                    <input id="edad" type="number" min="5" />
                </div>
                <div class="buttons">
                        <button class="btn-cancel" @click="regresar" type="button">Cancelar</button>
                        <button class="btn-primary" type="submit">Modificar</button>
                    </div>
            </form>
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

/* Estilos para el Contenido del Modal */
.modal-content {
    background: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    width: 90%;
    max-width: 450px;
    transition: transform 0.3s ease-out;
}

.modal-content h3 {
    margin-top: 0;
    color: #1e293b;
}

/* Estilos de formulario dentro del modal */
.modal-content label {
    display: block;
    margin-top: 10px;
    margin-bottom: 5px;
    font-weight: 500;
    color: #334155;
}

.modal-content input {
    width: 100%;
    padding: 10px;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    box-sizing: border-box;
}

.buttons {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-top: 25px;
}

h3 {
    align-self: center;
}
</style>