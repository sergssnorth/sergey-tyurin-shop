<template>
        <div class="container-fluid">
            <div class="d-block d-sm-none">
                <div class="row pb-3">
                    <div id="carouselExampleSlidesOnly" class="carousel slide px-0" data-bs-ride="carousel">
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                                <img v-bind:src="product.get_image1" class="d-block w-100" alt="...">
                            </div>
                            <div class="carousel-item">
                                <img v-bind:src="product.get_image2" class="d-block w-100" alt="...">
                            </div>
                            <div class="carousel-item">
                                <img v-bind:src="product.get_image3" class="d-block w-100" alt="...">
                            </div>
                            <div class="carousel-item">
                                <img v-bind:src="product.get_image4" class="d-block w-100" alt="...">
                            </div>

                        </div>
                    </div>
                </div>
                <div class="row">
                    <h1 class="">{{ product.name }}</h1>
                    <h3 class="">Цена: {{ product.price }} ₽</h3>


                    <template v-if="availableProductSize">
                        <div class="list-group list-group-horizontal px-2 mb-3">
                            <a href="#" v-for = "size in product.available_product_size" class="list-group-item" v-bind:class="{ 'active' : isSelected(size.size_name) }" v-on:click="selected = size.size_name"> {{ size.size_name }}</a>
                        </div>

                        <div class="row  p-0">
                                <div class="col-4">
                                    <div class="btn-group btn-group-sm mb-3" role="group" aria-label="Basic outlined example">
                                        <button type="button" @click="quantityMinus" class="btn"><i class="bi bi-dash-circle" style="font-size: 24px"></i></button>
                                        <input type="number" class="form-control border-0 text-center " v-model="quantity" aria-describedby="button-addon1">
                                        <button type="button" @click="quantityPlus" class="btn"><i class="bi bi-plus-circle" style="font-size: 24px"></i></button>
                                    </div>
                                </div>
                                <div class="col-8">
                                </div>
                        </div>

                        <button type="button" class="btn btn-dark" @click="addToCart()">Добавить в корзину</button>
                        <button type="button" class="btn" style="outline: 0 !important"><i class="bi bi-heart mx-3" @click="addToFavorite()" style="font-size: 20px"></i></button>


                    </template>
                    <template v-else>
                        <span class="title is-4">Нет в наличии</span>
                    </template>

                    <div>
                    <p class="">Информация:</p>
                    </div>

                    <p class="mb-1"><span class="title is-6">Описание: </span>Эта футболка из мягкого хлопкового джерси, сочетающая визуальные признаки вечной роскоши с
                        современной графической привлекательностью, украшена фирменным логотипом amiri и мотивом ma
                        в сезонном градиенте. этот чай является культовой эмблемой мира и прекрасно сочетается с
                        домашней джинсовой одеждой, брюками или шортами.</p>
                    <p class="mb-1"><span class="title is-6">Коллекция: </span>до весны 2024 года</p>
                    <p class="mb-1"><span class="title is-6">Производство: </span>сделано в италии</p>
                    <p class="mb-1"><span class="title is-6">Состав: </span>100% хлопок</p>
                </div>
            </div>
            <div class="d-none d-sm-block">
                <div class="row pb-0">
                    <div class="col-8">
                        <div class="row pb-0"> 
                            <div class="col-lg-6 px-0">
                                <div class="card rounded-0 border-0">
                                    <img v-bind:src="product.get_image1" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                    <ModalImage v-bind:product="product" />

                                    <img v-bind:src="product.get_image3" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                    <ModalImage v-bind:product="product" />
                                </div>
                            </div>
                            <div class="col-lg-6 px-0">
                                <div class="card rounded-0 border-0">
                                    <img v-bind:src="product.get_image2" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                    <ModalImage v-bind:product="product" />

                                    <img v-bind:src="product.get_image4" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                    <ModalImage v-bind:product="product" />
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-4" style="margin-top: 1rem;"> 
                        <div class="" style="margin-bottom: 2rem;">

                        <h1 class="">{{ product.name }}</h1>
                        <p class="fs-4">Цена: {{ product.price }} ₽</p>

                        <template v-if="availableProductSize">

                            <div class="list-group list-group-horizontal mb-2">
                                <a href="#" v-for = "size in product.available_product_size" class="list-group-item" style="" v-bind:class="{ 'active' : isSelected(size.size_name) }" v-on:click="selected = size.size_name"> {{ size.size_name }}</a>
                            </div>
                            

                            <div class="d-block d-none d-md-block d-lg-none mb-2"><!-- На md -->
                                <div class="row  p-0">
                                    <div class="col-7">
                                        <div class="btn-group btn-group-sm mb-3" role="group" aria-label="Basic outlined example">
                                            <button type="button" @click="quantityMinus" class="btn"><i class="bi bi-dash-circle" style="font-size: 24px"></i></button>
                                            <input type="number" class="form-control border-0 text-center " v-model="quantity" aria-describedby="button-addon1">
                                            <button type="button" @click="quantityPlus" class="btn"><i class="bi bi-plus-circle" style="font-size: 24px"></i></button>
                                        </div>
                                    </div>
                                    <div class="col-5">
                                    </div>
                                </div>
                            </div>
                            <div class="d-block d-none d-lg-block d-xl-none mb-2"><!-- На lg -->
                                <div class="row  p-0">
                                    <div class="col-5">
                                        <div class="btn-group btn-group-sm mb-3" role="group" aria-label="Basic outlined example">
                                            <button type="button" @click="quantityMinus" class="btn"><i class="bi bi-dash-circle" style="font-size: 24px"></i></button>
                                            <input type="number" class="form-control border-0 text-center " v-model="quantity" aria-describedby="button-addon1">
                                            <button type="button" @click="quantityPlus" class="btn"><i class="bi bi-plus-circle" style="font-size: 24px"></i></button>
                                        </div>
                                    </div>
                                    <div class="col-7">
                                    </div>
                                </div>
                            </div>
                        

                            <div class="d-none d-sm-block d-lg-none d-xl-block d-md-none d-lg-block mb-2"> <!-- На больших экранах -->
                                <div class="row pb-0">
                                    <div class="col-4">
                                        <div class="btn-group btn-group-sm" role="group" aria-label="Basic outlined example">
                                            <button type="button" @click="quantityMinus" class="btn"><i class="bi bi-dash-circle" style="font-size: 24px"></i></button>
                                            <input type="number" class="form-control border-0 text-center " v-model="quantity" aria-describedby="button-addon1">
                                            <button type="button" @click="quantityPlus" class="btn"><i class="bi bi-plus-circle" style="font-size: 24px"></i></button>
                                        </div>
                                    </div>
                                    <div class="col-8">
                                    </div>
                                </div>
                            </div>
                            
                            <button type="button" class="btn btn-dark mb-2" @click="addToCart()">Добавить в корзину</button>
                            <template v-if="activeHeart">
                                <button type="button" class="btn mx-2 mb-2" style="outline: 0 !important"><i class="bi bi-heart-fill px-1" @click="actionToFavorite()" style="font-size: 20px"></i></button>
                            </template>
                            <template v-else>
                                <button type="button" class="btn mx-2 mb-2" style="outline: 0 !important"><i class="bi bi-heart px-1" @click="actionToFavorite()" style="font-size: 20px"></i></button>
                            </template>
                            
                        </template>
                        <template v-else>
                            <span class="title is-4">Нет в наличии</span>
                        </template>
                        
                        </div>

                        <div>
                            <p class="mb-1 fs-5 text">Информация:</p>
                        </div>

                        <p class="mb-2"><span class="title is-6">Описание: </span>Футболка из мягкого хлопкового джерси, сочетающая визуальные признаки вечной роскоши с
                        современной графической привлекательностью, украшена фирменным логотипом amiri.</p>
                        <p class="mb-2"><span class="title is-6">Коллекция: </span>до весны 2024 года</p>
                        <p class="mb-2"><span class="title is-6">Производство: </span>сделано в италии</p>
                        <p class="mb-2"><span class="title is-6">Состав: </span>100% хлопок</p>
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
            selected: 0,
            isActive: 'L',
            product: {
                id : 0,
                name: "",
                get_absolute_url: "",
                price: "",
                get_image1: "",
                get_image2: "",
                get_image3: "",
                get_image4: "",
                available_product_size: []
            },
            favorite: {
                items: []
            },
            quantity: 1
        }
    },
    components: {
        ModalImage
    },
    mounted() {
        this.getProduct() 
        this.favorite = this.$store.state.favorite
    
    },
    computed: {
        availableProductSize() {
            if (this.product.available_product_size.length > 0) {
                return true
            }
        },
        activeHeart() {
            const item = {
                product: this.product,
            }
            let results = this.favorite.items.filter(i => i.product.id === item.product.id)
            if(results.length > 0){
                return true
            }
        },
    },
    methods: {
        isSelected: function (i) {
            return i === this.selected
        },
        quantityPlus() {
            this.quantity += 1
        },
        quantityMinus() {
            this.quantity -= 1
        },

        async getProduct() {
            const big_category_slug = this.$route.params.big_category_slug
            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/product/${big_category_slug}/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data
                    document.title = this.product.name + ' | Djackets'
                    console.log(this.product)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                size: this.selected,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)
        },
        actionToFavorite() {
            const item = {
                product: this.product,
            }

            // function Action(i) {
            //     if(i.product.id !== item.product.id) {
            //         return i
            //     } 
            // }
            // this.favorite.items = this.favorite.items.filter(Action)
            // localStorage.setItem('favorite', JSON.stringify(this.favorite.items))
            this.$store.commit('actionToFavorite', item)
        },
        addToFavorite() {
            const item = {
                product: this.product,
            }
            this.$store.commit('addToFavorite', item)
        }
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
