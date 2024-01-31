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