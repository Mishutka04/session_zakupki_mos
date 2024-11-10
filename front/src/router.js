import { createRouter, createWebHashHistory } from 'vue-router';
import ProcurementList from './components/ProcurementList.vue';
import QuotationSession from './components/QuotationSession.vue';
import TenderRequestForm from './components/TenderRequestForm.vue';
import Analys from './components/Analys.vue';
import A2 from './components/A2.vue';

export default createRouter({
    history: createWebHashHistory(),
    routes: [

        // Добавьте маршрут для корневого пути
        { path: '/', redirect: '/send-url/' }, // Перенаправление на /list/
        
        // Или, если вы хотите отобразить компонент
        // { path: '/', component: YourHomeComponent }, // Замените YourHomeComponent на ваш компонент
        
        // Добавьте обработчик несуществующих маршрутов
        // { path: '/:pathMatch(.*)*', redirect: '/send-url/' }, // Перенаправление на /list/ для несуществующих маршрутов

        { path: '/send-url', component: TenderRequestForm },

        

        
        // { name: 'test', path: '/test/', component: AdminPanel },
        
        // {
        //     path: '/:pathMatch(.*)*',
        //     redirect: "/",
        // }

    ]
})