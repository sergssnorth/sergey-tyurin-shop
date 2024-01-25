<template>
    <div class="col-sm-6 col-md-4 col-lg-3 mb-3 px-1">
        <router-link v-bind:to="product.get_absolute_url">
            <div class="card rounded-0 border-0">
                <img v-bind:src="pictureHover" @mouseover="hover = true" @mouseleave="hover = false">
                <div class="card-body">
                    <h2 class="h6">{{ product.name }}</h2>
                    <p class="h6">₽ {{ product.price }}</p>
                </div>
            </div>
        </router-link>
    </div>
</template>

<script>
export default {
    name: 'ProductBox',
    data() {
        return {
            hover: false
        }
    },
    props: {
        product: Object,
    },
    computed: {
        pictureHover () {
            if (this.hover == true) {
                return this.product.get_image2
            } else {
                return this.product.get_image1
            }
        }
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