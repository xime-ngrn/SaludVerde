<script setup>
import Menu from '@/components/MenuBar.vue';
import Footer from '@/components/Footer.vue';
import '@/assets/styles/base.css';
</script>

<template>
    <Menu />

    <div class="home-container">
        <section class="hero">
            <h2>Aviso de Privacidad</h2>
            <div class="hero-card">
                <div class="hero-left">
                    <h3>Tu privacidad es importante para nosotros</h3>
                    <div class="intro">
                        <div class="intro-text">
                            <p>
                                En Salud Verde estamos comprometidos con la protección de tus datos personales y con el respeto a tu privacidad. Este Aviso de Privacidad explica cómo recolectamos, usamos y protegemos tu información al hacer uso de nuestros servicios en línea relacionados con la educación y salud financiera.
                            </p>
                        </div>
                        <div class="intro-image">
                            <img src="@/assets/images/candado.gif" class="hero-family" alt="Aviso Privacidad" />
                        </div>
                    </div>
                    
                    <div class="privacy-section">
                        <section>
                            <h4>1. Responsable de la información</h4>
                            <p>Salud Verde, creado en las instalaciones de la Escuela Superior de Cómputo (ESCOM) del Instituto Politécnico Nacional (IPN), es responsable del tratamiento de tus datos personales y de su uso para fines académicos y de servicios.</p>
                        </section>
                        <section>
                            <h4>2. Datos que recolectamos</h4>
                            <p>Dentro de la página web se solicitan datos personales, tales como:</p>
                            <ul>
                                <li>Nombre completo</li>
                                <li>Edad</li>
                                <li>Correo electrónico</li>
                                <li>Vocación</li>
                                <li>Género</li>
                                <li>Contraseña</li>
                            </ul>
                            <p>Con el fin de brindarte una experiencia personalizada y mejorar la calidad de nuestros servicios.</p>
                        </section>
                        <section>
                            <h4>3. Finalidades del uso de datos</h4>
                            <p>Tus datos personales serán utilizados dentro de la aplicación para:</p>
                            <ul>
                                <li>Brindarte acceso a los servicios y funcionalidades de la plataforma.</li>
                                <li>Mejorar y personalizar tu experiencia en la plataforma.</li>
                                <li>Enviar notificaciones relacionadas con tu cuenta y actividades en la plataforma.</li>
                            </ul>
                            <p>No compartimos tus datos personales con terceros sin tu consentimiento explícito.</p>
                        </section>
                        <section>
                            <h4>4. Protección de tu información</h4>
                            <p>Implementamos medidas de seguridad administrativas, técnicas y físicas para proteger tu información contra pérdida, mal uso o acceso no autorizado.</p>
                        </section>
                        <section>
                            <h4>5. Transferencia de datos</h4>
                            <p>No compartiremos tus datos personales con terceros sin tu consentimiento, salvo en los casos que lo permita la ley.</p>
                        </section>
                        <section>
                            <h4>6. Derechos ARCO</h4>
                            <p>Tienes derecho a acceder, rectificar, cancelar u oponerte al uso de tus datos personales. Para ello, es necesario ponerte en contacto con el equipo de Salud Verde y realizar los cambios pertinentes.</p>
                        </section>
                        <section>
                            <h4>7. Cambios al Aviso de Privacidad</h4>
                            <p>Este Aviso de Privacidad puede actualizarse en cualquier momento. Te notificaremos cualquier cambio en esta misma página y en nuestras redes sociales.</p>
                        </section>
                        <section>
                            <h4>8. Contacto</h4>
                            <p>
                                Si tienes alguna pregunta o inquietud sobre este Aviso de Privacidad, por favor contáctanos a través de nuestro correo electrónico:
                                <a href="mailto:saludverde@salud-verde.com.mx" class="correo">saludverde@salud-verde.com.mx</a>
                            </p>
                        </section>
                    </div>
                </div>
            </div>
        </section>
    </div>

    <Footer />
</template>

<style scoped>
.home-container {
    padding: 2rem;
    background: #f8fafc;
    min-height: 100vh;
    box-sizing: border-box;
}
.hero {
    text-align: center;
    margin-bottom: 2rem;
}
.hero-card {
    max-width: 1000px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content: center;
    align-items: flex-start;
    text-align: left;
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 4px 24px rgba(44, 62, 80, 0.10);
    box-sizing: border-box;
    width: 100%;
    padding: 2rem 1.2rem 1.5rem 1.2rem;
}
.hero-left {
    flex: 1 1 300px;
    max-width: 950px;
    text-align: left;
    border-radius: 16px;
}
.intro {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    align-items: center;
    margin-bottom: 2rem;
}
.intro-text {
    flex: 1 1 250px;
    min-width: 220px;
}
.intro-image {
    flex: 1 1 200px;
    min-width: 180px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.hero-family {
    width: 100%;
    max-width: 220px;
    height: auto;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(44, 62, 80, 0.10);
}
.privacy-section {
    margin-top: 2rem;
}
.privacy-section section {
    margin-bottom: 2rem;
}
.privacy-section ul {
    margin-left: 45px;
    margin-bottom: 1rem;
}
.privacy-section li {
    font-size: 1.1rem;
    color: #34495e;
    line-height: 1.6;
}
p {
    padding: 0 0 0 20px;
}
.correo {
    font-weight: bold;
    text-decoration: none;
    color: #2980b9;
    border-bottom: 2px solid #2980b9;
    padding-bottom: 2px;
    font-size: 1.1rem;
    margin-left: 4px;
    transition: color 0.2s;
}
.correo:hover {
    color: var(--color-1);
    border-bottom-color: var(--color-2);
}
@media (max-width: 700px) {
    .hero-card, .intro {
        flex-direction: column;
        gap: 1rem;
    }
    .hero-left {
        padding: 1rem;
    }
    .hero-title {
        font-size: 2rem;
    }
}
</style>