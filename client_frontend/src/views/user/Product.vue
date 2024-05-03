<template>
    <div class="container-fluid">
        <div class="d-block d-sm-none">
            <div class="row pb-3">
                <div id="carouselExampleSlidesOnly" class="carousel slide px-0" data-bs-ride="carousel">
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img v-bind:src="product.image1" class="d-block w-100" alt="...">
                        </div>
                        <div class="carousel-item">
                            <img v-bind:src="product.image2" class="d-block w-100" alt="...">
                        </div>
                        <div class="carousel-item">
                            <!-- <img v-bind:src="product.get_image3" class="d-block w-100" alt="..."> -->
                        </div>
                        <div class="carousel-item">
                            <!-- <img v-bind:src="product.get_image4" class="d-block w-100" alt="..."> -->
                        </div>

                    </div>
                </div>
            </div>
            <div class="row">
                <h1 class="">{{ product.model_name }}</h1>
                <h3 class="">Цена: 2000 ₽</h3>


                <template v-if="availableProductSize">
                    <div class="list-group list-group-horizontal px-2 mb-3">
                        <a href="#" v-for="size in product.available_product_size" class="list-group-item"
                            v-bind:class="{ 'active': isSelected(size.size_name) }"
                            v-on:click="selected = size.size_name"> {{ size.size_name }}</a>
                    </div>

                    <div class="row  p-0">
                        <div class="col-4">
                            <div class="btn-group btn-group-sm mb-3" role="group" aria-label="Basic outlined example">
                                <button type="button" @click="quantityMinus" class="btn"><i class="bi bi-dash-circle"
                                        style="font-size: 24px"></i></button>
                                <input type="number" class="form-control border-0 text-center " v-model="quantity"
                                    aria-describedby="button-addon1">
                                <button type="button" @click="quantityPlus" class="btn"><i class="bi bi-plus-circle"
                                        style="font-size: 24px"></i></button>
                            </div>
                        </div>
                        <div class="col-8">
                        </div>
                    </div>

                    <button type="button" class="btn btn-dark" @click="addToCart()">Добавить в корзину</button>
                    <button type="button" class="btn" style="outline: 0 !important"><i class="bi bi-heart mx-3"
                            @click="addToFavorite()" style="font-size: 20px"></i></button>


                </template>
                <template v-else>
                    <span class="title is-4">Нет в наличии</span>
                </template>

                <div>
                    <p class="">Информация:</p>
                </div>

                <p class="mb-1"><span class="title is-6">Описание: </span>Эта футболка из мягкого хлопкового джерси,
                    сочетающая
                    визуальные признаки вечной роскоши с
                    современной графической привлекательностью, украшена фирменным логотипом amiri и мотивом ma
                    в сезонном градиенте. этот чай является культовой эмблемой мира и прекрасно сочетается с
                    домашней джинсовой одеждой, брюками или шортами.</p>
                <p class="mb-1"><span class="title is-6">Коллекция: </span>до весны 2024 года</p>
                <p class="mb-1"><span class="title is-6">Производство: </span>сделано в италии</p>
                <p class="mb-1"><span class="title is-6">Состав: </span>100% хлопок</p>
            </div>
        </div>
        <div class="d-none d-sm-block">
            <div class="row pb-0 mt-3">
                <div class="col-7">
                    <div class="row pb-0">
                        <div class="col-lg-6" style="padding-right: 0;">
                            <div class="card rounded-0 border-0 mx-2 my-2">
                                <img v-bind:src="product.image1" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <ModalImage v-bind:product="product" />
                            </div>
                        </div>
                        <div class="col-lg-6" style="padding-left: 0;">
                            <div class="card rounded-0 border-0 mx-2 my-2">
                                <img v-bind:src="product.image2" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <ModalImage v-bind:product="product" />
                            </div>
                        </div>
                    </div>
                    <div class="row pb-0">
                        <div class="col-lg-6" style="padding-right: 0;">
                            <div class="card rounded-0 border-0 mx-2 my-2">
                                <img v-bind:src="product.image3" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <ModalImage v-bind:product="product" />
                            </div>
                        </div>
                        <div class="col-lg-6" style="padding-left: 0;">
                            <div class="card rounded-0 border-0 mx-2 my-2">
                                <img v-bind:src="product.image4" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <ModalImage v-bind:product="product" />
                            </div>
                        </div>
                    </div>
                    <div class="row pb-0">
                        <div class="col-lg-6" style="padding-right: 0;">
                            <div class="card rounded-0 border-0 mx-2 my-2">
                                <img v-bind:src="product.image5" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <ModalImage v-bind:product="product" />
                            </div>
                        </div>
                        <div class="col-lg-6" style="padding-left: 0;">
                            <div class="card rounded-0 border-0 mx-2 my-2">
                                <img v-bind:src="product.image6" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <ModalImage v-bind:product="product" />
                            </div>
                        </div>
                    </div>
                    <div class="row pb-0">
                        <div class="col-lg-6" style="padding-right: 0;">
                            <div class="card rounded-0 border-0 mx-2 my-2">
                                <img v-bind:src="product.image7" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <ModalImage v-bind:product="product" />
                            </div>
                        </div>
                        <div class="col-lg-6" style="padding-left: 0;">
                            <div class="card rounded-0 border-0 mx-2 my-2">
                                <img v-bind:src="product.image8" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <ModalImage v-bind:product="product" />
                            </div>
                        </div>
                    </div>
                    <div class="row mb-3">
                        <div class="col-lg-6" style="padding-right: 0;">
                            <div class="card rounded-0 border-0 mx-2 my-2">
                                <img v-bind:src="product.image9" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <ModalImage v-bind:product="product" />
                            </div>
                        </div>
                        <div class="col-lg-6" style="padding-left: 0;">
                            <div class="card rounded-0 border-0 mx-2 my-2">
                                <img v-bind:src="product.image10" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <ModalImage v-bind:product="product" />
                            </div>
                        </div>
                    </div>

                </div>

                <div class="col-5">
                    <div class="row">
                        <div class="col-1"></div>
                        <div class="col-10">
                            <h1 class="my-2" style="font-size: 1.5rem; font-weight: 600">{{ product.model_name }}</h1>
                            <p class="" style="font-size: 1.3rem;font-weight: 600">2000 ₽</p>

                            <!-- <button class="btn" style="font-size: 0.7rem; margin-right: 0.8rem;"
                                v-for="instance in productInstances.productInstances" :key="instance.id"
                                :style="{ color: getSizeColor(instance.size_name)}" :class="{'active': isSelected(instance.size_name)}" :click="selected = instance.size_name">{{ instance.size_name }}</button> -->

                            <button class="btn" style="font-size: 0.7rem; margin-right: 0.8rem;"
                                v-for="instance in productInstances.productInstances" :key="instance.id"
                                :style="{ color: getSizeColor(instance.size_name) }"
                                :class="{ 'active': isSelected(instance.size_name) }"
                                @click = "selected = instance.size_name">{{
                                instance.size_name }}</button>

                            <!-- <template v-if="availableProductSize">
                                <div class="list-group list-group-horizontal mb-2">
                                    <a href="#" v-for="size in product.available_product_size" class="list-group-item"
                                        style="" v-bind:class="{ 'active': isSelected(size.size_name) }"
                                        v-on:click="selected = size.size_name"> {{ size.size_name }}</a>
                                </div>


                                <div class="d-block d-none d-md-block d-lg-none mb-2">
                                    <div class="row  p-0">
                                        <div class="col-7">
                                            <div class="btn-group btn-group-sm mb-3" role="group"
                                                aria-label="Basic outlined example">
                                                <button type="button" @click="quantityMinus" class="btn"><i
                                                        class="bi bi-dash-circle" style="font-size: 24px"></i></button>
                                                <input type="number" class="form-control border-0 text-center "
                                                    v-model="quantity" aria-describedby="button-addon1">
                                                <button type="button" @click="quantityPlus" class="btn"><i
                                                        class="bi bi-plus-circle" style="font-size: 24px"></i></button>
                                            </div>
                                        </div>
                                        <div class="col-5">
                                        </div>
                                    </div>
                                </div>
                                <div class="d-block d-none d-lg-block d-xl-none mb-2">
                                    <div class="row  p-0">
                                        <div class="col-5">
                                            <div class="btn-group btn-group-sm mb-3" role="group"
                                                aria-label="Basic outlined example">
                                                <button type="button" @click="quantityMinus" class="btn"><i
                                                        class="bi bi-dash-circle" style="font-size: 24px"></i></button>
                                                <input type="number" class="form-control border-0 text-center "
                                                    v-model="quantity" aria-describedby="button-addon1">
                                                <button type="button" @click="quantityPlus" class="btn"><i
                                                        class="bi bi-plus-circle" style="font-size: 24px"></i></button>
                                            </div>
                                        </div>
                                        <div class="col-7">
                                        </div>
                                    </div>
                                </div>


                                <div class="d-none d-sm-block d-lg-none d-xl-block d-md-none d-lg-block mb-2">
                                  
                                    <div class="row pb-0">
                                        <div class="col-4">
                                            <div class="btn-group btn-group-sm" role="group"
                                                aria-label="Basic outlined example">
                                                <button type="button" @click="quantityMinus" class="btn"><i
                                                        class="bi bi-dash-circle" style="font-size: 24px"></i></button>
                                                <input type="number" class="form-control border-0 text-center "
                                                    v-model="quantity" aria-describedby="button-addon1">
                                                <button type="button" @click="quantityPlus" class="btn"><i
                                                        class="bi bi-plus-circle" style="font-size: 24px"></i></button>
                                            </div>
                                        </div>
                                        <div class="col-8">
                                        </div>
                                    </div>
                                </div>

                                <button type="button" class="btn btn-dark mb-2" @click="addToCart()">Добавить в
                                    корзину</button>
                                <template v-if="activeHeart">
                                    <button type="button" class="btn mx-2 mb-2" style="outline: 0 !important"><i
                                            class="bi bi-heart-fill px-1" @click="actionToFavorite()"
                                            style="font-size: 20px"></i></button>
                                </template>
                                <template v-else>
                                    <button type="button" class="btn mx-2 mb-2" style="outline: 0 !important"><i
                                            class="bi bi-heart px-1" @click="actionToFavorite()"
                                            style="font-size: 20px"></i></button>
                                </template>

                            </template>
                            <template v-else>
                                <span class="title is-4">Нет в наличии</span>
                            </template> -->



                            <div>
                                <p class="mb-1 fs-5 text">Информация:</p>
                            </div>

                            <p class="mb-2"><span class="title is-6">Описание: </span>Футболка из мягкого хлопкового
                                джерси,
                                сочетающая
                                визуальные признаки вечной роскоши с
                                современной графической привлекательностью, украшена фирменным логотипом amiri.</p>
                            <p class="mb-2"><span class="title is-6">Коллекция: </span>до весны 2024 года</p>
                            <p class="mb-2"><span class="title is-6">Производство: </span>сделано в италии</p>
                            <p class="mb-2"><span class="title is-6">Состав: </span>100% хлопок</p>
                        </div>
                        <div class="col-1">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios'
import ModalImage from '@/components/ModalImage'

export default {
    name: 'Product',
    data() {
        return {
            selected: null,

            product: {},

            otherProducts: {
                totalCount: 0,
                totalPages: 0,
                products: []
            },

            productInstances: {
                totalCount: 0,
                totalPages: 0,
                productInstances: []
            },

            warehouseElements: {
                totalCount: 0,
                totalPages: 0,
                warehouseElements: []
            },



            // favorite: {
            //     items: []
            // },
            quantity: 1
        }
    },
    components: {
        ModalImage
    },
    async mounted() {
        console.log("mounted")
        await this.getProduct()
        await this.getProductInstances(this.product.id)
        await this.getWarehouseElements(this.product.id)
        // await this.getOtherProducts(this.product.model_id)
        // this.favorite = this.$store.state.favorite
        console.log("mounted")
    },
    computed: {
        // availableProductSize() {
        //     if (this.product.available_product_size.length > 0) {
        //         return true
        //     }
        // },
        // activeHeart() {
        //     const item = {
        //         product: this.product,
        //     }
        //     let results = this.favorite.items.filter(i => i.product.id === item.product.id)
        //     if(results.length > 0){
        //         return true
        //     }
        // },
    },
    methods: {
        getSizeColor(sizeName) {
            const foundSize = this.warehouseElements.warehouseElements.find(element => element.size_name === sizeName);
            if (foundSize && foundSize.count !== 0) {
                return 'black'; // Цвет черный, если размер есть в наличии и его количество не нулевое
            } else {
                return '#A9A9A9'; // Цвет серый, если размер отсутствует в наличии или его количество нулевое
            }
        },
        handleButtonClick(instance) {
            // Set the clicked button as active
            this.activeSize = instance.size_name;

            // Perform certain actions based on the clicked button
            // For example, you can trigger a method here
        },
        changeColorName(colorName) {
            this.$refs.colorName.textContent = colorName;
        },
        resetColorName() {
            const defaultColorName = this.product.model_name;
            this.$refs.colorName.textContent = defaultColorName;
        },
        isSelected: function (i) {
            console.log("this i")
            console.log(i)
            console.log("this i")

            console.log("this.selected")
            console.log(this.selected)
            console.log("this.selected")
            return i == this.selected
        },
        // quantityPlus() {
        //     this.quantity += 1
        // },
        // quantityMinus() {
        //     this.quantity -= 1
        // },

        // async getProduct() {
        //     const model_slug = this.$route.params.model_slug
        //     const product_id = this.$route.params.product_id

        //     await axios
        //         .get(`/api/v1/product/${big_category_slug}/${category_slug}/${product_slug}`)
        //         .then(response => {
        //             this.product = response.data
        //             document.title = this.product.name + ' | Djackets'
        //             console.log(this.product)
        //         })
        //         .catch(error => {
        //             console.log(error)
        //         })
        // },
        // Остановился тут
        async getProduct() {
            const productId = this.$route.params.product_id

            const params = {
                product_id: productId,
                offset: 0,
                limit: 20
            }
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
                this.product = transformedData.products[0];
            } catch (error) {
                console.error(error);
            }
        },
        async getProductInstances(productId) {
            const params = {
                product_id: productId,
                sort_by: "id",
                order: "asc",
                offset: 0,
                limit: 20
            }
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
            const params = {
                product_id: productId,
                sort_by: "id",
                order: "asc",
                offset: 0,
                limit: 20
            }
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

        // addToCart() {
        //     if (isNaN(this.quantity) || this.quantity < 1) {
        //         this.quantity = 1
        //     }

        //     const item = {
        //         product: this.product,
        //         size: this.selected,
        //         quantity: this.quantity
        //     }

        //     this.$store.commit('addToCart', item)
        // },
        // actionToFavorite() {
        //     const item = {
        //         product: this.product,
        //     }

        //     // function Action(i) {
        //     //     if(i.product.id !== item.product.id) {
        //     //         return i
        //     //     } 
        //     // }
        //     // this.favorite.items = this.favorite.items.filter(Action)
        //     // localStorage.setItem('favorite', JSON.stringify(this.favorite.items))
        //     this.$store.commit('actionToFavorite', item)
        // },
        // addToFavorite() {
        //     const item = {
        //         product: this.product,
        //     }
        //     this.$store.commit('addToFavorite', item)
        // }
    }
}
</script>


<style lang="scss">
a.list-group-item.active {
    color: #fff;
    background-color: #333;
    border-color: #333;
}
</style>
