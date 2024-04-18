<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron"
        :style="cardBodyStyles">
            
            <div class="flex-grow-1 d-flex  align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.75rem;">
                <i class="bi bi-layers"></i>
                </span>
                <span>{{ dataModel.name }}</span>
                <span class="ms-auto"><i class="bi bi-hash"></i></span>
                <span class="" style="margin-right: 1.5rem;">{{ dataModel.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button class="btn btn-icon mx-1 px-2 d-inline text-success" @click="">
                    <i class="bi bi-plus-circle" style="font-size: 18px;"></i>
                </button>
                <button class="btn btn-icon mx-1 px-2 d-inline text-dark" @click="this.$router.push({ path: '/models', query: { 'model': dataModel.id } });">
                    <i class="bi bi-layers" style="font-size: 18px;"></i>
                </button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataModel.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                
                
                <div class="modal fade" :id="'editModal_' + dataModel.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение модели</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <select v-model="updatedModel.categoryId" class="form-select py-3 mt-2 mb-3" aria-label="Default select example">
                                    <option :value="0">Категория</option>
                                    <option v-for="category in categories" :key="category.id" :value="category.id">
                                        {{ category.name }}
                                    </option>
                                </select>
                                <select v-model="updatedModel.collectionId" class="form-select py-3 mb-3" aria-label="Default select example">
                                    <option :value="0">Коллекция</option>
                                    <option v-for="collection in collections" :key="collection.id" :value="collection.id">
                                        {{ collection.name }}
                                    </option>
                                </select>
                                <select v-model="updatedModel.detailId" class="form-select py-3 mb-3" aria-label="Default select example">
                                    <option :value="0">Описание</option>
                                    <option v-for="detail in details" :key="detail.id" :value="detail.id">
                                        {{ detail.name }}
                                    </option>
                                </select>
                                <select v-model="updatedModel.sizeGuideId" class="form-select py-3 mb-3" aria-label="Default select example">
                                    <option :value="0">Размерная сетка</option>
                                    <option v-for="sideGuide in sizeGuides" :key="sideGuide.id" :value="sideGuide.id">
                                        {{ sideGuide.name }}
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
                                <button @click="updateModel()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Изменить</button>
                            </div>
                        </div>
                    </div>
                </div>

                <button @click="deleteModel()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
            </div>
        </div>
        <div class="separator-card" v-show="isCollapsed"></div>
        <div :id="'collapseProduct' + dataModel.id" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
            <div class="card-body">
                <div v-if="productLoading">
                    <div class="text-center">
                        <div v-show="productLoading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>

                <div v-if="!productLoading">
                    <div v-if="dataProducts.products.length != 0">
                        <div v-for="product in dataProducts.products" :key="product.id" class="card mb-2" style="border-radius: 1.5rem;">
                            <div class="card-body elementSecondList py-1 px-3 d-flex align-items-center" id="headingExampleTwo" aria-controls="collapseIndicatorChevron">
                                <span style="margin-right: 0.5em;">{{ product.id }}.</span>
                                <span>{{ product.color_name }}</span>
                                <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                                <button @click="deleteProduct()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                            </div>
                        </div>
                    </div>
                    <div v-else style="text-align: start;">
                        <span>Продуктов нет</span>

                    </div>
                </div>
            </div>
        </div>
    </div>
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
        details: Array,
        sizeGuides: Array,

        showErrorToast: Function,
        setLoading: Function,
        loading: Boolean,
        handleModelUpdated: Function,
        handleModelDeleted: Function,

    },
    data() {
        return {
            isCollapsed : false,

            dataModel : this.model,

            updatedModel: {
                categoryId: 0,
                collectionId: 0,
                detailId: 0,
                sizeGuideId: 0,
                name: '',
                slug: '',
            },
            
            dataProducts : {
                totalCount: 0,
                totalPages: 0,
                products: []
            },
            
            productLoading: true,
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
        this.updatedModel.categoryId = this.model.category_id === null ? 0 : this.model.category_id
        this.updatedModel.collectionId =  this.model.collection_id === null ? 0 : this.model.collection_id;
        this.updatedModel.detailId = this.model.detail_id === null ? 0 : this.model.detail_id;
        this.updatedModel.sizeGuideId = this.model.size_guide_id === null ? 0 : this.model.size_guide_id;
        this.updatedModel.name = this.model.name;
        this.updatedModel.slug = this.model.slug;
        // console.log("created")
        console.log(this.model)
        // console.log(this.updatedModel)
        // console.log("created")
    },
    methods: {
        async getProducts(modelId) {
            this.productLoading = true;
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
                this.productLoading = false;
            }
        },
        async updateModel() {
            const formData = {
                category_id: this.updatedModel.categoryId,
                collection_id: this.updatedModel.collectionId,
                detail_id: this.updatedModel.detailId,
                size_guide_id: this.updatedModel.sizeGuideId,
                name: this.updatedModel.name,
                slug: this.updatedModel.slug
            }
            this.setLoading(true);
            try {
                const response = await axios.put(`/model/${this.dataModel.id}`, formData);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleModelUpdated()
            }
        },
        async deleteModel() {
            this.setLoading(true);
            try {
                const response = await axios.delete(`/model/${this.dataModel.id}`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleModelDeleted()
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
}
</script>

<style scoped>

</style>