<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron"
        :style="cardBodyStyles">
            
            <div class="flex-grow-1 d-flex align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.75rem;">
                <i class="bi bi-currency-dollar"></i>
                </span>
                <span>{{ dataPriceList.name }}</span>
                <span class="ms-auto"><i class="bi bi-hash"></i></span>
                <span class="" style="margin-right: 1.5rem;">{{ dataPriceList.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button class="btn btn-icon mx-1 px-2 d-inline text-success" @click="">
                    <i class="bi bi-plus-circle" style="font-size: 18px;"></i>
                </button>
                <button class="btn btn-icon mx-1 px-2 d-inline text-dark" @click="this.$router.push({ path: '/models', query: { 'model': dataPriceList.id } });">
                    <i class="bi bi-layers" style="font-size: 18px;"></i>
                </button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataPriceList.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                
                
                <div class="modal fade" :id="'editModal_' + dataPriceList.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение склада</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="updatedPriceList.name">
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
        <div :id="'collapsePriceList' + dataPriceList.id" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
            <div class="card-body">
                <div v-if="priceListElementsLoading">
                    <div class="text-center">
                        <div v-show="priceListElementsLoading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>
                
                <div v-if="!priceListElementsLoading">
                    <div v-if="dataPriceListElements.priceListElements.length != 0">
                        <div v-for="priceListElement in dataPriceListElements.priceListElements" :key="priceListElement.id" class="card mb-2" style="border-radius: 1.5rem;">
                            <div class="card-body elementSecondList py-1 px-3 d-flex align-items-center" id="headingExampleTwo" aria-controls="collapseIndicatorChevron">
                                <span style="margin-right: 0.5em;">{{ priceListElement.id }}.</span>
                                <span style="margin-right: 1.5rem;">{{ priceListElement.model_name }}</span>

                                <span style="margin-right: 0.25rem;"><i class="bi bi-file-code-fill"></i></span>
                                <span>{{ priceListElement.size_name }}</span>

                                <span class="ms-auto" style="margin-right: 1rem;">{{ priceListElement.price}} ₽</span>
                                <div class="vr" style="margin-right: 1.15rem;"></div>
                                <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                                <button @click="deletePriceListElement()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
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
    name: 'ListPriceLists',
    props: {
        priceList: Object,

        showErrorToast: Function,
        setLoading: Function,
        loading: Boolean,
        handlePriceListUpdated: Function,
        handlePriceListDeleted: Function,

    },
    data() {
        return {
            isCollapsed : false,

            dataPriceList : this.priceList,

            updatedPriceList: {
                name: '',
            },
            
            dataPriceListElements : {
                totalCount: 0,
                totalPages: 0,
                priceListElements: []
            },
            
            priceListElementsLoading: true,
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
        this.updatedPriceList.name = this.priceList.name === null ? "" : this.priceList.name
    },
    methods: {
        async getPriceListElements(priceListId) {
            this.priceListElementsLoading = true;
            const params = { price_list_id: priceListId,
                            offset: 0,
                            limit: 20 }
            try {
                const response = await axios.get(`/price-list-elements`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, price_list_elements } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    priceListElements: price_list_elements
                };
                this.dataPriceListElements = transformedData;
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.priceListElementsLoading = false;
            }
        },

        
        async updatePriceList() { 
            const formData = {
                name: this.updatedPriceList.name,
            }
            this.setLoading(true);
            try {
                const response = await axios.put(`/price-list/${this.dataPriceList.id}`, formData);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handlePriceListUpdated()
            }
        },
        async deletePriceList() {
            this.setLoading(true);
            try {
                const response = await axios.delete(`/price-list/${this.dataPriceList.id}`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handlePriceListDeleted()
            }
        },

        async toggleSeparator(event) {
            console.log("toggleSeparator")
            console.log(this.isCollapsed)
            console.log("toggleSeparator")

            // Подождем, чтобы Vue успел обновить isCollapsed
            await this.$nextTick();

            const collapseTarget = document.getElementById('collapsePriceList' + this.dataPriceList.id);

            if (!this.isCollapsed) {
                new Collapse(collapseTarget, { toggle: false }).show();
            } else {
                new Collapse(collapseTarget, { toggle: false }).hide();
            }

            this.isCollapsed = !this.isCollapsed;

            if (this.isCollapsed) {
              await this.getPriceListElements(this.dataPriceList.id);
            }          
        },
    }
}
</script>

<style scoped>

</style>