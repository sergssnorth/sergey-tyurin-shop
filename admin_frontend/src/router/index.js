import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

import ProductStatistics from  '../views/ProductStatistics.vue'

import BigCategory from '../views/BigCategory.vue'
import Category from '../views/Category.vue'
import Detail from '../views/Detail.vue'
import SizeGuide from '../views/SizeGuide.vue'
import Model from  '../views/Model.vue'
import Product from  '../views/Product.vue'

import Collection from  '../views/Collection.vue'
import Size from '../views/Size.vue'
import Color from '../views/Color.vue'
import OrderStatus from '../views/OrderStatus.vue'

import User from '../views/User.vue'
import Employee from '../views/Employee.vue'

import Order from '../views/Order.vue'

import Warehouse from '@/views/Warehouse.vue'
import PriceList from '@/views/PriceList.vue'

import Department from '@/views/Department.vue'
import EmployeeStatus from '@/views/EmployeeStatus.vue'



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
    path: '/details',
    name: 'Detail',
    component: Detail
  },

  {
    path: '/products',
    name: 'Product',
    component: Product
  },
  {
    path: '/collections',
    name: 'Collection',
    component: Collection
  },
  {
    path: '/size-guides',
    name: 'SizeGuide',
    component: SizeGuide
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
    path: '/users',
    name: 'User',
    component: User
  },
  {
    path: '/employees',
    name: 'Employee',
    component: Employee
  },

  {
    path: '/orders',
    name: 'Order',
    component: Order
  },

  {
    path: '/warehouses',
    name: 'Warehouse',
    component: Warehouse
  },
  {
    path: '/price-lists',
    name: 'PriceList',
    component: PriceList
  },
  {
    path: '/departments',
    name: 'Department',
    component: Department
  },
  {
    path: '/employee-statuses',
    name: 'EmployeeStatus',
    component: EmployeeStatus
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
