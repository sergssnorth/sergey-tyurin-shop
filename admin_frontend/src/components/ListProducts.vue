<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron"
        :style="cardBodyStyles">
            
            <div class="flex-grow-1 d-flex  align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.5rem;">
                <i class="bi bi-person-circle"></i>
                </span>
                <span>{{ dataProduct.color_name }}</span>
                <span class="ms-auto" style="color: grey; margin-right: 0rem;"><i class="bi bi-hash"></i></span>
                <span class="" style="color: grey; margin-right: 1.5rem;">{{ dataProduct.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button class="btn btn-icon mx-1 px-2 d-inline text-dark" @click="this.$router.push({ path: '/models', query: { 'model': dataProduct.id } });">
                    <i class="bi bi-layers" style="font-size: 18px;"></i>
                </button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataProduct.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                
                
                <div class="modal fade" :id="'editModal_' + dataProduct.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение продукта</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <select v-model="updatedProduct.modelId" class="form-select py-3 mt-2 mb-3" aria-label="Default select example">
                                    <option :value="0">Модель</option>
                                    <option v-for="model in models" :key="model.id" :value="model.id">
                                        {{ model.name }}
                                    </option>
                                </select>
                                <select v-model="updatedProduct.colorId" class="form-select py-3 mb-3" aria-label="Default select example">
                                    <option :value="0">Коллекция</option>
                                    <option v-for="color in colors" :key="color.id" :value="color.id">
                                        {{ color.name }}
                                    </option>
                                </select>
                            </div>
                            <div class="modal-footer ">
                                <button @click="updateProduct()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Изменить</button>
                            </div>
                        </div>
                    </div>
                </div>

                <button @click="deleteProduct()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
            </div>
        </div>
        <div class="separator-card" v-show="isCollapsed"></div>
        <div :id="'collapseProduct' + dataProduct.id" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
            <div class="card-body">
                <div v-if="productInstancesLoading">
                    <div class="text-center">
                        <div v-show="productInstancesLoading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>

                <div v-if="!productInstancesLoading">
                    <div v-if="dataProductInstances.productInstances.length != 0">
                        <div v-for="productInstance in dataProductInstances.productInstances" :key="productInstance.id" class="card mb-2" style="border-radius: 1.5rem;">
                            <div class="card-body elementSecondList py-1 px-3 d-flex align-items-center" id="headingExampleTwo" aria-controls="collapseIndicatorChevron">
                                <span style="margin-right: 0.5em;">{{ productInstance.id }}.</span>
                                <span>{{ productInstance.size_name }}</span>
                                <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                                <button @click="deleteProduct()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                            </div>
                        </div>
                        <div class="d-flex align-items-center mt-3">
                            <button class="btn btn-outline-success px-3" style="border-radius: 1.25rem;">
                                <i class="bi bi-layers" style="margin-right: 0.5em;"></i>
                                <span>Добавить экземляр продукта</span>
                            </button>
                        </div>
                    </div>
                    <div v-else style="text-align: start;">
                        <span>Экземляров продукта нет</span>
                        <div class="d-flex align-items-center mt-3">
                            <button class="btn btn-outline-success px-3" style="border-radius: 1.25rem;">
                                <i class="bi bi-layers" style="margin-right: 0.5em;"></i>
                                <span>Добавить экземляр продукта</span>
                            </button>
                        </div>
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
    name: 'ListProducts',
    props: {
        product: Object,
        models: Array,
        colors: Array,

        showErrorToast: Function,
        setLoading: Function,
        loading: Boolean,
        handleProductUpdated: Function,
        handleProductDeleted: Function,

    },
    data() {
        return {
            isCollapsed : false,

            dataProduct : this.product,

            updatedProduct: {
                modelId: 0,
                colorId: 0,
            },
            
            dataProductInstances : {
                totalCount: 0,
                totalPages: 0,
                productInstances: []
            },
            
            productInstancesLoading: true,
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
        this.updatedProduct.modelId = this.product.model_id === null ? 0 : this.product.model_id;
        this.updatedProduct.colorId =  this.product.color_id === null ? 0 : this.product.color_id;
    },
    methods: {
        async getProductInstances(productId) {
            this.productInstancesLoading = true;
            const params = {product_id: productId,
                            offset: 0,
                            limit: 20 }
            try {
                const response = await axios.get(`/product-instances`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, product_instances } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    productInstances: product_instances
                };
                this.dataProductInstances = transformedData;
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.productInstancesLoading = false;
            }
        },
        async updateProduct() {
            const formData = {
                category_id: this.updatedModel.categoryId,
                collection_id: this.updatedModel.collectionId,
            }
            this.setLoading(true);
            try {
                const response = await axios.put(`/model/${this.dataProduct.id}`, formData);
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
        async deleteProduct() {
            this.setLoading(true);
            try {
                const response = await axios.delete(`/model/${this.dataProduct.id}`);
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

            const collapseTarget = document.getElementById('collapseProduct' + this.dataProduct.id);

            if (!this.isCollapsed) {
                new Collapse(collapseTarget, { toggle: false }).show();
            } else {
                new Collapse(collapseTarget, { toggle: false }).hide();
            }

            this.isCollapsed = !this.isCollapsed;

            if (this.isCollapsed) {
              await this.getProductInstances(this.dataProduct.id);
            }          
        },
    }
}
</script>