import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import AdminHome from '../views/admin/AdminHome.vue'
import LogIn from '../components/LogIn.vue'
import SignUp from '../components/SignUp.vue'
import Home from '../views/user/Home.vue'
import Product from '../views/user/Product.vue'
import Favorite from '../views/user/Favorite.vue'
import Cart from '../views/user/Cart.vue'
import Payment from '../views/user/Payment.vue'
import Category from '../views/user/Category.vue'
import AboutUs from '../views/user/AboutUs.vue'
import MyAccount from '../views/user/MyAccount.vue'
import Test from '../views/user/Test.vue'
import Checkout from '../views/user/Checkout.vue'

const routes = [
  {
    path: '/admin',
    name: 'AdminHome',
    component: AdminHome
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/product/:big_category_slug/:category_slug/:product_slug',
    name: 'Product',
    component: Product
  },
  {
    path: '/:big_category_slug/:category_slug',
    name: 'Category',
    component: Category
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/favorite',
    name: 'Favorite',
    component: Favorite
  },
  {
    path: '/cart/payment',
    name: 'Payment',
    component: Payment,
    meta: {
        requireLogin: true
    }
  },
  {
    path: '/about-us',
    name: 'AboutUs',
    component: AboutUs
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount
  },
  {
    path: '/test',
    name: 'Test',
    component: Test
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
        return ({
            el: to.hash,
            behavior: 'smooth',
        })
    } else if (savedPosition) {
        return (savedPosition);
    } else {
        return {left: 0, top: 0}
    }
},
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router