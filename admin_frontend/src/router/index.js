import { createRouter, createWebHistory } from 'vue-router'
import AdminHome from '../views/AdminHome.vue'
import ProductStatistics from  '../views/ProductStatistics.vue'
import Models from  '../views/Models.vue'
import BigCategories from '../views/BigCategories.vue'

const routes = [
  {
    path: '/',
    name: 'AdminHome',
    component: AdminHome
  },
  {
    path: '/product-statistics',
    name: 'ProductStatistics',
    component: ProductStatistics
  },
  {
    path: '/big-categories',
    name: 'BigCategories',
    component: BigCategories
  },
  {
    path: '/models',
    name: 'Models',
    component: Models
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
