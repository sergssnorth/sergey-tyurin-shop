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
            <div id="collapseIndicatorChevron" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
                <div class="card-body">
                    Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred.
                    <button class="btn">Text</button>
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
        }
    },
    computed: {
       
    },
    methods: {
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

<style scoped>

</style>