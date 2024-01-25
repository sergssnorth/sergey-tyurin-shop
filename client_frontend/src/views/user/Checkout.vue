<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Оплата</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Продукт</th>
                            <th>Размер</th>
                            <th>Цена</th>
                            <th>Количество</th>
                            <th>Сумма</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr v-for="item in cart.items"
                            v-bind:key="item.product.id">

                            <td>{{ item.product.name }}</td>
                            <td>{{ item.size }}</td>
                            <td>{{ item.product.price }} ₽</td>
                            <td>{{ item.quantity }}</td>
                            <td>{{ getItemTotal(item).toFixed(2) }} ₽</td>
                        </tr>
                    </tbody>

                    <tfoot>
                        <tr>
                            <td colspan="3">Итог</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>{{ cartTotalPrice.toFixed(2) }} ₽</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box mb-0">
                <h2 class="subtitle">Детали доставки</h2>
                <p class="has-text-grey mb-4">* Все поля обязательны к заполнению, доставка осуществляется Почтой России</p>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>Имя*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="accountInformation.name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Фамилия*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="accountInformation.sname">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="accountInformation.email">
                            </div>
                        </div>

                        <div class="field">
                            <label>Телефон*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="accountInformation.phone">
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Область*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="accountInformation.client_delivery_information[0].region">
                            </div>
                        </div>

                        <div class="field">
                            <label>Город*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="accountInformation.client_delivery_information[0].city">
                            </div>
                        </div>

                        <div class="field">
                            <label>Улица*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="accountInformation.client_delivery_information[0].street">
                            </div>
                        </div>

                        <div class="field">
                            <label>Дом*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="accountInformation.client_delivery_information[0].building">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <hr>

                <div id="card-element" class="mb-5"></div>

                <template v-if="cartTotalLength">
                    <button class="button is-dark" @click="submitForm">Оплатить</button>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Checkout',
    data() {
        return {
            user_id: 0,
            accountInformation: {
                client_delivery_information: [
                    {
                        region: "",
                        city: "",
                        street: "",
                        building: ""
                    }
                ],
                name: "",
                sname: "",
                email: "",
                phone: ""
            },
            cart: {
                items: []
            },
            card: {},
            errors: []
        }
    },
    mounted() {
        document.title = 'Оплата'
        this.cart = this.$store.state.cart

    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        submitForm() {
            this.errors = []

            if (this.accountInformation.name === '') {
                this.errors.push('Поле имя не заполнено!')
            }

            if (this.accountInformation.sname === '') {
                this.errors.push('Поле фамилия не заполнено!')
            }

            if (this.accountInformation.email === '') {
                this.errors.push('Поле e-mail не заполненно!')
            }

            if (this.accountInformation.phone === '') {
                this.errors.push('Поле телефон не заполненно!')
            }

            if (this.accountInformation.client_delivery_information[0].region === '') {
                this.errors.push('Поле область не заполненно!')
            }

            if (this.accountInformation.client_delivery_information[0].city === '') {
                this.errors.push('Поле город не заполненно!')
            }

            if (this.accountInformation.client_delivery_information[0].street === '') {
                this.errors.push('Поле улица не заполненно!')
            }

            if (this.accountInformation.client_delivery_information[0].building === '') {
                this.errors.push('Поле дом не заполненно!')
            }

            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)

                this.stripe.createToken(this.card).then(result => {                    
                    if (result.error) {
                        this.$store.commit('setIsLoading', false)

                        this.errors.push('Something went wrong with Stripe. Please try again')

                        console.log(result.error.message)
                    } else {
                        this.stripeTokenHandler(result.token)
                    }
                })
            }
        },
        async stripeTokenHandler(token) {
            const items = []

            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    price: item.product.price * item.quantity
                }

                items.push(obj)
            }

            const data = {
                'first_name': this.accountInformation.name,
                'last_name': this.accountInformation.sname,
                'email': this.accountInformation.email,
                'phone': this.accountInformation.phone,

                'region': this.accountInformation.client_delivery_information[0].region,
                'city': this.accountInformation.client_delivery_information[0].city,
                'street': this.accountInformation.client_delivery_information[0].street,
                'building': this.accountInformation.client_delivery_information[0].building,
                
                'items': items,
            }

            await axios
                .post('/api/v1/checkout/', data)
                .then(response => {
                    this.$store.commit('clearCart')
                    this.$router.push('/cart/success')
                })
                .catch(error => {
                    this.errors.push('Something went wrong. Please try again')

                    console.log(error)
                })

                this.$store.commit('setIsLoading', false)
        }
    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
    }
}
</script>