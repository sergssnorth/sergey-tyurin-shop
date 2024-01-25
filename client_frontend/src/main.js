import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'
import 'bootstrap-icons/font/bootstrap-icons.css'
import { Toast } from 'bootstrap/dist/js/bootstrap.js'
import axios from 'axios'

axios.defaults.baseURL = "http://127.0.0.1:8000"
// axios.defaults.baseURL = "https://api.sergeytyurin.ru"

createApp(App).use(store).use(router, axios).mount('#app')
