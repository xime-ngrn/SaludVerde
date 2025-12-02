<script setup>
import router from '@/router';

function avisoPrivacidad() {
    router.push('/aviso-privacidad');
}
</script>

<template>
    <div class="container">
        <div class="footer">
            <p class="small">© Todos los derechos reservados a los creadores del proyecto.</p>
            <a href="#" class="aviso-privacidad" @click="avisoPrivacidad">
                <div class="opcion">
                    <img src="@/assets/images/aviso-privacidad.png" alt="Logo SaludVerde" class="logo" />
                    Aviso de Privacidad
                </div>
            </a>
        </div>

        <div class="social">
            <p class="small">Síguenos en nuestras Redes Sociales</p>
            <div class="icons">
                <img src="@/assets/images/tiktok.png" />
                <img src="@/assets/images/instagram.png" />
                <img src="@/assets/images/facebook.png" />
            </div>
        </div>
    </div>
</template>

<style scoped>
.container {
    width: 100%;
    height: 100%;
    padding: 40px 20px;
    background-color: var(--color-2);
    font-size: var(--text-small);
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
a {
    padding: 0 0 0 20px;
}
</style>