<template>
    <div class="row mx-0 pb-0 ">
        <ProductBox 
          v-for="product in latestProducts"
          v-bind:key="product.id"
          v-bind:product="product" />
    </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'

export default {
    name: 'Home',
    data() {
        return {
            latestProducts: []
        }
    },
    components: {
        ProductBox
    },
    mounted() {
        this.getLatestProducts()
        document.image
        document.title = 'Главная страница'
    },
    methods: {
        async getLatestProducts() {
            await axios
                .get('/api/v1/latest-products/')
                .then(response => {
                    this.latestProducts = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}

</script>
