<script setup>
import { ref, onMounted } from 'vue';
import Menu from '@/components/MenuBar.vue';
import Options from '@/components/OptionsBar.vue';
import EditProfileModal from '@/components/EditarUsuario.vue'; 
import { getAuthToken } from '@/utils/cookies';

const userData = ref({});
const currentUser = getAuthToken();
const error = ref('');

const fetchUserData = async () => {
    error.value = '';

    if (!currentUser) return;
    try {
        const response = await fetch(`http://127.0.0.1:5000/usuario?username=${currentUser}`);
        const data = await response.json();
        userData.value = data;
        error.value = null;
    } catch (error) {
        error.value = "Error al cargar los datos del usuario.";
    }
};

const handleUpdate = async (updatedForm) => {
    error.value = '';

    try {
        const dataToSend = { 
            ...updatedForm, 
            username: userData.value.username 
        };

        const response = await fetch('http://127.0.0.1:5000/update_usuario', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dataToSend)
        });

        if (response.ok) {
            alert("Cambios guardados");
            isModalOpen.value = false;
            fetchUserData();
        }
    } catch (error) {
        error.value = "Error al guardar los cambios.";
        alert("Error al guardar los cambios");
        console.error("Error en la petición:", error);
    }
};

onMounted(fetchUserData);

const isModalOpen = ref(false);
const openModal = () => isModalOpen.value = true;
const closeModal = () => isModalOpen.value = false;
</script>

<template>
    <Menu />
    <div class="home-container">
        <Options />

        <div class="home">
            <h3>Información del Usuario</h3>

            <button @click="openModal" class="btn-primary">Modificar Información</button>
            
            <div class="container">
                <span v-if="error" class="error">{{ error }}</span>
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
    width: 100%;
    display: flex;
    flex-direction: column;
    padding: 20px;
    align-items: flex-start;
    font-size: 1rem;
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
.error {
    color: #e74c3c;
    font-size: 0.85rem;
    padding: 10px;
    border-radius: 4px;
    margin-bottom: 15px;
    font-size: 0.9rem;
    text-align: center;
    width: 100%;
}

.btn-primary {
    align-self: flex-end;
    margin-right: 100px;
}
</style>