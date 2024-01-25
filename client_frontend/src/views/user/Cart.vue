<template>
    <div class="container-fluid">
        <div class="d-block d-sm-none"><!-- Видно на XS --> 
            <div class="row mx-0 pb-0">
                <div class="col-12">
                    <div class="row pb-3">
                        <div class="col-12 " v-for="item in cart.items">
                            <div class="card my-3" style="max-width: 38rem;">
                                <div class="row g-0" style="padding-bottom: 0;">
                                    <img v-bind:src="item.product.get_image1"  class="img-fluid rounded-start">
                                    <div class="card-body">
                                        <div class="mb-3">
                                            <router-link :to="item.product.get_absolute_url"><span class="fs-5 text-dark" >{{ item.product.name }}</span></router-link>
                                        </div>
                                        
                                        <p class="fs-6 text-dark">Размер: {{ item.size }}</p>
                                        <p class="fs-6 text-dark">Цена: {{ item.product.price }} ₽</p>
                                        <div class="mb-3">
                                            <button class="btn" @click="decrementQuantity(item)"><span class="mr-1"><i class="bi bi-dash-circle" style="font-size: 20px;"></i></span></button>
                                                {{ item.quantity }}
                                            <button class="btn" @click="incrementQuantity(item)"><span class="ml-1"><i class="bi bi-plus-circle" style="font-size: 20px;"></i></span></button>
                                            <button class="btn" @click="removeFromCart(item)"><span class="pl-4"><i class="bi bi-trash3" style="font-size: 20px;"></i></span></button>    
                                        </div>
                                        <p class="fs-6 text-dark">Итог: {{ getItemTotal(item).toFixed(2) }} ₽</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <hr>
                <div class="col-12">
                    <h3 class="mt-4 text-center">Оформление заказа</h3>
                    <div class="card mb-5">
                        <div class="card-body">
                        <form class="row g-3 pb-0">
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" placeholder="">
                                    <label for="floatingInput">Имя *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Фамилия *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Email *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Телефон *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Область / Район *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Город *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Почтовый индекс *</label>
                                </div>
                            </div>
                            <!-- <div class="col-12">
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" id="gridCheck">
                                    <label class="form-check-label" for="gridCheck">
                                        Check me out
                                    </label>
                                </div>
                            </div> -->

                            <div class="col-12">
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Оформить заказ</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>        
                </div>
            </div>
        </div>

        <div class="d-none d-sm-block d-md-none"> <!-- Видно на SM -->
            <div class="row mx-0 pb-0">
                <div class="col-12">
                    <div class="row pb-3">
                        <div class="col-12 " v-for="item in cart.items">
                            <div class="card mx-5 my-4" style="max-width: 38rem;">
                                <div class="row g-0" style="padding-bottom: 0;">
                                    <div class="col-4">
                                        <img v-bind:src="item.product.get_image1"  class="img-fluid rounded-start">
                                    </div>
                                    <div class="col-8 d-flex align-items-center">
                                        <div class="card-body py-0">
                                            <div class="mb-1">
                                                <router-link :to="item.product.get_absolute_url"><span class="fs-5 text-dark" >{{ item.product.name }}</span></router-link>
                                            </div>
                                            
                                            <p class="fs-6 text-dark mb-1">Размер: {{ item.size }}</p>
                                            <p class="fs-6 text-dark mb-1" >Цена: {{ item.product.price }} ₽</p>
                                            <div class="mb-1">
                                                <button class="btn" @click="decrementQuantity(item)"><span class="mr-1"><i class="bi bi-dash-circle" style="font-size: 20px;"></i></span></button>
                                                    {{ item.quantity }}
                                                <button class="btn" @click="incrementQuantity(item)"><span class="ml-1"><i class="bi bi-plus-circle" style="font-size: 20px;"></i></span></button>
                                                <button class="btn" @click="removeFromCart(item)"><span class="pl-4"><i class="bi bi-trash3" style="font-size: 20px;"></i></span></button>    
                                            </div>
                                            <p class="fs-6 text-dark">Итог: {{ getItemTotal(item).toFixed(2) }} ₽</p>
                                        </div>
                                    </div>
                                
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <hr>
                <div class="col-12">
                    <h3 class="mt-4 text-center">Оформление заказа</h3>
                    <div class="card mb-5">
                        <div class="card-body">
                        <form class="row g-3 pb-0">
                            <div class="col-6">
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" placeholder="">
                                    <label for="floatingInput">Имя *</label>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Фамилия *</label>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Email *</label>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Телефон *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Область / Район *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Город *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Почтовый индекс *</label>
                                </div>
                            </div>
                            <!-- <div class="col-12">
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" id="gridCheck">
                                    <label class="form-check-label" for="gridCheck">
                                        Check me out
                                    </label>
                                </div>
                            </div> -->

                            <div class="col-12">
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Оформить заказ</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>        
                </div>
            </div>
        </div>
        <div class="d-none d-md-block d-lg-none"><!-- Видно на MD -->
            <div class="row mx-0 pb-0">
                <div class="col-10 offset-1">
                    <div class="row pb-3">
                        <div class="col-12" v-for="item in cart.items">
                            <div class="card mx-5 my-4" style="max-width: 38rem;">
                                <div class="row g-0" style="padding-bottom: 0;">
                                    <div class="col-4">
                                        <img v-bind:src="item.product.get_image1"  class="img-fluid rounded-start">
                                    </div>
                                    <div class="col-8 d-flex align-items-center">
                                        <div class="card-body py-0">
                                            <div class="mb-3">
                                                <router-link :to="item.product.get_absolute_url"><span class="fs-5 text-dark" >{{ item.product.name }}</span></router-link>
                                            </div>
                                            
                                            <p class="fs-6 text-dark mb-2">Размер: {{ item.size }}</p>
                                            <p class="fs-6 text-dark mb-2" >Цена: {{ item.product.price }} ₽</p>
                                            <div class="mb-3">
                                                <button class="btn" @click="decrementQuantity(item)"><span class="mr-1"><i class="bi bi-dash-circle" style="font-size: 20px;"></i></span></button>
                                                    {{ item.quantity }}
                                                <button class="btn" @click="incrementQuantity(item)"><span class="ml-1"><i class="bi bi-plus-circle" style="font-size: 20px;"></i></span></button>
                                                <button class="btn" @click="removeFromCart(item)"><span class="pl-4"><i class="bi bi-trash3" style="font-size: 20px;"></i></span></button>    
                                            </div>
                                            <p class="fs-6 text-dark">Итог: {{ getItemTotal(item).toFixed(2) }} ₽</p>
                                        </div>
                                    </div>
                                
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <hr>
                <div class="col-12">
                    <h3 class="mt-4 text-center">Оформление заказа</h3>
                    <div class="card mb-5">
                        <div class="card-body">
                        <form class="row g-3 pb-0">
                            <div class="col-6">
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" placeholder="">
                                    <label for="floatingInput">Имя *</label>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Фамилия *</label>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Email *</label>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Телефон *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Область / Район *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Город *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Почтовый индекс *</label>
                                </div>
                            </div>
                            <!-- <div class="col-12">
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" id="gridCheck">
                                    <label class="form-check-label" for="gridCheck">
                                        Check me out
                                    </label>
                                </div>
                            </div> -->

                            <div class="col-12">
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Оформить заказ</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>        
                </div>
            </div>
        </div>
        <div class="d-none d-lg-block d-xl-none"><!-- Видно на LG --> Видно только на lg</div>
        <div class="d-none d-xl-block d-xxl-none"><!-- Видно на XL --> Видно только на xl</div>

        <div class="d-none d-sm-block d-sm-none d-xl-none d-xxl-block d-lg-none d-xl-block d-md-none d-lg-block  d-md-block mb-5"> <!-- Видно на самых больших -->
            <div class="row mx-0 pb-0">
                <div class="col-1"></div>
                <div class="col-6">
                    <div class="row">
                        <div class="col-12 " v-for="item in cart.items">
                            <div class="card mx-5 my-4" style="max-width: 38rem;">
                                <div class="row g-0" style="padding-bottom: 0;">
                                    <div class="col-4">
                                        <img v-bind:src="item.product.get_image1"  class="img-fluid rounded-start">
                                    </div>
                                    <div class="col-8 d-flex align-items-center">
                                        <div class="card-body">
                                            <div class="mb-3">
                                                <router-link :to="item.product.get_absolute_url"><span class="fs-5 text-dark" >{{ item.product.name }}</span></router-link>
                                            </div>
                                            
                                            <p class="fs-6 text-dark">Размер: {{ item.size }}</p>
                                            <p class="fs-6 text-dark">Цена: {{ item.product.price }} ₽</p>
                                            <div class="mb-3">
                                                <button class="btn" @click="decrementQuantity(item)"><span class="mr-1"><i class="bi bi-dash-circle" style="font-size: 20px;"></i></span></button>
                                                    {{ item.quantity }}
                                                <button class="btn" @click="incrementQuantity(item)"><span class="ml-1"><i class="bi bi-plus-circle" style="font-size: 20px;"></i></span></button>
                                                <button class="btn" @click="removeFromCart(item)"><span class="pl-4"><i class="bi bi-trash3" style="font-size: 20px;"></i></span></button>    
                                            </div>
                                            <p class="fs-6 text-dark">Итог: {{ getItemTotal(item).toFixed(2) }} ₽</p>
                                        </div>
                                    </div>
                                
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-4">
                    <h3 class="mt-4 text-center">Оформление заказа</h3>
                    <div class="card">
                        <div class="card-body">
                        <form class="row g-3 pb-0">
                            <div class="col-6">
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" placeholder="">
                                    <label for="floatingInput">Имя *</label>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Фамилия *</label>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Email *</label>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Телефон *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Область / Район *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Город *</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="" placeholder="name@example.com">
                                    <label for="floatingInput">Почтовый индекс *</label>
                                </div>
                            </div>
                            <!-- <div class="col-12">
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" id="gridCheck">
                                    <label class="form-check-label" for="gridCheck">
                                        Check me out
                                    </label>
                                </div>
                            </div> -->

                            <div class="col-12">
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Оформить заказ</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>        
                </div>
                <div class="col-1"></div>
            </div>
        </div>
    </div>
</template>

<script>
// import CartItem from '@/components/CartItem.vue'

export default {
    name: 'Cart',
    // components: {
    //     CartItem
    // },
    data() {
        return {
            cart: {
                items: []
            },
            hover: false
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            function RemoveItem(i) {
                if(i.product.id !== item.product.id) {
                    return i 
                }
                else if (i.size !== item.size) {
                    return i   
                }            
            }
            this.cart.items = this.cart.items.filter(RemoveItem)
            this.updateCart()
        },
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        decrementQuantity(item) {
            item.quantity -= 1

            if (item.quantity === 0) {
                this.removeFromCart(item)
            }

            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity += 1

            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        pictureHover(item) {
            if (this.hover == true) {
                return item.product.get_image2
            } else {
                console.log("привет")
                console.log(item)
                return item.product.get_image1
            }
        }
        
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        
    }
}
</script>

<style lang="scss">




</style>