import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

import ProductStatistics from  '../views/ProductStatistics.vue'

import BigCategory from '../views/BigCategory.vue'
import Category from '../views/Category.vue'
import Model from  '../views/Model.vue'
import Product from  '../views/Product.vue'

import Collection from  '../views/Collection.vue'
import Size from '../views/Size.vue'
import Color from '../views/Color.vue'
import OrderStatus from '../views/OrderStatus.vue'

import Client from '../views/Client.vue'

import Order from '../views/Order.vue'




const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/product-statistics',
    name: 'ProductStatistics',
    component: ProductStatistics
  },
  {
    path: '/big-categories',
    name: 'BigCategory',
    component: BigCategory
  },
  {
    path: '/categories',
    name: 'Category',
    component: Category
  },
  {
    path: '/models',
    name: 'Model',
    component: Model
  },
  {
    path: '/product/:model_id',
    name: 'Product',
    component: Product
  },
  {
    path: '/collections',
    name: 'Collection',
    component: Collection
  },
  {
    path: '/sizes',
    name: 'Size',
    component: Size
  },
  {
    path: '/colors',
    name: 'Color',
    component: Color
  },
  {
    path: '/order-status',
    name: 'OrderStatus',
    component: OrderStatus
  },

  {
    path: '/clients',
    name: 'Client',
    component: Client
  },

  {
    path: '/orders',
    name: 'Order',
    component: Order
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
