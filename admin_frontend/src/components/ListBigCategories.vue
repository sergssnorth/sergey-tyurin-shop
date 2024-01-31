<template>
    <div class="card mb-1">
        <div class="card-body py-1 px-3">
        <div class="d-flex align-items-center">
            <span>{{ category.name }}</span>
            <button class="btn btn-icon d-inline ms-auto px-2"><i class="bi bi bi-box-seam"></i></button>
            <button class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
            <button class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
        </div>
        </div>
    </div>

    <!-- <div class="col-sm-6 col-md-4 col-lg-3 mb-3 px-1">
        <router-link v-bind:to="product.get_absolute_url">
            <div class="card rounded-0 border-0">
                <img v-bind:src="pictureHover" @mouseover="hover = true" @mouseleave="hover = false">
                <div class="card-body">
                    <h2 class="h6">{{ product.name }}</h2>
                    <p class="h6">₽ {{ product.price }}</p>
                </div>
            </div>
        </router-link>
    </div> -->
</template>

<script>
export default {
    name: 'ListBigCategories',
    data() {
        return {
            
        }
    },
    props: {
        category: Object,
    },
    computed: {
       
    }
}
</script>

<style scoped>

</style>