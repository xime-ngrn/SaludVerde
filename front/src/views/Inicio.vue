<script setup>
import { ref } from 'vue';
import Menu from '@/components/menuBar.vue';
import Footer from '@/components/footer.vue';
import '@/assets/styles/base.css';
import router from '@/router';

function registrarse() {
    router.push('/registro');
}

</script>

<template>
  <Menu></Menu>

  <div class="home-container">
    <section class="hero">
      <h1 class="hero-title">Las finanzas al alcance de todos</h1>

      <div class="hero-card">
        <div class="hero-left">
          <h2>El 75% de los adolescentes no tienen un conocimiento de finanzas personales.</h2>
          <p class="hero-text">
            Aprender a manejar el dinero desde joven es una de las decisiones más inteligentes que puedes tomar.
          </p>
          <button class="btn-primary" @click="registrarse">Empezar ahora</button>
        </div>

        <div class="hero-right">
          <img src="@/assets/images/familia.png" class="hero-family" />
        </div>
      </div>
    </section>

    <section class="features">
      <h2 class="section-title">Comienza desde ahora</h2>

      <div class="features-grid">
        <div class="feature-card">
          <img src="@/assets/images/organizacion.png" class="feature-img" />
          <div class="info-card">
            <h3>Organización Clara</h3>
            <p>Visualiza tus objetivos con nosotros de forma más clara</p>
          </div>
        </div>

        <div class="feature-card">
          <img src="@/assets/images/goals.png" class="feature-img" />
          <div class="info-card">
            <h3>Metas para todos</h3>
            <p>Aprende a establecer y continuar con tus metas financieras a lo largo del tiempo</p>
          </div>
        </div>

        <div class="feature-card">
          <img src="@/assets/images/grupo-de-edad.png" class="feature-img" />
          <div class="info-card">
            <h3>Pequeños hábitos</h3>
            <p>Metas claras, pasos sencillos, logros grandes para un futuro certero</p>
          </div>
        </div>

        <div class="feature-card">
          <img src="@/assets/images/ahorro.png" class="feature-img" />
          <div class="info-card">
            <h3>Ahorra fácil</h3>
            <p>Cuida tu dinero y aprende a gestionarlo para disfrutarlo en el presente y estar seguro para el futuro</p>
          </div>
        </div>
      </div>

      <button class="btn-primary register" @click="registrarse">Regístrate ahora</button>
    </section>
  </div>

  <Footer />
</template>

<style scoped>
.home-container {
  max-width: 100;
}

.hero {
  background: linear-gradient(135deg, #93d2ff 0%, #4fd1c5 100%);
  padding: 40px 20px 40px 20px;
}

.hero-title {
  font-size: 48px;
  font-weight: 900;
  color: #1a3557;
  margin-bottom: 36px;
  letter-spacing: 1px;
  text-align: center;
}

.hero-card {
  max-width: 85%;
  min-height: 400px;
  margin: 0 auto;
  background: #fff;
  border-radius: 24px;
  padding: 40px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.10);
}

.hero-left {
  width: 55%;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  text-align: left;
  justify-content: center;
}
.hero-text {
  font-size: 20px;
  color: #444;
  margin-bottom: 18px;
}

.btn-primary {
  background: linear-gradient(90deg, #3878C7 0%, #4fd1c5 100%);
  color: #fff;
  font-weight: 700;
  border: none;
  border-radius: 12px;
  padding: 14px 32px;
  font-size: 18px;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(56,120,199,0.15);
  transition: background 0.2s, transform 0.2s;
}

.btn-primary:hover {
  background: linear-gradient(90deg, #4fd1c5 0%, #3878C7 100%);
  transform: translateY(-3px) scale(1.03);
}

.hero-right {
  width: 40%;
  text-align: right;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-family {
  width: 260px;
  border-radius: 18px;
  box-shadow: 0 2px 12px rgba(56,120,199,0.10);
}

.features {
  background: #f8fafc;
  padding: 40px 20px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 25px;
  justify-items: center;
}

.feature-card {
  width: 85%;
  border-radius: 18px;
  padding: 25px;
  background: var(--color-2);
  font-weight: 700;
  display: flex;
  flex-direction: row ;
  justify-content: space-between;
  align-items: center;
  text-align: left;
  border-radius: 12px;
  box-shadow: 0 2px 8px var(--fondo-3);
  transition: transform 0.2s, box-shadow 0.2s;
}

.feature-card:hover {
  transform: translateY(-4px) scale(1.03);
  box-shadow: 0 6px 24px rgba(56,120,199,0.18);
}

.feature-img {
  width: 150px;
  border-radius: 12px;
  background: #fff;
  padding: 10px;
}

.info-card {
  padding: 10px;
  margin: 0 15px 0 15px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.register {
  display: block;
  margin: 48px auto 0 auto;
}

/* Responsive Design */
@media (max-width: 900px) {
  .hero-card {
    flex-direction: column;
    width: 100%;
    padding: 24px;
  }
  .hero-left, .hero-right {
    width: 100%;
    text-align: center;
    padding: 10px;
  }
  .features-grid {
    grid-template-columns: 1fr;
    gap: 24px;
  }
  .right, .social {
    padding: 0;
  }
}
</style>