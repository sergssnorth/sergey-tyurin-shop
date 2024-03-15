<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron"
        :style="cardBodyStyles">
            
            <div class="flex-grow-1 d-flex  align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.5rem;">
                <i class="bi bi-person-circle"></i>
                </span>
                <span>{{ dataModel.name }}</span>
                <span class="ms-auto" style="color: grey; margin-right: 0rem;"><i class="bi bi-hash"></i></span>
                <span class="" style="color: grey; margin-right: 1.5rem;">{{ dataModel.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button class="btn btn-icon mx-1 px-2 d-inline text-dark" @click="this.$router.push({ path: '/models', query: { 'model': dataModel.id } });">
                    <i class="bi bi-layers" style="font-size: 18px;"></i>
                </button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataModel.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                
                
                <div class="modal fade" :id="'editModal_' + dataModel.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение клиента</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <select v-model="updatedModel.categoryId" class="form-select py-3" aria-label="Default select example">
                                    <option v-for="category in categories.categories" :key="category.id" :value="category.id">
                                        {{ category.name }}
                                    </option>
                                </select>
                                <select v-model="updatedModel.collectionId" class="form-select py-3" aria-label="Default select example">
                                    <option v-for="collection in collections.collections" :key="collection.id" :value="collection.id">
                                        {{ collection.name }}
                                    </option>
                                </select>
                                <div class="form-floating mb-3">
                                <input type="text" class="form-control" placeholder="name@example.com" v-model="updatedModel.name">
                                <label for="floatingInput">Имя</label>
                                </div>
                                <div class="form-floating mb-3">
                                <input type="text" class="form-control" placeholder="Password" v-model="updatedModel.slug">
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
        <div :id="'collapseProduct' + dataModel.id" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
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
                        <div v-for="model in dataModels.models" :key="model.id" class="d-flex align-items-center">
                            <span style="margin-right: 0.5em;">{{ model.id }}.</span>
                            <span>{{ model.name }}</span>
                            <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                            <button @click="deleteBigmodel()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                        </div>
                    </div>
                    <div v-else>
                        <span>Моделей нет</span>
                    </div>
                </div>
                
            </div>
        </div>
    </div>
    <!-- <div class="card mb-1">
        <div class="card-body py-1 px-3">
        <div class="d-flex align-items-center">
            <span>{{ data_model.name }} </span>
            
            
            <span class="ms-auto" style="color: grey; margin-right: 0.5rem;"><i class="bi bi-boxes"></i></span>
            <span class="" style="color: grey; margin-right: 0.5rem;"> {{ TreeBigmodel }}</span>
            <span class="" style="color: grey; margin-right: 0.5rem;"><i class="bi bi-arrow-right"></i></span>
            <span class="" style="color: grey; margin-right: 1.5rem;"> {{ Treemodel }}</span>
            <span class="" style="color: grey; margin-right: 0.5rem;"><i class="bi bi-gem"></i></span>
            <span class="" style="color: grey; margin-right: 1.5rem;"> {{ TreeCollection }}</span>

            <div class="vr" style="margin-right: 1.15rem;"></div>
            <button @click="$router.push(`/product/${this.data_model.id}`)"  class="btn btn-icon d-inline px-2"><i class="bi bi bi-box-seam"></i></button>
            
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
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="Password" v-model="update_data_model.description">
                      <label for="floatingPassword">Описание</label>
                    </div>
                    <select v-model="update_data_model.big_model_id" class="form-select py-3 mb-3" aria-label="Default select example">
                        <option :value="0">Выберите раздел</option>
                        <option v-for="big_model in data_big_categories" :key="big_model.id" :value="big_model.id">
                            {{ big_model.name }}
                        </option>
                    </select>
                    <select v-model="update_data_model.model_id" class="form-select py-3 mb-3" aria-label="Default select example">
                        <option :value="0">Выберите категорию</option>
                        <option v-for="model in data_categories" :key="model.id" :value="model.id">
                            {{ model.name }}
                        </option>
                    </select>
                    <select v-model="update_data_model.collection_id" class="form-select py-3 mb-3" aria-label="Default select example">
                        <option :value="0">Выберите коллекцию</option>
                        <option v-for="collection in data_collections" :key="collection.id" :value="collection.id">
                            {{ collection.name }}
                        </option>
                    </select>
                  </div>
                  <div class="modal-footer ">
                    <button @click="updatemodel()" type="button" class="btn btn-primary" data-bs-dismiss="modal">Изменить</button>
                  </div>
                </div>
              </div>
            </div>

            <button @click="deletemodel()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
        </div>
        </div>
    </div> -->
</template>

<script>
import axios from 'axios'
import { Collapse } from 'bootstrap/dist/js/bootstrap.js'

export default {
    name: 'ListModels',
    props: {
        model: Object,
        categories: Array,
        collections: Array,
    },
    data() {
        return {
            isCollapsed : false,

            dataModel : this.model,

            updatedModel: {
                categoryId: 0,
                collectionId: 0,
                name: '',
                slug: '',
            },
            
            dataProducts : {
                totalCount: 0,
                totalPages: 0,
                products: []
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
        this.updatedModel = { ...this.model };
    },
    methods: {
        async getProducts(modelId) {
            this.loading = true;
            const params = { model_id: modelId,
                            offset: 0,
                            limit: 20 }
            try {
                const response = await axios.get(`/products`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, products } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    products: products
                };
                this.dataProducts = transformedData;
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

            const collapseTarget = document.getElementById('collapseProduct' + this.dataModel.id);

            if (!this.isCollapsed) {
                new Collapse(collapseTarget, { toggle: false }).show();
            } else {
                new Collapse(collapseTarget, { toggle: false }).hide();
            }

            this.isCollapsed = !this.isCollapsed;

            if (this.isCollapsed) {
              await this.getProducts(this.dataModel.id);
            }          
        },
    }

    // props: {
    //     model: Object,
    //     big_categories: Array,
    //     categories: Array,
    //     collections: Array
    // },
    // data() {
    //     return {
    //         data_model: this.model,
    //         data_big_categories: this.big_categories,
    //         data_categories: this.categories,
    //         data_collections: this.collections,

    //         update_data_model: {
    //             name: '',
    //             slug: '',
    //             description: '',
    //             big_model_id: 0,
    //             model_id: 0,
    //             collection_id: 0,
    //             FilterId: '',
    //         },
    //     }
    // },
    // computed: {
    //     TreeBigmodel() {
    //         console.log("TreeBigmodel")
    //         const bigmodelId = this.data_model.big_model_id
    //         const bigmodel = this.data_big_categories.find(model => model.id == bigmodelId)  

    //         return bigmodel ? bigmodel.name : ''; 
    //     },
    //     Treemodel() {
    //         console.log("Treemodel")
    //         const modelId = this.data_model.model_id
    //         const model = this.data_categories.find(model => model.id == modelId)  

    //         return model ? model.name : ''; 
    //     },
    //     TreeCollection() {
    //         console.log("TreeCollection")
    //         const collectionId = this.data_model.collection_id
    //         const collection = this.data_collections.find(collection => collection.id == collectionId)

    //         return collection ? collection.name : ''; 
    //     }
    // },
    // created() {
    //   this.update_data_model = { ...this.data_model };
    // },
    // methods: {
    //     async deleteModel() {
    //         await axios
    //             .delete(`/model/${this.data_model.id}`)
    //             .then(response => {
    //                 console.log(response.data)
    //                 this.$emit('modelDeleted');
    //             })
    //             .catch(error => {
    //                 console.log(error)
    //             })
    //     },
    //     async updateModel() {
    //         const formData = {
    //             name: this.update_data_model.name,
    //             slug: this.update_data_model.slug,
    //             description: this.update_data_model.description,
    //             model_id: this.update_data_model.model_id,
    //             collection_id: this.update_data_model.collection_id
    //         }
    //         await axios
    //             .put(`/model/${this.data_model.id}`, formData)
    //             .then(response => {
    //                 console.log(response.data)
    //                 this.data_model = { ...this.update_data_model}
    //                 this.$emit('modelUpdated');
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