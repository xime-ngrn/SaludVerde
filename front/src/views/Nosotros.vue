<script setup>
import MenuBar from '@/components/menuBar.vue';
import Footer from '@/components/footer.vue';
import '@/assets/styles/base.css';
import router from '@/router';

</script>

<template>
    <MenuBar />

    <div class="home-container">
        <section class="hero">
            <h2>Sobre Nosotros</h2>
            <div class="hero-card">
                <div class="hero-left">
                    <h3>Conoce más sobre nuestro equipo y misión</h3>
                    <div class="intro">
                        <div class="intro-text">
                            <p class="card-text">
                                Somos un grupo dedicado a brindar educación financiera accesible para todos.
                                Nuestro objetivo es empoderar a las personas para que tomen decisiones financieras informadas y mejoren su bienestar económico.
                            </p>
                        </div>
                        <div class="intro-image">
                            <img src="@/assets/images/logo.png" class="hero-family" alt="Logo de Salud Verde" />
                        </div>
                    </div>

                    <div class="info-section">
                        <section>
                            <h4>Objetivo del Proyecto</h4>
                            <p>Desarrollo de una plataforma web interactiva y educativa que brinde a los jóvenes la posibilidad de adentrarse en el mundo de las finanzas personales para el fomento de hábitos financieros saludables, mejora de su capacidad de ahorro y la prevención del endeudamiento de alto riesgo.</p>
                        </section>
                        <section>
                            <h4>Misión</h4>
                            <p>Ser la plataforma web interactiva y accesible que empodera a los jóvenes para que adquieran las herramientas, el conocimiento y la confianza necesarios en el manejo de sus finanzas personales.</p>
                            <p>Para lograrlo, desarrollamos: </p>
                            <ul>
                                <li>Promover el acceso a la educación financiera de forma fácil y sencilla para todos.</li>
                                <li>Fomentar hábitos financieros saludables desde una edad temprana.</li>
                                <li>Mejorar significativamente su capacidad de ahorro.</li>
                                <li>Prevenir el endeudamiento de alto riesgo.</li>
                            </ul>
                        </section>
                        <section>
                            <h4>Visión</h4>
                            <p>Ser el referente líder a nivel nacional en educación financiera juvenil, reconocido por transformar positivamente la relación de los adolescentes con el dinero.</p>
                            <p>Para ello, se busca a futuro:</p>
                            <ul>
                                <li>Crear una generación de jóvenes financieramente inteligentes que tomen decisiones responsables y planifiquen su futuro con seguridad.</li>
                                <li>Adentrar a los jóvenes al mundo de las finanzas personales con ayuda de expertos en la materia que los acompañen.</li>
                                <li>Acercamiento con entidades financieras, los productos y servicios que cada una ofrece y probabilidades de crecimiento a futuro.</li>
                                <li>Ser el catalizador de un cambio cultural donde la salud financiera sea vista como una parte integral del bienestar personal.</li>
                                <li>Expandir nuestra plataforma para llegar a cada joven, adaptándonos a las últimas tecnologías y tendencias educativas.</li>
                            </ul>
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
}
.hero {
    text-align: center;
    margin-bottom: 2rem;
}
.hero-card {
    max-width: 900px;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: flex-start;
    gap: 2rem;
    margin-top: 2rem;
}
.hero-left {
    flex: 1 1 300px;
    max-width: 950px;
    text-align: left;
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 4px 24px rgba(44, 62, 80, 0.10);
    padding: 2rem;
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
.info-section {
    margin-top: 2rem;
}
.info-section section {
    margin-bottom: 2rem;
}
.info-section ul {
    margin-left: 45px;
    margin-bottom: 1rem;
}
.info-section li {
    font-size: 1.1rem;
    color: #34495e;
    line-height: 1.6;
}
p {
    padding: 0 0 0 20px;
}
</style>