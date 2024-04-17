import {createRouter, createWebHistory} from "vue-router";
import Home from '../components/mainVue.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes:[
        {
            path: '',
            name: 'home',
            component: Home
        },
        {
            path: '/caller',
            name: 'cal',
            component: () => import("../components/mainVue.vue")
        }
    ]
})

export default router
