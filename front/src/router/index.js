import {createRouter, createWebHistory} from "vue-router";
import Home from '../components/mainVue.vue'

const routes = [
    {
        path:'',
        name:'home',
        component:Home
    },
    {
        path:'/callDuring',
        name:'caller',
        component:() => import('../components/Call.vue')
    }
]

const router = createRouter({
    history:createWebHistory(process.env.BASE_URL),
    routes
})

export default router