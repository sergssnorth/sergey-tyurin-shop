<template>
    <div class="row my-3 mx-0 pb-0 ">
        <div class="col-1">

        </div>
        <div class="col-10">
            <div class="row mt-2">
                <ProductBox 
                v-for="product in products.products"
                :key="product.id"
                :product="product" />
            </div>
        </div>
        <div class="col-1">

        </div>
        
    </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'

export default {
    name: 'Home',
    data() {
        return {
            products: {
                totalCount: 0,
                totalPages: 0,
                products: []
            }
        }
    },
    components: {
        ProductBox
    },
    async mounted() {
        console.log("ПРИВЕТ ПРИВЕТ ПРИВЕТ")
        console.log("ПРИВЕТ ПРИВЕТ ПРИВЕТ")
        console.log("ПРИВЕТ ПРИВЕТ ПРИВЕТ")
        console.log("ПРИВЕТ ПРИВЕТ ПРИВЕТ")
        document.title = 'Главная страница'
        await this.getProducts()
    },
    methods: {
        async getProducts() {
            const params = { price_list_id: 1,
                            offset: 0,
                            limit: 20 }
            try {
                const response = await axios.get(`/products`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, products } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    products: products
                };
                this.products = transformedData;
                console.log(this.products)
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } 
        }
    }
}

</script>
