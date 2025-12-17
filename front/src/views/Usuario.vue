<script setup>
import { ref, reactive } from 'vue';
import Menu from '@/components/MenuBar2.vue';
import Options from '@/components/OptionsBar.vue';
// 💡 Necesitas crear este componente Modal
import EditProfileModal from '@/components/EditarUsuario.vue'; 

// Datos del usuario (simulados)
const userData = reactive({
    nombre: 'Juan',
    apellido: 'Pérez',
    username: 'Juan23',
    email: 'juan.perez@example.com',
    fechaRegistro: '15 de Marzo, 2023',
    vocacion: 'Estudiante',
    edad: 20,
});

// 1. Estado reactivo para controlar el modal
const isModalOpen = ref(false);

// 2. Lógica para abrir/cerrar el modal
const openModal = () => {
    isModalOpen.value = true;
};

const closeModal = () => {
    isModalOpen.value = false;
};
</script>

<template>
    <Menu />
    
    <div class="home-container">
        <Options />

        <div class="home">
            <h3>Información del Usuario</h3>

            <button @click="openModal" class="btn-primary">Modificar Información</button>
            
            <div class="container">
                <p><strong>Nombre:</strong> {{ userData.nombre }} {{ userData.apellido }}</p>
                <p><strong>Nombre de Usuario:</strong> {{ userData.username }}</p>
                <p><strong>Email:</strong> {{ userData.email }}</p>
                <p><strong>Fecha de Registro:</strong> {{ userData.fechaRegistro }}</p>
                <p><strong>Vocación:</strong> {{ userData.vocacion }}</p>
                <p><strong>Edad:</strong> {{ userData.edad }} años</p>
            </div>
        </div>
    </div>

    <EditProfileModal 
        v-if="isModalOpen" 
        :initial-data="userData"
        @close="closeModal" 
        @update-profile="handleUpdate"
    />
</template>

<style scoped>
.home-container {
    display: flex;
    flex-direction: row;
    background: #f8fafc;
    min-height: 100vh;
    height: 100vh;
    max-height: 100vh;
    overflow: hidden;
}
.home {
    /* Ajustes para un diseño vertical más limpio en la sección de info */
    width: 100%;
    /* Removido height: 100vh; y overflow: hidden; para permitir scroll si es necesario */
    display: flex;
    flex-direction: column; /* Apila elementos verticalmente */
    padding: 20px;
    align-items: flex-start; /* Alinea los elementos a la izquierda (inicio) */
    font-size: 1rem; /* Ajuste para mejor lectura */
    color: #334155;
}
.container {
    width: 80%;
    margin: 40px auto;
    padding: 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background: rgba(255, 255, 255, 0.7);
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}

h3 {
    align-self: center;
}

.btn-primary {
    align-self: flex-end;
    margin-right: 100px;
}
</style>