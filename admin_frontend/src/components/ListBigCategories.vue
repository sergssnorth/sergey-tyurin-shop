<template>
    <div class="card mb-1">
        <div class="card-body py-1 px-3">
        <div class="d-flex align-items-center">
            <span>{{ data_big_category.name }}</span>
            <button @click="$router.push(`/categories?big_category_id=${this.data_big_category.id}`)" class="btn btn-icon d-inline ms-auto px-2"><i class="bi bi bi-box-seam"></i></button>
            
            <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + data_big_category.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
            <div class="modal fade" :id="'editModal_' + data_big_category.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                <div class="modal-content">
                  <div class="modal-header text-center">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Изменить раздел, {{ data_big_category.name }}</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="name@example.com" v-model="update_data_big_category.name">
                      <label for="floatingInput">Имя</label>
                    </div>
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="Password" v-model="update_data_big_category.slug">
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
    name: 'ListBigCategories',
    props: {
        big_category: Object,
    },
    data() {
        return {
            data_big_category: this.big_category,
            update_data_big_category: {
                name: '',
                slug: '',
            },
        }
    },
    created() {
      this.update_data_big_category = { ...this.big_category };
    },
    methods: {
        async deleteBigCategory() {
            await axios
                .delete(`/big_category/${this.data_big_category.id}`)
                .then(response => {
                    console.log(response.data)
                    this.$emit('bigCategoryDeleted');
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async updateBigCategory() {
            const formData = {
                name: this.update_data_big_category.name,
                slug: this.update_data_big_category.slug
            }
            await axios
                .put(`/big_category/${this.data_big_category.id}`, formData)
                .then(response => {
                    console.log(response.data)
                    this.data_big_category = { ...this.update_data_big_category }
                    this.$emit('bigCategoryUpdated');
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