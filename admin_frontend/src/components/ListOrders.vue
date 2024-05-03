<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron"
        :style="cardBodyStyles">
            
            <div class="flex-grow-1 d-flex  align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.75rem;">
                    <i class="bi bi-box-seam"></i>
                </span>
                <span>{{ dataOrder.name }}</span>
                <span class="ms-auto"><i class="bi bi-hash"></i></span>
                <span class="" style="margin-right: 1.5rem;">{{ dataOrder.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button class="btn btn-icon mx-1 px-2 d-inline text-success" @click="">
                    <i class="bi bi-plus-circle" style="font-size: 18px;"></i>
                </button>

                <button class="btn btn-icon mx-1 px-2 d-inline text-dark" @click="this.$router.push({ path: '/models', query: { 'order': dataOrder.id } });">
                    <i class="bi bi-layers" style="font-size: 18px;"></i>
                </button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataOrder.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>  
                
                <div class="modal fade" :id="'editModal_' + dataOrder.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение категории</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mb-3">
                                <input type="text" class="form-control" placeholder="name@example.com" v-model="updatedOrder.name">
                                <label for="floatingInput">Имя</label>
                                </div>
                                <div class="form-floating mb-3">
                                <input type="text" class="form-control" placeholder="Password" v-model="updatedOrder.slug">
                                <label for="floatingPassword">Слаг</label>
                                </div>
                            </div>
                            <div class="modal-footer ">
                                <button @click="updateOrder()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Изменить</button>
                            </div>
                        </div>
                    </div>
                </div>

                <button @click="deleteOrder()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
            </div>
        </div>
        <div class="separator-card" v-show="isCollapsed"></div>
        <div :id="'collapseProduct' + dataOrder.id" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
            <div class="card-body">
                <div v-if="orderElementsLoading">
                    <div class="text-center">
                        <div v-show="orderElementsLoading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>

                <div v-if="!orderElementsLoading">
                    <div v-if="dataOrderElements.orderElements.length != 0">
                        <div v-for="orderElement in dataOrderElements.orderElements" :key="orderElement.id" class="card mb-2" style="border-radius: 1.5rem;">
                            <div class="card-body elementSecondList py-1 px-3 d-flex align-items-center" id="headingExampleTwo" aria-controls="collapseIndicatorChevron">
                                <span style="margin-right: 0.5em;">{{ orderElement.id }}.</span>
                                <span style="margin-right: 1.5rem;">{{ orderElement.model_name }}</span>

                                <span style="margin-right: 0.25rem;"><i class="bi bi-file-code-fill"></i></span>
                                <span>{{ orderElement.size_name }}</span>

                                <span class="ms-auto" style="margin-right: 1rem;">{{ orderElement.price}} ₽</span>
                                <span style="margin-right: 1rem;">{{ orderElement.count}} шт.</span>
                                <div class="vr" style="margin-right: 1.15rem;"></div>
                                <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                                <button @click="deletePriceListElement()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                            </div>
                        </div>
                        
                    </div>
                    <div v-else style="text-align: start;">
                        <span>Элементов заказа нет</span>
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
    name: 'ListOrders',
    props: {
        order: Object,
        users: Array,
        employees: Array,
        orderStatuses: Array,

        showErrorToast: Function,
        setLoading: Function,
        loading: Boolean,
        handleOrderUpdated: Function,
        handleOrderDeleted: Function,
    },
    data() {
        return {
            isCollapsed : false,
            
            dataOrder : this.order,

            updatedOrder: {
                userId: null,
                name: "",
                sname: "",
                lname: "",
                phone: "",
                email: "",
                region: "",
                city: "",
                postal_code: "",
                employeeId: 0,
                orderStatusId: 0,
            },
            
            dataOrderElements : {
                totalCount: 0,
                totalPages: 0,
                orderElements: []
            },
            
            orderElementsLoading: true,
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
        this.updatedOrder = { ...this.order };
    },
    methods: {
        async getOrderElements(orderId) {
            this.orderElementsLoading = true;
            const params = { order_id: orderId,
                            offset: 0,
                            limit: 20 }
            try {
                const response = await axios.get(`/order-elements`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, order_elements } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    orderElements: order_elements
                };
                this.dataOrderElements = transformedData;
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.orderElementsLoading = false;
            }
        },
        async updateOrder() {
            const formData = {
                name: this.updatedOrder.name,
                slug: this.updatedOrder.slug
            }
            this.setLoading(true);
            try {
                const response = await axios.put(`/order/${this.dataOrder.id}`, formData);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleOrderUpdated()
            }
        },
        async deleteOrder() {
            this.setLoading(true);
            try {
                const response = await axios.delete(`/order/${this.dataOrder.id}`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleOrderDeleted()
            }
        },
        async toggleSeparator(event) {
            console.log("toggleSeparator")
            console.log(this.isCollapsed)
            console.log("toggleSeparator")

            // Подождем, чтобы Vue успел обновить isCollapsed
            await this.$nextTick();

            const collapseTarget = document.getElementById('collapseProduct' + this.dataOrder.id);

            if (!this.isCollapsed) {
                new Collapse(collapseTarget, { toggle: false }).show();
            } else {
                new Collapse(collapseTarget, { toggle: false }).hide();
            }

            this.isCollapsed = !this.isCollapsed;

            if (this.isCollapsed) {
              await this.getOrderElements(this.dataOrder.id);
            }          
        },
    }
}
</script>
