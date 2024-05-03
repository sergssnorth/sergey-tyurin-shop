<template>
    <div class="col-sm-6 col-md-4 col-lg-3 mb-3 px-2">
        <router-link :to="'/product/' + product.model_slug + '/' + product.id">
            <div class="card rounded-0 border-0">
                <img v-bind:src="pictureHover" @mouseover="hover = true" @mouseleave="hover = false">
                <div class="card-body">
                    <h2 class="h6" style="font-size: 0.9rem; margin-bottom: 0">{{ product.model_name }}</h2>
                    <!-- Вывести тут -->
                    <div class="mb-1">
                        <span style="font-size: 0.7rem; margin-right: 0.8rem;" v-for="instance in productInstances.productInstances" :key="instance.id" :style="{ color: getSizeColor(instance.size_name) }">{{ instance.size_name }}</span>
                    </div>
                    <p class="h6" style="font-size: 0.9rem; color: #212529;">₽ {{ minPrice }}</p>
                    
                </div>
            </div>
        </router-link>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    
    name: 'ProductBox',
    props: {
        product: Object,
    },
    data() {
        return {
            hover: false,
            dataProduct: this.product,
            productInstances : {
                totalCount: 0,
                totalPages: 0,
                productInstances: []
            },
            warehouseElements: {
                totalCount: 0,
                totalPages: 0,
                warehouseElements: []
            },
            priceListElements: {
                totalCount: 0,
                totalPages: 0,
                priceListElements: []
            }
        }
    },
    async created() {
        console.log("created")
        await this.getProductInstances(this.dataProduct.id);
        await this.getWarehouseElements(this.dataProduct.id)
        await this.getPriceList(this.dataProduct.id)
    },
    computed: {
        pictureHover () {
            if (this.hover == true) {
                return this.product.image2
            } else {
                return this.product.image1
            }
        },
        minPrice() {
            if (this.priceListElements.priceListElements.length > 0) {
                // Используйте метод reduce для поиска минимальной цены
                return this.priceListElements.priceListElements.reduce((min, current) => {
                    return current.price < min ? current.price : min;
                }, this.priceListElements.priceListElements[0].price); // Инициализируйте min первым значением цены
            } else {
                return 0; // Если список пуст, возвращайте 0 или другое значение по умолчанию
            }
        }
    },
    methods: {
        async getProductInstances(productId) {
            const params = {product_id: productId,
                            sort_by:"id",
                            order:"asc",
                            offset: 0,
                            limit: 20 }
            try {
                const response = await axios.get(`/product-instances`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, product_instances } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    productInstances: product_instances
                };
                this.productInstances = transformedData;
            } catch (error) {
                console.error(error);
            }
        },
        async getWarehouseElements(productId) {
            const params = {product_id: productId,
                            sort_by:"id",
                            order:"asc",
                            offset: 0,
                            limit: 20 }
            try {
                const response = await axios.get(`/warehouse-elements`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, warehouse_elements } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    warehouseElements: warehouse_elements
                };
                this.warehouseElements = transformedData;
            } catch (error) {
                console.error(error);
            }
        },
        async getPriceList(productId) {
            const params = {product_id: productId,
                            offset: 0,
                            limit: 20 }
            try {
                const response = await axios.get(`/price-list-elements`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, price_list_elements } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    priceListElements: price_list_elements
                };
                this.priceListElements = transformedData;
            } catch (error) {
                console.error(error);
            }
        },
        getSizeColor(sizeName) {
            const foundSize = this.warehouseElements.warehouseElements.find(element => element.size_name === sizeName);
            if (foundSize && foundSize.count !== 0) {
                return 'black'; // Цвет черный, если размер есть в наличии и его количество не нулевое
            } else {
                return '#A9A9A9'; // Цвет серый, если размер отсутствует в наличии или его количество нулевое
            }
        },
    }
}
</script>

<style scoped>

.px-1 {
    padding-right: 0.1rem !important;
    padding-left: 0.1rem !important;
}

.card {
    height: 100%;
}

a {
    text-decoration: none;
}

</style>