<script setup>
import { ref, reactive } from 'vue';
import Menu from '@/components/MenuBar2.vue';
import Options from '@/components/OptionsBar.vue';
// 💡 Necesitas crear este componente Modal
import EditProfileModal from '@/components/EditarUsuario.vue'; 

// Datos del usuario (simulados)
const userData = reactive({
    nombre: 'Juan Pérez',
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

// Lógica para actualizar los datos desde el modal (ejemplo)
const handleUpdate = (newUserData) => {
    // Aquí actualizas tu store o realizas la petición a la API
    // Por ahora, solo actualizamos el estado local
    Object.assign(userData, newUserData);
    closeModal();
};

</script>

<template>
    <Menu />
    
    <div class="home-container">
        <Options />

        <div class="home">
            <h3>Información del Usuario</h3>

            <button @click="openModal" class="btn-primary">Modificar Información</button>
            
            <div class="info">
                <p><strong>Nombre:</strong> {{ userData.nombre }}</p>
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

h3 {
    align-self: center;
}

.btn-primary {
    align-self: flex-end;
}
</style>