<template>
    <div class="col-sm-6 col-md-4 col-lg-3 mb-3 px-1">
        <router-link v-bind:to="item.product.get_absolute_url">
            <div class="card rounded-0 border-0">
                <img v-bind:src="pictureHover" @mouseover="hover = true" @mouseleave="hover = false">
                <div class="card-body">
                    <h2 class="h6">{{ item.product.name }}</h2>
                    <p class="h6">₽ {{ item.product.price }}</p>
                </div>
            </div>
        </router-link>
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
            item: this.initialItem,
            hover: false
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
    computed: {
        pictureHover () {
            if (this.hover == true) {
                return this.item.product.get_image2
            } else {
                return this.item.product.get_image1
            }
        }
    }

}
</script>