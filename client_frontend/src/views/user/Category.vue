<template>
    <div class="row my-3 mx-0 pb-0 ">
        <div class="col-1">

        </div>
        <div class="col-10">
            <div class="row">
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
    name: 'Category',
    components: {
        ProductBox
    },
    data() {
        return {
            products: {
                totalCount: 0,
                totalPages: 0,
                products: []
            }
        }
    },
    async mounted() {
        const categorySlug = this.$route.params.category_slug
        await this.getProducts(categorySlug)
    },
    methods: {
        async getProducts(categorySlug) {
            const params = { category_slug: categorySlug,
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
    },
    watch: {
        async '$route'(to, from) {
            const categorySlug = this.$route.params.category_slug
            await this.getProducts(categorySlug)
        }
    },
    
}

</script>
