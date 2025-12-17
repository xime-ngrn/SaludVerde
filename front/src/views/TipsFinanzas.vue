<script setup>
import { ref } from 'vue';
import Menu from '@/components/MenuBar.vue';
import Footer from '@/components/Footer.vue';
import Card from '@/components/Card.vue';
import '@/assets/styles/base.css';

const tips = ref([
    {
        title: 'Realizar un presupuesto mensual',
        content: 'Crear un presupuesto te ayuda a controlar tus gastos y ahorrar dinero cada mes. Destina una cantidad fija para tus necesidades, deseos y ahorro. ¡Una meta clara te ayuda a priorizar tus gastos y seguir disfrutando de tu dinero!',
        date: '2024-01-15',
        link: '#'
    },
    {
        title: 'Ahorra al menos el 10% de tus ingresos',
        content: 'Destinar una parte de tus ingresos al ahorro te prepara para emergencias y metas futuras.Reúne al menos 3 a 6 meses de gastos básicos. Este colchón te protege contra imprevistos.',
        date: '2024-02-10',
        link: '#'
    },
    {
        title: 'Evita las deudas innecesarias',
        content: 'Antes de adquirir una deuda, evalúa si realmente es necesaria y si puedes pagarla a tiempo. Espera un día antes de comprar algo no planeado. Muchas veces te darás cuenta de que no lo necesitas, y si realmente lo quieres, puedes hacer un plan de ahorro y esperar una buena oferta. ¡Obtienes lo que deseas y a un mejor precio, sin riesgos!',
        date: '2024-03-05',
        link: '#'
    },
    {
        title: 'Regla 50/30/20',
        content: 'Distribuye tus ingresos de la siguiente manera: 50% para necesidades (alquiler, comida, transporte), 30% para deseos (salidas, entretenimiento) y 20% para ahorro e inversión. Esta regla te ayuda a mantener un equilibrio financiero saludable y a alcanzar tus metas económicas a largo plazo.',
        date: '2024-04-12',
        link: '#'
    },
    {
        title: 'Cuida los gastos hormiga',
        content: 'Pequeñas compras pueden sumar miles al año. Identifícalos y reduce los que no son necesarios. Prepara café en casa, lleva tu comida al trabajo o escuela, y opta por actividades gratuitas o económicas. Estos pequeños cambios pueden generar un gran impacto en tus finanzas a largo plazo.',
        date: '2024-05-20',
        link: '#'
    },
    {
        title: 'Administrar el uso de tarjetas de crédito',
        content: 'Las tarjetas de crédito pueden ser útiles para emergencias o compras grandes, pero es importante usarlas con responsabilidad. Paga el saldo completo cada mes para evitar intereses y no gastes más de lo que puedes pagar. Mantén un control estricto de tus gastos para evitar endeudarte innecesariamente.',
        date: '2024-06-18',
        link: '#'
    },
    {
        title: 'Aprovecha los descuentos con inteligencia',
        content: 'Los descuentos pueden ser una excelente manera de ahorrar dinero, pero es importante no caer en la trampa de comprar cosas que no necesitas solo porque están en oferta. Antes de aprovechar un descuento, pregúntate si realmente necesitas el producto y si lo comprarías al precio original. De esta manera, podrás hacer compras más inteligentes y evitar gastos innecesarios.',
        date: '2024-07-22',
        link: '#'
    }
])

</script>

<template>
    <Menu />

    <div class="home-container">
        <section class="hero">
            <h2>Tips de Finanzas Personales</h2>
            <div class="hero-card">
                <h3>Todo empieza con pequeños hábitos.</h3>
                <p>Conoce los tips de expertos en la materia y conoce más acerca de cómo mejorar tus hábitos financieros para un mejor futuro.</p>

                <div class="cards">
                    <Card
                        v-for="(tip, index) in tips"
                        :key="index"
                        :title="tip.title"
                        :content="tip.content"
                        :date="tip.date"
                        :link="tip.link"
                    />
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
.info, .info2 {
    width: 100%;
    text-align: left;
}

.info2 p {
    font-size: 1.1rem;
    color: #334155;
    margin: 1rem 0;
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

.info ul {
    padding-left: 1.2rem;
    margin: 0;
}

.info li {
    margin-bottom: 0.7rem;
    font-size: 1.05rem;
    color: #475569;
    line-height: 1.6;
}

.info li strong {
    color: var(--color-3);
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