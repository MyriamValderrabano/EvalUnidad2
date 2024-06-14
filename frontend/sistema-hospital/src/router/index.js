import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/components/login.vue'
import registerUser from'@/components/registerUser.vue'
import sidebar from '@/components/sidebar.vue'
import usuarios from '@/components/usuarios.vue'
import personas from '@/components/personas.vue'
import medicamentos from '@/components/medicamentos.vue'
import LotesMed from '@/components/LotesMed.vue'
import ConsumiblesView from '@/components/consumibles.vue'
import dispensacionView from '@/components/dispensacion.vue'
import tablaMedic from '@/components/tablamedicamentos.vue'
import tablaCon from '@/components/tablaconsumibles.vue'
import tablaLotes from '@/components/tablalotes.vue'
import tablaDis from'@/components/tabladispensacion.vue'
import footer from '@/components/Pie-Pagina.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component:registerUser
    },
    {
      path: '/footer',
      name: 'footer',
      component:footer
    },
    {
      path: '/home',
      name: 'home',
      component:sidebar,
      children:[
        {path:'/person',name:'personas',component:personas},
        {path:'/medicament',name:'medicamentos',component:medicamentos},
        {path:'/lotes',name:'lotesmed',component:LotesMed},
        {path:'/consumibles',name:'consumibles',component:ConsumiblesView},
        {path:'/dispensation',name:'dispensacion',component:dispensacionView},
        {path:'/tablamedic',name:'tablamedicamentos',component:tablaMedic},
        {path:'/tablacon',name:'tablaconsumibles',component:tablaCon},
        {path:'/tablalot',name:'tablalotes',component:tablaLotes},
        {path:'/tabladis',name:'tabladis',component:tablaDis},
      ]
    },
    {
      path: '/user',
      name: 'user',
      component:usuarios
    },
    {
      path: '/person',
      name: 'person',
      component:personas
    }]
})

export default router
