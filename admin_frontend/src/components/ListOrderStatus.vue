<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron"
        :style="cardBodyStyles">
            
            <div class="flex-grow-1 d-flex  align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.75rem;">
                <i class="bi bi-file-check"></i>
                </span>
                <span>{{ dataOrderStatus.name }}</span>
                <span class="ms-auto"><i class="bi bi-hash"></i></span>
                <span class="" style="margin-right: 1.5rem;">{{ dataOrderStatus.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button class="btn btn-icon mx-1 px-2 d-inline text-success" @click="">
                    <i class="bi bi-plus-circle" style="font-size: 18px;"></i>
                </button>

                <button class="btn btn-icon mx-1 px-2 d-inline text-dark" @click="this.$router.push({ path: '/orders', query: { 'orderStatus': dataOrderStatus.id } });">
                    <i class="bi bi-layers" style="font-size: 18px;"></i>
                </button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataOrderStatus.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                
                
                <div class="modal fade" :id="'editModal_' + dataOrderStatus.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение статуса заказа</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="updatedOrderStatus.name">
                                    <label for="floatingInput">Имя</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" placeholder="Password" v-model="updatedOrderStatus.slug">
                                    <label for="floatingPassword">Слаг</label>
                                </div>
                            </div>
                            <div class="modal-footer ">
                                <button @click="updateOrderStatus()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Изменить</button>
                            </div>
                        </div>
                    </div>
                </div>

                <button @click="deleteOrderStatus()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
            </div>
        </div>
        <div class="separator-card" v-show="isCollapsed"></div>
        <div :id="'collapseProduct' + dataOrderStatus.id" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
            <div class="card-body">
                <div v-if="orderLoading">
                    <div class="text-center">
                        <div v-show="orderLoading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>

                <div v-if="!orderLoading">
                    <div v-if="dataOrders.orders.length != 0">
                        <div v-for="model in dataOrders.orders" :key="orderStatus.id" class="d-flex align-items-center">
                            <span style="margin-right: 0.5em;">{{ model.id }}.</span>
                            <span>{{ model.name }}</span>
                            <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                            <button @click="deleteBigCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
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
            <span>{{ data_order_status.name }}</span>
            <button @click="$router.push(`/orders`)" class="btn btn-icon d-inline ms-auto px-2"><i class="bi bi bi-box-seam"></i></button>
            
            <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + data_order_status.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
            <div class="modal fade" :id="'editModal_' + data_order_status.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                <div class="modal-content">
                  <div class="modal-header text-center">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Изменить статус заказа, {{ data_order_status.name }}</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="name@example.com" v-model="update_data_order_status.name">
                      <label for="floatingInput">Имя</label>
                    </div>
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="Password" v-model="update_data_order_status.slug">
                      <label for="floatingPassword">Слаг</label>
                    </div>
                  </div>
                  <div class="modal-footer">
                    <button @click="updateOrderStatus()" type="button" class="btn btn-primary" data-bs-dismiss="modal">Изменить</button>
                  </div>
                </div>
              </div>
            </div>

            <button @click="deleteOrderStatus()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
        </div>
        </div>
    </div> -->
</template>

<script>
import axios from 'axios'
import { Collapse } from 'bootstrap/dist/js/bootstrap.js'

export default {
    name: 'ListOrderStatus',
    props: {
        orderStatus: Object,
        showErrorToast: Function,
        setLoading: Function,
        loading: Boolean,
        handleOrderStatusUpdated: Function,
        handleOrderStatusDeleted: Function,
    },
    data() {
        return {
            isCollapsed : false,
            
            dataOrderStatus : this.orderStatus,

            updatedOrderStatus: {
                name: '',
                slug: '',
            },
            
            dataOrders : {
                totalCount: 0,
                totalPages: 0,
                orders: []
            },
            
            orderLoading: true,
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
        this.updatedOrderStatus = { ...this.orderStatus };
    },
    methods: {
        async getOrders(orderStatusId) {
            this.orderLoading = true;
            const params = {order_status_id: orderStatusId,
                            offset: 0,
                            limit: 100 }
            try {
                const response = await axios.get(`/orders`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, orders } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    orders: orders
                };
                this.dataOrders = transformedData;
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.orderLoading = false;
            }
        },
        async updateOrderStatus() {
            const formData = {
                name: this.updatedOrderStatus.name,
                slug: this.updatedOrderStatus.slug,
            }
            this.setLoading(true);
            try {
                const response = await axios.put(`/order-status/${this.dataOrderStatus.id}`, formData);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleOrderStatusUpdated()
            }
        },
        async deleteOrderStatus() {
            this.setLoading(true); // Включить индикатор загрузки
            try {
                const response = await axios.delete(`/order-status/${this.dataOrderStatus.id}`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleOrderStatusDeleted()
            }
        },
        async toggleSeparator(event) {
            console.log("toggleSeparator")
            console.log(this.isCollapsed)
            console.log("toggleSeparator")

            // Подождем, чтобы Vue успел обновить isCollapsed
            await this.$nextTick();

            const collapseTarget = document.getElementById('collapseProduct' + this.dataOrderStatus.id);

            if (!this.isCollapsed) {
                new Collapse(collapseTarget, { toggle: false }).show();
            } else {
                new Collapse(collapseTarget, { toggle: false }).hide();
            }

            this.isCollapsed = !this.isCollapsed;

            if (this.isCollapsed) {
              await this.getOrders(this.dataOrderStatus.id);
            }          
        },
    }
    // props: {
    //     order_status: Object,
    // },
    // data() {
    //     return {
    //         data_order_status: this.order_status,
    //         update_data_order_status: {
    //             name: '',
    //             slug: '',
    //         },
    //     }
    // },
    // created() {
    //   this.update_data_order_status = { ...this.order_status };
    // },
    // methods: {
    //     async deleteOrderStatus() {
    //         await axios
    //             .delete(`/order-status/${this.data_order_status.id}`)
    //             .then(response => {
    //                 console.log(response.data)
    //                 this.$emit('orderStatusDeleted');
    //             })
    //             .catch(error => {
    //                 console.log(error)
    //             })
    //     },
    //     async updateOrderStatus() {
    //         const formData = {
    //             name: this.update_data_order_status.name,
    //             slug: this.update_data_order_status.slug,
    //         }
    //         try {
    //             await axios
    //             .put(`/order-status/${this.data_order_status.id}`, formData)
    //             .then(response => {
    //                 console.log(response.data)
    //                 this.data_order_status = { ...this.update_data_order_status }
    //                 this.$emit('orderStatusUpdated');
    //             })
    //         } catch (error) {
    //             console.log(error);
    //         }
    //     },
    // }
}
</script>

<style scoped>

</style>