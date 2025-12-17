<script setup>
import { ref } from 'vue';
import Menu from '@/components/MenuBar.vue';
import Footer from '@/components/Footer.vue';
import Card from '@/components/Card.vue';
import '@/assets/styles/base.css';

const tips = ref([
    {
        title: 'Investiga antes de invertir',
        content: 'Infórmate sobre las opciones de inversión disponibles y comprende cómo funcionan. Lee libros, toma cursos y consulta con asesores financieros si es necesario.',
        date: '2024-03-15',
        link: '#'
    },
    {
        title: 'Diversifica tu cartera',
        content: 'No pongas todos tus huevos en una sola canasta. Diversificar tus inversiones entre diferentes activos (acciones, bonos, bienes raíces, etc.) puede ayudar a reducir el riesgo.',
        date: '2024-04-10',
        link: '#'
    },
    {
        title: 'Mantén una perspectiva a largo plazo',
        content: 'Las inversiones pueden fluctuar en el corto plazo, pero históricamente han tendido a crecer con el tiempo. Mantén la calma durante las caídas del mercado y enfócate en tus objetivos a largo plazo.',
        date: '2024-05-05',
        link: '#'
    }
]);
</script>

<template>
    <Menu />

    <div class="home-container">
        <section class="hero">
            <h2>Tips de Inversiones </h2>
            <div class="hero-card">
                <h3>Las inversiones son una herramienta poderosa para asegurar un buen futuro financiero</h3>
                
                <div class="info">
                    <p>Invertir no es solo para expertos financieros; con el conocimiento adecuado, cualquiera puede comenzar a invertir y hacer crecer su dinero. Aquí te presentamos algunos consejos clave para iniciarte en el mundo de las inversiones:</p>
                    <ul>
                        <li><strong>Define tus objetivos financieros:</strong> Antes de invertir, es crucial tener claros tus objetivos. ¿Estás invirtiendo para la jubilación, para comprar una casa o para financiar la educación? Tus objetivos influirán en tu estrategia de inversión.</li>
                        <li><strong>Conoce tu tolerancia al riesgo:</strong> Cada inversión conlleva un nivel de riesgo. Evalúa cuánto riesgo estás dispuesto a asumir y elige inversiones que se alineen con tu perfil de riesgo.</li>
                        <li><strong>Diversifica tu cartera:</strong> No pongas todos tus huevos en una sola canasta. Diversificar tus inversiones entre diferentes activos (acciones, bonos, bienes raíces, etc.) puede ayudar a reducir el riesgo.</li>
                        <li><strong>Investiga antes de invertir:</strong> Infórmate sobre las opciones de inversión disponibles y comprende cómo funcionan. Lee libros, toma cursos y consulta con asesores financieros si es necesario.</li>
                        <li><strong>Mantén una perspectiva a largo plazo:</strong> Las inversiones pueden fluctuar en el corto plazo, pero históricamente han tendido a crecer con el tiempo. Mantén la calma durante las caídas del mercado y enfócate en tus objetivos a largo plazo.</li>
                        <li><strong>Revisa y ajusta tu cartera regularmente:</strong> A medida que cambian tus objetivos y circunstancias financieras, es importante revisar y ajustar tu cartera de inversiones para asegurarte de que sigue alineada con tus metas.</li>
                    </ul>
                </div>

                <div class="info2">
                    <p>Recuerda, invertir es un viaje que requiere paciencia, disciplina y educación continua. Comenzar temprano y ser constante puede marcar una gran diferencia en tu futuro financiero. ¡Empieza hoy y construye el camino hacia la libertad financiera!</p>
                </div>
                
                <hr />

                <div class="cards-container">
                    <h3>Conoce nuestros tips de inversion</h3>

                    <div class="cards">
                        <Card v-for="(tip, index) in tips" :key="index" :title="tip.title" :content="tip.content" :date="tip.date" :link="tip.link" />
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
    padding: 2rem;
    box-sizing: border-box;
    width: 100%;
}
.info{
    width: 100%;
    text-align: left;
}
.info2 {
    width: 100%;
    display: flex;
    justify-content: center;
}

.info2 p {
    width: 80%; 
    text-align: center;
    font-size: 1.1rem;
    color: #334155;
    background: var(--color-2);
    border-left: 6px solid var(--color-1);
    padding: 1rem 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(52, 199, 89, 0.08);
    font-weight: 500;
}

.info p {
    font-size: 1.1rem;
    color: #334155;
    margin-bottom: 1rem;
}

ul {
    margin-left: 45px;
    margin-bottom: 2rem;
}
li {
    font-size: 1.1rem;
    color: #34495e;
    line-height: 1.6;
}

.cards-container {
    width: 100%;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.cards-container h3 {
    margin: 0;
}

.cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    width: 100%;
    margin-top: 2rem;
    box-sizing: border-box;
}

p {
    padding: 0 0 0 20px;
}

@media (max-width: 1100px) {
    .hero-card {
        padding: 2rem 1.2rem 1.5rem 1.2rem;
        max-width: 98vw;
    }
    .cards {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
    }
}

@media (max-width: 900px) {
    .home-container {
        padding: 1rem;
    }
    .hero-card {
        padding: 1.2rem 0.7rem;
        border-radius: 14px;
    }
    .cards {
        grid-template-columns: 1fr;
        gap: 1.2rem;
    }
    .info2 p {
        font-size: 1rem;
        padding: 0.7rem 0.7rem;
    }
    .info p {
        font-size: 1rem;
    }
    .info li {
        font-size: 1rem;
    }
    ul {
        margin-left: 20px;
    }
    p {
        padding-left: 10px;
    }
}

@media (max-width: 600px) {
    .hero h2 {
        font-size: 1.5rem;
    }
    .hero-card {
        padding: 0.7rem 0.2rem;
        border-radius: 10px;
    }
    .cards {
        gap: 0.7rem;
    }
    .info2 p {
        font-size: 0.95rem;
        padding: 0.5rem 0.5rem;
    }
    .info p {
        font-size: 0.95rem;
    }
    .info li {
        font-size: 0.95rem;
    }
}

@media (max-width: 400px) {
    .hero h2 {
        font-size: 1.1rem;
    }
    .hero-card {
        padding: 0.3rem 0.1rem;
    }
}
</style>
