import { createRouter, createWebHistory } from 'vue-router';

// Importar las vistas
import LogIn from '@/views/LogIn.vue';
import Registro from '@/views/Registro.vue';
import Home from '@/views/Home.vue';
import AboutUs from '@/views/Nosotros.vue';
import AvisoPrivacidad from '@/views/AvisoPrivacidad.vue';
import Inicio from '@/views/Inicio.vue';

import Error from '@/views/Error.vue';

// Definir las rutas
const routes = [
  { path: '/', name: 'Inicio', component: Inicio },
  { path: '/salud-verde', name: 'Salud Verde', component: Inicio },
  { path: '/login', name: 'LogIn', component: LogIn },
  { path: '/registro', name: 'Register', component: Registro },
  { path: '/home', name: 'Home', component: Home },
  { path: '/nosotros', name: 'Nosotros', component: AboutUs },
  { path: '/aviso-privacidad', name: 'AvisoPrivacidad', component: AvisoPrivacidad },
  { path: '/error', name: 'Error', component: Error },
  { path: '/:pathMatch(.*)*', redirect: '/error' }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router;