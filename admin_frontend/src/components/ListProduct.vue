<template>
    <div class="card mb-1">
            <a href="#collapseIndicatorChevron" class="card-body py-1 px-3 d-flex align-items-center" id="headingExampleTwo" data-bs-toggle="collapse" aria-expanded="false" aria-controls="collapseIndicatorChevron">
                <span>{{ product.color_name }}</span>
                <!-- <button @click="$router.push(`/categories?big_category_id=${this.category.id}`)" class="btn btn-icon d-inline ms-auto px-2"><i class="bi bi bi-box-seam"></i></button> -->
                
                <button  data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                <!-- <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                    <div class="modal-content">
                    <div class="modal-header text-center">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Изменить раздел</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="form-floating mb-3">
                        <input type="text" class="form-control" placeholder="name@example.com" v-model="category.name">
                        <label for="floatingInput">Имя</label>
                        </div>
                        <div class="form-floating mb-3">
                        <input type="text" class="form-control" placeholder="Password" v-model="category.slug">
                        <label for="floatingPassword">Слаг</label>
                        </div>
                    </div>
                    <div class="modal-footer ">
                        <button @click="updateBigCategory()" type="button" class="btn btn-primary" data-bs-dismiss="modal">Изменить</button>
                    </div>
                    </div>
                </div>
                </div> -->

                <button @click="deleteBigCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
            </a>
            <div class="separator-card"></div>
            <div id="collapseIndicatorChevron" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
                <div class="card-body">
                    <div v-for="size in data_product_sizes" :key="size.id" class="d-flex align-items-center">
                        <span>{{ size.size_name }}</span>
                        <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                        <button @click="deleteBigCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                    </div>
                    <div class="d-flex align-items-center mt-3">
                        <button class="btn btn-outline-success"><i class="bi bi-plus-circle" style="margin-right: 0.5em;"></i>Добавить размер</button>
                    </div>
                </div>
            </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ListProducts',
    props: {
        product: Object,
    },
    data() {
        return {
            data_product: this.product,
            data_product_sizes: []
        }
    },
    mounted() {
        this.getProductSizes(this.data_product.id)
    },
    computed: {
       
    },
    methods: {
        async getProductSizes(product_id) {
            const params = { product_id: product_id}
            await axios
                .get(`/product-sizes`, { params })
                .then(response => {
                    this.data_product_sizes = response.data
                    console.log(this.data_product_sizes)
                })
                .catch(error => {
                    console.log(error)
                })
        },

        async deleteBigCategory() {
            await axios
                .delete(`/big_category/${this.big_category.id}`)
                .then(response => {
                    console.log(response.data)
                    this.$emit('categoryDeleted', this.category.id);
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async updateBigCategory() {
            const formData = {
                name: this.big_category.name,
                slug: this.big_category.slug
            }
            await axios
                .put(`/big_category/${this.big_category.id}`, formData)
                .then(response => {
                    console.log(response.data)
                    this.$emit('categoryUpdated', this.category.id);
                })
                .catch(error => {
                    console.log(error)
                })
        },
    }
}
</script>

<style lang="scss">


.separator-card {
  display: flex;
  align-items: center;
  text-align: center;
}

.separator-card::before,
.separator-card::after {
  content: '';
  flex: 1;
  border-bottom: 1px solid #dee2e6;
  margin-left: 0.25em;
}

.separator-card:not(:empty)::before {
  margin-right: 2em;
}

.separator-card:not(:empty)::after {
  margin-left: 2em;
}
</style>