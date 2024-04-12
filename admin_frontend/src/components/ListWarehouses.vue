<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron"
        :style="cardBodyStyles">
            
            <div class="flex-grow-1 d-flex  align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.5rem;">
                <i class="bi bi-person-circle"></i>
                </span>
                <span>{{ dataWarehouse.name }}</span>
                <span class="ms-auto" style="color: grey; margin-right: 0rem;"><i class="bi bi-hash"></i></span>
                <span class="" style="color: grey; margin-right: 1.5rem;">{{ dataWarehouse.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button class="btn btn-icon mx-1 px-2 d-inline text-dark" @click="this.$router.push({ path: '/models', query: { 'model': dataWarehouse.id } });">
                    <i class="bi bi-layers" style="font-size: 18px;"></i>
                </button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataWarehouse.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                
                
                <div class="modal fade" :id="'editModal_' + dataWarehouse.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение модели</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="updatedModel.name">
                                    <label for="floatingInput">Имя</label>
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
        <div :id="'collapseWarehouse' + dataWarehouse.id" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
            <div class="card-body">
                <div v-if="warehouseElementsLoading">
                    <div class="text-center">
                        <div v-show="warehouseElementsLoading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>

                <div v-if="!warehouseElementsLoading">
                    <div v-if="dataWarehouseElements.warehouseElements.length != 0">
                        <div v-for="warehouseElement in dataWarehouseElements.warehouseElements" :key="warehouseElement.id" class="card mb-2" style="border-radius: 1.5rem;">
                            <div class="card-body elementSecondList py-1 px-3 d-flex align-items-center" id="headingExampleTwo" aria-controls="collapseIndicatorChevron">
                                <span style="margin-right: 0.5em;">{{ warehouseElement.id }}.</span>
                                <span>{{ warehouseElement.color_name }}</span>
                                <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                                <button @click="deleteWarehouseElement()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                            </div>
                        </div>
                        <div class="d-flex align-items-center mt-3">
                            <button class="btn btn-outline-success px-3" style="border-radius: 1.25rem;">
                                <i class="bi bi-layers" style="margin-right: 0.5em;"></i>
                                <span>Добавить продукт</span>
                            </button>
                        </div>
                    </div>
                    <div v-else style="text-align: start;">
                        <span>Продуктов нет</span>
                        <div class="d-flex align-items-center mt-3">
                            <button class="btn btn-outline-success px-3" style="border-radius: 1.25rem;">
                                <i class="bi bi-layers" style="margin-right: 0.5em;"></i>
                                <span>Добавить продукт</span>
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
    name: 'ListWarehouses',
    props: {
        warehouse: Object,

        showErrorToast: Function,
        setLoading: Function,
        loading: Boolean,
        handleWarehouseUpdated: Function,
        handleWarehouseDeleted: Function,

    },
    data() {
        return {
            isCollapsed : false,

            dataWarehouse : this.warehouse,

            updatedWarehouse: {
                name: '',
            },
            
            dataWarehouseElements : {
                totalCount: 0,
                totalPages: 0,
                warehouseElements: []
            },
            
            warehouseElementsLoading: true,
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
        this.updatedWarehouse.name = this.warehouse.name === null ? "" : this.model.category_id
    },
    methods: {
        async getWarehouseElements(warehouseId) {
            this.warehouseElementsLoading = true;
            const params = { warehouse_id: warehouseId,
                            offset: 0,
                            limit: 20 }
            try {
                const response = await axios.get(`/warehouse-elements`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, warehouse_elements } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    warehouseElements: warehouse_elements
                };
                this.dataWarehouseElements = transformedData;
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.warehouseElementsLoading = false;
            }
        },

        
        async updateWarehouse() { 
            const formData = {
                name: this.updatedWarehouse.name,
            }
            this.setLoading(true);
            try {
                const response = await axios.put(`/warehouse/${this.dataWarehouse.id}`, formData);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleWarehouseUpdated()
            }
        },
        async deleteWarehouse() {
            this.setLoading(true);
            try {
                const response = await axios.delete(`/warehouse/${this.dataWarehouse.id}`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleWarehouseDeleted()
            }
        },

        async toggleSeparator(event) {
            console.log("toggleSeparator")
            console.log(this.isCollapsed)
            console.log("toggleSeparator")

            // Подождем, чтобы Vue успел обновить isCollapsed
            await this.$nextTick();

            const collapseTarget = document.getElementById('collapseWarehouse' + this.dataWarehouse.id);

            if (!this.isCollapsed) {
                new Collapse(collapseTarget, { toggle: false }).show();
            } else {
                new Collapse(collapseTarget, { toggle: false }).hide();
            }

            this.isCollapsed = !this.isCollapsed;

            if (this.isCollapsed) {
              await this.getWarehouseElements(this.dataWarehouse.id);
            }          
        },
    }
}
</script>

<style scoped>

</style>