<template>
    <div class="card mb-1">
        <div class="card-body py-1 px-3">
        <div class="d-flex align-items-center">
            <span>{{ data_model.name }} </span>
            
            
            <span class="ms-auto" style="color: grey; margin-right: 0.5rem;"><i class="bi bi-boxes"></i></span>
            <span class="" style="color: grey; margin-right: 1.5rem;"> Hello </span>
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <button class="btn btn-icon d-inline px-2"><i class="bi bi bi-box-seam"></i></button>
            
            <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + data_model.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
            <div class="modal fade" :id="'editModal_' + data_model.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                <div class="modal-content">
                  <div class="modal-header text-center">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Изменить модель, {{ data_model.name }}</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="name@example.com" v-model="update_data_model.name">
                      <label for="floatingInput">Имя</label>
                    </div>
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="Password" v-model="update_data_model.slug">
                      <label for="floatingPassword">Слаг</label>
                    </div>
                    <select v-model="update_data_model.big_category_id" class="form-select py-3" aria-label="Default select example">
                        <option :value="0">Выберите раздел</option>
                        <option v-for="big_category in data_big_categories" :key="big_category.id" :value="big_category.id">
                            {{ big_category.name }}
                        </option>
                    </select>
                  </div>
                  <div class="modal-footer ">
                    <button @click="updateCategory()" type="button" class="btn btn-primary" data-bs-dismiss="modal">Изменить</button>
                  </div>
                </div>
              </div>
            </div>

            <button @click="deleteCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
        </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ListModels',
    props: {
        model: Object,
        big_categories: Array,
        categories: Array,
        collections: Array
    },
    data() {
        return {
            data_model: this.model,
            data_big_categories: this.big_categories,
            data_categories: this.categories,
            data_collections: this.collections,

            update_data_model: {
                name: '',
                slug: '',
                big_category_id: '',
            },
        }
    },
    computed: {
        // bigCategoryName() {
        //     const bigCategoryId = this.data_category.big_category_id;
        //     const bigCategory = this.data_big_categories.find(category => category.id === bigCategoryId);
        //     return bigCategory ? bigCategory.name : '';
        // },
    },

    created() {
      this.update_data_category = { ...this.category };
    },
    methods: {
        async deleteCategory() {
            await axios
                .delete(`/category/${this.data_category.id}`)
                .then(response => {
                    console.log(response.data)
                    this.$emit('categoryDeleted');
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async updateCategory() {
            const formData = {
                name: this.update_data_category.name,
                slug: this.update_data_category.slug,
                big_category_id: this.update_data_category.big_category_id,
            }
            await axios
                .put(`/category/${this.data_category.id}`, formData)
                .then(response => {
                    console.log(response.data)
                    this.data_category = { ...this.update_data_category }
                    this.$emit('categoryUpdated');
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