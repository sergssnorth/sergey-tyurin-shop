<template>
    <div class="container-fluid">
        <!-- <div class="row justify-content-center"> -->
        <div class="row">
            <div class="col-8">
                <div v-for="item in cart.items" class="card" style="width: 18rem;">
                    <img v-bind:src="pictureHover" @mouseover="hover = true" @mouseleave="hover = false" class="card-img-top">
                    <div class="card-body">
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    </div>
                </div>
            </div>
            <div class="col-4">

            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        decrementQuantity(item) {
            item.quantity -= 1

            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
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
        removeFromCart(item) {
            this.$emit('removeFromCart', item)
            this.updateCart()
        },
    },
}
</script>


<style lang="scss">

a {
    color: #333;
    text-decoration: none;
}

a:hover {
    color: #000;
    text-decoration: none;
}
</style>


<template>
    <div class="container-fluid">
        <div class="row justify-content-center">
            <div class="col-12">
                <h1 class="title text-center">Корзина</h1>
                <div class="d-block d-sm-none"> <!-- Видно на XS -->
                    <table class="table" v-if="cartTotalLength">
                        <thead class="table-dark">
                            <tr class="">
                                <th>Продукт</th>
                                <!-- <th>Размер</th> -->
                                <th>Цена</th>
                                <th>Количество</th>
                                <!-- <th>Сумма</th> -->

                            </tr>
                        </thead>

                        <tbody class="table-group-divider">
                            <tr v-for="item in cart.items">
                                <td class="align-middle">
                                    <router-link :to="item.product.get_absolute_url"><span>{{ item.product.name }} - {{ item.size }}</span></router-link>
                                </td>
                                <td class="align-middle">
                                    {{ item.product.price }} ₽
                                </td>
                                <td class="align-middle">
                                    <button class="btn" @click="decrementQuantity(item)"><span class="mr-1"><i class="bi bi-dash-circle" style="font-size: 20px;"></i></span></button>
                                        {{ item.quantity }}
                                    <button class="btn" @click="incrementQuantity(item)"><span class="ml-1"><i class="bi bi-plus-circle" style="font-size: 20px;"></i></span></button>
                                    <button class="btn" @click="removeFromCart(item)"><span class="pl-4"><i class="bi bi-trash3" style="font-size: 20px;"></i></span></button>    
                                </td>
                            </tr>
                            <!-- <CartItem
                                v-for="item in cart.items"
                                v-bind:key="item.product.id"
                                v-bind:initialItem="item"
                                v-on:removeFromCart="removeFromCart" /> -->
                        </tbody>
                    </table>
                    <p v-else>У вас нет никаких товаров в вашей корзине...</p>
                </div>

                <div class="d-none d-sm-block d-md-none"> <!-- Видно на SM -->
                    <table class="table" v-if="cartTotalLength">
                        <thead class="table-dark">
                            <tr class="">
                                <th>Продукт</th>
                                <th>Размер</th>
                                <th>Цена</th>
                                <th>Количество</th>
                                <th>Сумма</th>

                            </tr>
                        </thead>

                        <tbody class="table-group-divider">
                            <tr v-for="item in cart.items">
                                <td class="align-middle">
                                    <router-link :to="item.product.get_absolute_url"><span>{{ item.product.name }}</span></router-link>
                                </td>
                                <td class="align-middle">
                                    {{ item.size }}
                                </td>
                                <td class="align-middle">
                                    {{ item.product.price }} ₽
                                </td>
                                <td class="align-middle">
                                    <button class="btn" @click="decrementQuantity(item)"><span class="mr-1"><i class="bi bi-dash-circle" style="font-size: 20px;"></i></span></button>
                                        {{ item.quantity }}
                                    <button class="btn" @click="incrementQuantity(item)"><span class="ml-1"><i class="bi bi-plus-circle" style="font-size: 20px;"></i></span></button>
                                    <button class="btn" @click="removeFromCart(item)"><span class="pl-4"><i class="bi bi-trash3" style="font-size: 20px;"></i></span></button>    
                                </td>
                                <td class="align-middle">
                                    {{ getItemTotal(item).toFixed(2) }} ₽
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <p v-else>У вас нет никаких товаров в вашей корзине...</p>
                </div>

                <div class="d-none d-md-block d-lg-none">
                    <table class="table" v-if="cartTotalLength">
                        <thead class="table-dark">
                            <tr class="">
                                <th>Продукт</th>
                                <th>Размер</th>
                                <th>Цена</th>
                                <th>Количество</th>
                                <th>Сумма</th>

                            </tr>
                        </thead>

                        <tbody class="table-group-divider">
                            <tr v-for="item in cart.items">
                                <td class="align-middle">
                                    <router-link :to="item.product.get_absolute_url"><span>{{ item.product.name }}</span></router-link>
                                </td>
                                <td class="align-middle">
                                    {{ item.size }}
                                </td>
                                <td class="align-middle">
                                    {{ item.product.price }} ₽
                                </td>
                                <td class="align-middle">
                                    <button class="btn" @click="decrementQuantity(item)"><span class="mr-1"><i class="bi bi-dash-circle" style="font-size: 20px;"></i></span></button>
                                        {{ item.quantity }}
                                    <button class="btn" @click="incrementQuantity(item)"><span class="ml-1"><i class="bi bi-plus-circle" style="font-size: 20px;"></i></span></button>
                                    <button class="btn" @click="removeFromCart(item)"><span class="pl-4"><i class="bi bi-trash3" style="font-size: 20px;"></i></span></button>    
                                </td>
                                <td class="align-middle">
                                    {{ getItemTotal(item).toFixed(2) }} ₽
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <p v-else>У вас нет никаких товаров в вашей корзине...</p>
                </div>
                <div class="d-none d-lg-block d-xl-none"><!-- Видно на LG -->
                    <table class="table" v-if="cartTotalLength">
                        <thead class="table-dark">
                            <tr class="">
                                <th>Продукт</th>
                                <th>Размер</th>
                                <th>Цена</th>
                                <th>Количество</th>
                                <th>Сумма</th>

                            </tr>
                        </thead>

                        <tbody class="table-group-divider">
                            <tr v-for="item in cart.items">
                                <td class="align-middle">
                                    <router-link :to="item.product.get_absolute_url"><span>{{ item.product.name }}</span></router-link>
                                </td>
                                <td class="align-middle">
                                    {{ item.size }}
                                </td>
                                <td class="align-middle">
                                    {{ item.product.price }} ₽
                                </td>
                                <td class="align-middle">
                                    <button class="btn" @click="decrementQuantity(item)"><span class="mr-1"><i class="bi bi-dash-circle" style="font-size: 20px;"></i></span></button>
                                        {{ item.quantity }}
                                    <button class="btn" @click="incrementQuantity(item)"><span class="ml-1"><i class="bi bi-plus-circle" style="font-size: 20px;"></i></span></button>
                                    <button class="btn" @click="removeFromCart(item)"><span class="pl-4"><i class="bi bi-trash3" style="font-size: 20px;"></i></span></button>    
                                </td>
                                <td class="align-middle">
                                    {{ getItemTotal(item).toFixed(2) }} ₽
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <p v-else>У вас нет никаких товаров в вашей корзине...</p>
                </div>
                <div class="d-none d-xl-block d-xxl-none"><!-- Видно на XL -->
                    <table class="table" v-if="cartTotalLength">
                        <thead class="table-dark">
                            <tr class="">
                                <th>Продукт</th>
                                <th>Размер</th>
                                <th>Цена</th>
                                <th>Количество</th>
                                <th>Сумма</th>

                            </tr>
                        </thead>

                        <tbody class="table-group-divider">
                            <tr v-for="item in cart.items">
                                <td class="align-middle">
                                    <router-link :to="item.product.get_absolute_url"><span>{{ item.product.name }}</span></router-link>
                                </td>
                                <td class="align-middle">
                                    {{ item.size }}
                                </td>
                                <td class="align-middle">
                                    {{ item.product.price }} ₽
                                </td>
                                <td class="align-middle">
                                    <button class="btn" @click="decrementQuantity(item)"><span class="mr-1"><i class="bi bi-dash-circle" style="font-size: 20px;"></i></span></button>
                                        {{ item.quantity }}
                                    <button class="btn" @click="incrementQuantity(item)"><span class="ml-1"><i class="bi bi-plus-circle" style="font-size: 20px;"></i></span></button>
                                    <button class="btn" @click="removeFromCart(item)"><span class="pl-4"><i class="bi bi-trash3" style="font-size: 20px;"></i></span></button>    
                                </td>
                                <td class="align-middle">
                                    {{ getItemTotal(item).toFixed(2) }} ₽
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <p v-else>У вас нет никаких товаров в вашей корзине...</p>
                </div>

                <div class="d-none d-sm-block d-sm-none d-xl-none d-xxl-block d-lg-none d-xl-block d-md-none d-lg-block  d-md-block"> <!-- Видно на самых больших -->
                    <table class="table" v-if="cartTotalLength">
                        <thead class="table-dark">
                            <tr class="">
                                <th>Продукт</th>
                                <th>Размер</th>
                                <th>Цена</th>
                                <th>Количество</th>
                                <th>Сумма</th>

                            </tr>
                        </thead>

                        <tbody class="table-group-divider">
                            <tr v-for="item in cart.items">
                                <td class="align-middle">
                                    <router-link :to="item.product.get_absolute_url"><span>{{ item.product.name }}</span></router-link>
                                </td>
                                <td class="align-middle">
                                    {{ item.size }}
                                </td>
                                <td class="align-middle">
                                    {{ item.product.price }} ₽
                                </td>
                                <td class="align-middle">
                                    <button class="btn" @click="decrementQuantity(item)"><span class="mr-1"><i class="bi bi-dash-circle" style="font-size: 20px;"></i></span></button>
                                        {{ item.quantity }}
                                    <button class="btn" @click="incrementQuantity(item)"><span class="ml-1"><i class="bi bi-plus-circle" style="font-size: 20px;"></i></span></button>
                                    <button class="btn" @click="removeFromCart(item)"><span class="pl-4"><i class="bi bi-trash3" style="font-size: 20px;"></i></span></button>    
                                </td>
                                <td class="align-middle">
                                    {{ getItemTotal(item).toFixed(2) }} ₽
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <p v-else>У вас нет никаких товаров в вашей корзине...</p>
                </div>
        
        </div>
            <div class="column is-12 box">
                <h2 class="subtitle">Оплата</h2>

                <strong>{{ cartTotalPrice.toFixed(2) }} ₽</strong>, {{ cartTotalLength }} вещи

                <hr>
                <router-link to="/cart/checkout" class="button is-dark">Перейти к оплате</router-link>
            </div>
        </div>
    </div>
</template>