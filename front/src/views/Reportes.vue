<script setup>
import Menu from '@/components/MenuBar2.vue';
import Options from '@/components/OptionsBar.vue';
import Reporte from '@/components/Reporte.vue';

const reportes = [
    { title: 'Mayo', gastos: 1200, ingresos: 3000 },
    { title: 'Junio', gastos: 3500, ingresos: 9000 },
    { title: 'Julio', gastos: 15000, ingresos: 36000 },
];



</script>

<template>
    <Menu />
    
    <div class="home-container">
        <Options />

        <div class="home">
            <h3>Reportes Mensuales</h3>

            <button class="agregar">Agregar Reporte</button>
            
            <div class="reportes">
                <Reporte v-for="(reporte, index) in reportes" :key="index" :title="reporte.title" :gastos="reporte.gastos" :ingresos="reporte.ingresos" />
            </div>
        </div>
    </div>
</template>

<style scoped>
.home-container {
    display: flex;
    flex-direction: row;
    background: #f8fafc;
    min-height: 100vh; 
    overflow-y: auto;
}
.home {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 1.5rem;
    color: #334155;
    padding: 20px;
}
.reportes {
    flex-grow: 1;
    padding: 20px;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    align-content: flex-start;
    font-size: 1.5rem;
    color: #334155;
    overflow-y: auto;
    height: auto;
    max-height: 100vh;
}
.agregar {
    background-color: var(--color-1);
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    margin: 0;
    font-size: 1rem;
    align-self: flex-end;
    margin-right: 30px;
}

@media (max-width: 900px) {
    .home-container {
        flex-direction: column; /* Mobile: OptionsBar arriba de Home */
        overflow-y: auto; /* El scroll lo manejará el container principal */
    }

    /* 💡 Ocultar OptionsBar para mobile. 
       Esto usualmente se maneja haciendo el Options un componente de menú de hamburguesa. */
    .options-bar {
        /* Para simular que Options se convierte en una barra horizontal o se oculta. 
           Si no lo vas a ocultar, asegúrate de que no tenga un 'width' fijo. */
        width: 100%;
        min-height: auto;
        /* display: none; */ 
    }

    .home {
        padding: 10px;
        /* En mobile, puede ser mejor que los reportes ocupen todo el ancho para una mejor lectura. */
        justify-content: center; 
    }
    
    /* Si el componente Reporte no es flexible, hazlo 100% de ancho en mobile. */
    /* Aquí necesitarías saber la clase raíz del componente Reporte. 
       Ejemplo: .reporte-card { width: 100%; } */
}
</style>