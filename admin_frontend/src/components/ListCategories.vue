<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron"
        :style="cardBodyStyles">
            
            <div class="flex-grow-1 d-flex  align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.5rem;">
                <i class="bi bi-person-circle"></i>
                </span>
                <span>{{ dataCategory.name }}</span>
                <span class="ms-auto" style="color: grey; margin-right: 0rem;"><i class="bi bi-hash"></i></span>
                <span class="" style="color: grey; margin-right: 1.5rem;">{{ dataCategory.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button data-bs-toggle="modal" data-bs-target="#edi" class="btn btn-icon d-inline text-success px-2"><i class="bi bi-bag-plus"></i></button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataCategory.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                
                
                <div class="modal fade" :id="'editModal_' + dataCategory.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение клиента</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mb-3">
                                <input type="text" class="form-control" placeholder="name@example.com" v-model="updatedCategory.name">
                                <label for="floatingInput">Имя</label>
                                </div>
                                <div class="form-floating mb-3">
                                <input type="text" class="form-control" placeholder="Password" v-model="updatedCategory.slug">
                                <label for="floatingPassword">Слаг</label>
                                </div>
                            </div>
                            <div class="modal-footer ">
                                <button @click="updateClient()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Изменить</button>
                            </div>
                        </div>
                    </div>
                </div>

                <button @click="deleteClient()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
            </div>
        </div>
        <div class="separator-card" v-show="isCollapsed"></div>
        <div :id="'collapseProduct' + dataCategory.id" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
            <div class="card-body">
                <div v-if="loading">
                    <div class="text-center">
                        <div v-show="loading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>

                <div v-if="!loading">
                    <div v-if="dataModels.models.length != 0">
                        <div v-for="model in dataModels.models" :key="category.id" class="d-flex align-items-center">
                            <span style="margin-right: 0.5em;">{{ model.id }}.</span>
                            <span>{{ model.name }}</span>
                            <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                            <button @click="deleteBigCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                        </div>
                    </div>
                    <div v-else>
                        <span>Категорий нет</span>
                    </div>
                </div>
                
            </div>
        </div>
    </div>

    <!-- <div class="card mb-1">
        <div class="card-body py-1 px-3">
        <div class="d-flex align-items-center">
            <span>{{ data_category.name }} </span>
            
            
            <span class="ms-auto" style="color: grey; margin-right: 0.5rem;"><i class="bi bi-boxes"></i></span>
            <span class="" style="color: grey; margin-right: 1.5rem;">{{ categoryName }}</span>
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <button @click="$router.push(`/models?big_category_id=${this.data_category.big_category_id}&category_id=${this.data_category.id}&collection_id=0`)" class="btn btn-icon d-inline px-2"><i class="bi bi bi-box-seam"></i></button>
            
            <button  data-bs-toggle="modal" :data-bs-target="'#editModal_' + data_category.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
            <div class="modal fade" :id="'editModal_' + data_category.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                <div class="modal-content">
                  <div class="modal-header text-center">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Изменить категорию, {{ data_category.name }}</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="name@example.com" v-model="update_data_category.name">
                      <label for="floatingInput">Имя</label>
                    </div>
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="Password" v-model="update_data_category.slug">
                      <label for="floatingPassword">Слаг</label>
                    </div>
                    <select v-model="update_data_category.big_category_id" class="form-select py-3" aria-label="Default select example">
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
    </div> -->
</template>

<script>
import axios from 'axios'
import { Collapse } from 'bootstrap/dist/js/bootstrap.js'


export default {
    name: 'ListCategories',
    props: {
        category: Object,
        bigСategories: Array
    },
    data() {
        return {
            isCollapsed : false,
            
            dataCategory : this.category,
            updatedCategory: {
                name: '',
                slug: '',
            },
            
            dataModels : {
                totalCount: 0,
                totalPages: 0,
                categories: []
            },
            
            loading: true,
        }
    },

    computed: {
        cardBodyStyles() {
            if (this.isCollapsed) {
                return {
                backgroundColor: 'rgba(238, 238, 238, 0.637)',
                borderRadius: '1.5rem 1.5rem  0 0',
                };
            } else {
                return {};
            }
        },
    },
    created() {
        this.updatedCategory = { ...this.category };
    },
    methods: {
        async getModels(categoryId) {
            this.loading = true;
            const params = { category_id: categoryId,
                            offset: 0,
                            limit: 20 }
            try {
                const response = await axios.get(`/models`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, models } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    models: models
                };
                this.dataModels = transformedData;
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.loading = false;
            }
        },

        async toggleSeparator(event) {
            console.log("toggleSeparator")
            console.log(this.isCollapsed)
            console.log("toggleSeparator")

            // Подождем, чтобы Vue успел обновить isCollapsed
            await this.$nextTick();

            const collapseTarget = document.getElementById('collapseProduct' + this.dataCategory.id);

            if (!this.isCollapsed) {
                new Collapse(collapseTarget, { toggle: false }).show();
            } else {
                new Collapse(collapseTarget, { toggle: false }).hide();
            }

            this.isCollapsed = !this.isCollapsed;

            if (this.isCollapsed) {
              await this.getModels(this.dataCategory.id);
            }          
        },
    }


    // computed: {
    //     categoryName() {
    //         const categoryId = this.data_category.big_category_id;
    //         const category = this.data_big_categories.find(category => category.id === categoryId);
    //         return category ? category.name : '';
    //     },
    // },

    // created() {
    //   this.update_data_category = { ...this.category };
    // },
    // methods: {
    //     async deleteCategory() {
    //         await axios
    //             .delete(`/category/${this.data_category.id}`)
    //             .then(response => {
    //                 console.log(response.data)
    //                 this.$emit('categoryDeleted');
    //             })
    //             .catch(error => {
    //                 console.log(error)
    //             })
    //     },
    //     async updateCategory() {
    //         const formData = {
    //             name: this.update_data_category.name,
    //             slug: this.update_data_category.slug,
    //             big_category_id: this.update_data_category.big_category_id,
    //         }
    //         await axios
    //             .put(`/category/${this.data_category.id}`, formData)
    //             .then(response => {
    //                 console.log(response.data)
    //                 this.data_category = { ...this.update_data_category }
    //                 this.$emit('categoryUpdated');
    //             })
    //             .catch(error => {
    //                 console.log(error)
    //             })
    //     },
    // }
}
</script>

<style scoped>

</style>