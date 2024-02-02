<template>
    <div class="card mb-1">
        <div class="card-body py-1 px-3">
        <div class="d-flex align-items-center">
            <span>{{ localCategory.name }}</span>
            <button class="btn btn-icon d-inline ms-auto px-2"><i class="bi bi bi-box-seam"></i></button>
            
            <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
            <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                <div class="modal-content">
                  <div class="modal-header text-center">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Изменить раздел</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="name@example.com" v-model="localCategory.name">
                      <label for="floatingInput">Имя</label>
                    </div>
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="Password" v-model="localCategory.slug">
                      <label for="floatingPassword">Слаг</label>
                    </div>
                  </div>
                  <div class="modal-footer ">
                    <button @click="updateBigCategory()" type="button" class="btn btn-primary" data-bs-dismiss="modal">Изменить</button>
                  </div>
                </div>
              </div>
            </div>

            <button @click="deleteBigCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
        </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ListCategories',
    props: {
        category: Object,
    },
    data() {
        return {
            localCategory: this.category,
        }
    },
    computed: {
       
    },
    methods: {
        async deleteCategory() {
            await axios
                .delete(`/category/${this.localCategory.id}`)
                .then(response => {
                    console.log(response.data)
                    this.$emit('categoryDeleted', this.localCategory.id);
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async updateCategory() {
            const formData = {
                name: this.localCategory.name,
                slug: this.localCategory.slug
            }
            await axios
                .put(`/category/${this.localCategory.id}`, formData)
                .then(response => {
                    console.log(response.data)
                    this.$emit('categoryUpdated', this.localCategory.id);
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