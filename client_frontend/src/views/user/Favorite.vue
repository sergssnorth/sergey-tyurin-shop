<template>
    <div class="row mx-0">
        <h1 class="my-3 text-center">Избранное</h1>
        <FavoriteItem
            v-for="item in favorite.items"
            v-bind:key="item.product.id"
            v-bind:initialItem="item"
            v-on:removeFromCart="removeFromCart" />
    </div>
</template>

<script>
import FavoriteItem from '@/components/FavoriteItem.vue'

export default {
    name: 'Favorite',
    components: {
        FavoriteItem
    },
    data() {
        return {
            favorite: {
                items: []
            }
        }
    },
    mounted() {
        this.favorite = this.$store.state.favorite
    },
    methods: {
        removeFromCart(item) {
            function RemoveItem(i) {
                if(i.product.id !== item.product.id && i.size !== item.size) {
                    return i
                }
            }
            this.cart.items = this.cart.items.filter(RemoveItem)
        }
    },
    computed: {
        cartTotalLength() {
            let totalLength = 0
            for (let i = 0; i < this.favorite.items.length; i++) {
                totalLength += 1
            }
            if (totalLength == 0) {
                return totalLength
            }
            return totalLength
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
a {
    text-decoration: none;
}
</style>
