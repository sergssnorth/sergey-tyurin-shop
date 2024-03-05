<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron"
        :style="cardBodyStyles">
            
            <div class="flex-grow-1 d-flex  align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.5rem;">
                <i class="bi bi-person-circle"></i>
                </span>
                <span>{{ dataClient.name }}</span>
                <span class="ms-auto" style="color: grey; margin-right: 0rem;"><i class="bi bi-hash"></i></span>
                <span class="" style="color: grey; margin-right: 1.5rem;">{{ dataClient.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button data-bs-toggle="modal" data-bs-target="#edi" class="btn btn-icon d-inline text-success px-2"><i class="bi bi-bag-plus"></i></button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataClient.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                
                
                <div class="modal fade" :id="'editModal_' + dataClient.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение клиента</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mb-3">
                                <input type="text" class="form-control" placeholder="name@example.com" v-model="updatedClient.name">
                                <label for="floatingInput">Имя</label>
                                </div>
                                <div class="form-floating mb-3">
                                <input type="text" class="form-control" placeholder="Password" v-model="updatedClient.slug">
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
        <div :id="'collapseProduct' + dataClient.id" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
            <div class="card-body">
                <div v-if="loading">
                    <div class="text-center">
                        <div v-show="loading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>

                <div v-if="!loading">
                    <div v-if="dataOrders.length != 0">
                        <div v-for="order in dataOrders" :key="order.id" class="d-flex align-items-center">
                            <span style="margin-right: 0.5em;">{{ order.id }}.</span>
                            <span>{{ order.name }}</span>
                            <span>{{ order.status }}</span>
                            <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                            <button @click="deleteBigCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                        </div>
                    </div>
                    <div v-else>
                        <span>Заказов нет</span>
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
    name: 'ListClients',
    props: {
        client: Object,
        orders: Array,
        showErrorToast: Function,
    },
    data() {
        return {
            isCollapsed : false,
            
            dataClient : this.client,
            updatedClient: {
                name: '',
                slug: '',
            },
            
            dataOrders : [],
            
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
        this.updatedClient = { ...this.client };
    },
    methods: {
        async getOrders(client_id) {
            this.loading = true;
            const params = { client_id: client_id,
                            offset: 0,
                            limit: 5 }
            try {
                const response = await axios.get(`/orders`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const orders = response.data.orders ? response.data.orders : [];
                return response.data.orders;
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.loading = false;
            }
        },

        async loadClientOrders() {
            if (this.isCollapsed) {
                try {
                    const orders = await this.getOrders(this.dataClient.id);
                    this.dataOrders = orders;
                } catch (error) {
                    console.error("Произошла ошибка при получении заказов:", error);
                } finally {
                    this.loading = false;
                }
            }
        },

        async deleteClient() {
            await axios
                .delete(`/client/${this.dataClient.id}`)
                .then(response => {
                    console.log(response.data)
                    this.$emit('clientDeleted', this.dataClient.id);
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async updateClient() {
            const formData = {
                name: this.updatedClient.name,
                slug: this.updatedClient.slug
            }
            await axios
                .put(`/client/${this.dataClient.id}`, formData)
                .then(response => {
                    console.log(response.data)
                    this.$emit('clientUpdated', this.dataClient.id);
                    
                })
                .catch(error => {
                    console.log(error)
                })
        },

        async toggleSeparator(event) {
            console.log("toggleSeparator")
            console.log(this.isCollapsed)
            console.log("toggleSeparator")

            // Подождем, чтобы Vue успел обновить isCollapsed
            await this.$nextTick();

            const collapseTarget = document.getElementById('collapseProduct' + this.dataClient.id);

            if (!this.isCollapsed) {
                // Развернуть коллапс
                new Collapse(collapseTarget, { toggle: false }).show();
            } else {
                // Свернуть коллапс
                new Collapse(collapseTarget, { toggle: false }).hide();
            }
            this.isCollapsed = !this.isCollapsed;
            await this.loadClientOrders();
            this.loading = false;
        },
    }
}
</script>
