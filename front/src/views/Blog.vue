<script setup>
import { ref } from 'vue';
import Menu from '@/components/MenuBar.vue';
import Footer from '@/components/Footer.vue';
import Comment from '@/components/Comment.vue';
import '@/assets/styles/base.css';

const comments = ref([
    {
        author: 'Lalo',
        date: '2024-06-01',
        text: '¡Excelente blog! Los artículos son muy informativos y fáciles de entender.'
    },
    {
        author: 'María',
        date: '2024-06-05',
        text: 'La verdad nunca le había puesto mucha atención a mis finanzas personales, pensaba que con pagar mis cuentas a tiempo ya era suficiente. Pero cuando empecé a llevar un registro de mis gastos me di cuenta de cuánto dinero se me iba en cosas pequeñas como cafés, snacks o aplicaciones que ni usaba. Ahora trato de ahorrar al menos un 10% de lo que gano y me estoy organizando mejor. No soy experto, pero siento que poco a poco estoy tomando más control de mi dinero.'
    },
    {
        author: 'Carlos',
        date: '2024-06-10',
        text: 'Siempre pensé que ahorrar era imposible porque mi sueldo apenas alcanzaba, pero me recomendaron la regla del 50/30/20 y empecé a separar aunque fuera una cantidad pequeña. Al principio fueron $200 al mes, y ahora ya puedo ahorrar más sin sentir que me estoy quedando sin dinero. Me di cuenta de que la clave no es ganar mucho, sino administrar mejor lo que uno tiene.'
    },
    {
        author: 'Ana',
        date: '2024-06-12',
        text: 'Me encanta cómo este blog aborda temas financieros de manera tan accesible. Los consejos son prácticos y aplicables a la vida diaria. ¡Sigan así!'
    }
]);
</script>

<template>
    <Menu />

    <main class="home-container">
        <section class="hero">
            <h2>Blog de Salud Verde</h2>
            <article class="hero-card">
                <header>
                    <h3>
                        Bienvenido a nuestro blog, donde <strong>todos</strong> compartimos consejos y noticias sobre educación financiera.
                    </h3>
                </header>
                <section class="info">
                    <p>
                        En nuestro blog encontrarás artículos informativos, tips prácticos y las últimas novedades en el mundo de las finanzas personales. Nuestro objetivo es brindarte contenido valioso que te ayude a tomar decisiones financieras informadas y mejorar tu bienestar económico.
                    </p>
                    <ul>
                        <li><strong>Artículos Educativos:</strong> Explora una variedad de temas relacionados con la gestión del dinero, ahorro, inversión y planificación financiera.</li>
                        <li><strong>Consejos Prácticos:</strong> Obtén tips útiles para mejorar tus hábitos financieros y alcanzar tus metas económicas.</li>
                        <li><strong>Novedades del Sector:</strong> Mantente al día con las últimas tendencias y noticias en el ámbito financiero.</li>
                    </ul>
                </section>
                <section class="info2">
                    <p>
                        Te invitamos a leer nuestros artículos, compartir tus opiniones y participar en la conversación. Juntos, podemos construir una comunidad informada y empoderada en temas financieros. ¡Explora nuestro blog y comienza tu viaje hacia una mejor salud financiera hoy mismo!
                    </p>
                </section>
                <hr />
                <section class="comments-section">
                    <h3>Comentarios</h3>

                    <div class="agregar">
                        <form class="form" @submit.prevent="agregarComentario" autocomplete="off" >
                            <label for="comment">Agrega un comentario:</label>
                            <textarea></textarea>
                        </form>
                    </div>

                    <div class="comments">
                        <Comment
                            v-for="(comment, idx) in comments"
                            :key="idx"
                            :author="comment.author"
                            :date="comment.date"
                            :text="comment.text"
                        />
                    </div>
                </section>
            </article>
        </section>
    </main>

    <Footer />
</template>

<style>
.home-container {
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
    align-items: flex-start;
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 4px 24px rgba(44, 62, 80, 0.10);
    width: 100%;
    padding: 2rem 1.2rem 1.5rem 1.2rem;
}
.info, .info2 {
    width: 100%;
    text-align: left;
}
.info2 {
    margin-top: 1.5rem;
}
.comments-section {
    width: 90%;
    align-self: center;
}
.comments {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.agregar {
    width: 100%;
    margin: 20px 0;
}
.form {
    display: flex;
    flex-direction: column;
}
label {
    padding-left: 10px;
    text-align: left;
}

p {
    padding-left: 20px;
}
h3 {
    text-align: center;
    margin: 0 0 20px;
}
</style>