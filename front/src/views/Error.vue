<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

function logout() {
    router.push('/');
}

function goBack() {
    router.back();
}
</script>

<template>
    <div class="error-bg">
        <div class="error-card" tabindex="0" aria-label="Error message">
            <div class="error-icon">
                <img src="../assets/images/error.png" alt="Error" />
            </div>
            <h1> Se ha producido un error</h1>
            <p class="error-message">La página a la que intenta conectarse no existe o esta fuera de servicio.</p>
            <div class="error-actions">
                <button type="button" class="btn-error" @click.prevent="goBack">Regresar</button>
                <button type="button" class="btn-primary" @click.prevent="logout">Cerrar Sesión</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
.error-bg {
    min-height: 100vh;
    background: linear-gradient(135deg, #f8fafc 0%, #e0e7ef 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
}

.error-card {
    background: #fff;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(60, 72, 88, 0.18);
    max-width: 420px;
    width: 100%;
    padding: 40px 32px 32px 32px;
    display: flex;
    flex-direction: column;
    align-items: center;
    animation: fadeInUp 0.7s cubic-bezier(.39,.575,.565,1.000);
    outline: none;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(40px);}
    to { opacity: 1; transform: translateY(0);}
}

.error-icon img {
    width: 64px;
    height: 64px;
    margin-bottom: 18px;
    filter: drop-shadow(0 2px 8px rgba(0,0,0,0.08));
}

h1 {
    font-size: 1.7rem;
    color: #e53e3e;
    margin-bottom: 12px;
    text-align: center;
}

.error-message {
    color: #374151;
    font-size: 1.1rem;
    margin-bottom: 10px;
    text-align: center;
    margin: 25px;
}

.error-option {
    color: #6b7280;
    font-size: 1rem;
    margin-bottom: 22px;
    text-align: center;
}

.error-actions {
    display: flex;
    gap: 12px;
    margin-bottom: 24px;
    width: 100%;
    justify-content: space-around;
}

.error-btn {
    border: none;
    border-radius: 8px;
    padding: 10px 22px;
    font-size: 1rem;
    cursor: pointer;
    font-weight: 600;
    transition: 
    border-color 0.35s ease,
    background-color 0.35s ease,
    box-shadow 0.35s ease,
    transform 0.2s ease;
}
.error-btn:hover {
    background: #f3f4f6;
}

@media (max-width: 500px) {
    .error-card {
        padding: 24px 8px 16px 8px;
        max-width: 98vw;
    }
    .error-icon img {
        width: 48px;
        height: 48px;
    }
}
</style>