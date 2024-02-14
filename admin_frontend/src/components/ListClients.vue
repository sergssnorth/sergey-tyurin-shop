<template>
    <div class="card mb-1">
            <a @click="toggleSeparator" :data-bs-target="'#collapseProduct' + data_client.id" class="card-body py-1 px-3 d-flex align-items-center" id="headingExampleTwo" data-bs-toggle="collapse" aria-expanded="false" aria-controls="collapseIndicatorChevron">
                <span>{{ data_client.name }}</span>
                
                <button  data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>

                <button @click="deleteBigCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
            </a>
            <div class="separator-card" v-show="isCollapsed"></div>
            <div :id="'collapseProduct' + data_client.id" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
                <div class="card-body">
                    <div class="text-center">
                        <div v-show="loading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                    <div v-if="!loading">
                        <div v-for="order in client_orders" :key="order.id" class="d-flex align-items-center">
                            <span style="margin-right: 0.5em;">{{ order.id }}.</span>
                            <span>{{ order.name }}</span>
                            <span>{{ order.status }}</span>
                            <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                            <button @click="deleteBigCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                        </div>
                        <div class="d-flex align-items-center mt-3">
                            <button class="btn btn-outline-success"><i class="bi bi-plus-circle" style="margin-right: 0.5em;"></i>Добавить размер</button>
                        </div>
                    </div>
                </div>
            </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ListClients',
    props: {
        client: Object,
    },
    data() {
        return {
            isCollapsed : false,
            data_client : this.client,
            client_orders : [],
            loading : true,
        }
    },
    methods: {
        async getOrders(client_id) {
            const params = { client_id: client_id}
            try {
                const response = await axios.get(`/orders`, { params });
                return response.data;  // Вернуть данные из успешного запроса
            } catch (error) {
                console.error(error);
                throw error;  // Перехватывать и пробрасывать ошибку
            }
        },

        async loadClientOrders() {
            if (this.isCollapsed) {
                try {
                    const orders = await this.getOrders(this.data_client.id);
                    this.client_orders = orders;
                } catch (error) {
                    console.error("Произошла ошибка при получении заказов:", error);
                    // обработка ошибки
                } finally {
                    this.loading = false; // Установите loading в false после загрузки данных (успешно или с ошибкой)
                }
            }
        },

        async deleteClient() {
            await axios
                .delete(`/order/${this.data_client.id}`)
                .then(response => {
                    console.log(response.data)
                    this.$emit('clientDeleted', this.data_client.id);
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async updateClient() {
            const formData = {
                name: this.big_category.name,
                slug: this.big_category.slug
            }
            await axios
                .put(`/big_category/${this.data_client.id}`, formData)
                .then(response => {
                    console.log(response.data)
                    this.$emit('clientUpdated', this.data_client.id);
                })
                .catch(error => {
                    console.log(error)
                })
        },
        toggleSeparator() {
            this.isCollapsed = !this.isCollapsed;
            this.loadClientOrders();
            this.loading = true
             // Вызываем метод при нажатии на кнопку
        },
    }
}
</script>

<style lang="scss">

.card {
  a {
    text-decoration: none; // Убираем подчеркивание
    cursor: pointer;
  }
}

.separator-card {
  display: flex;
  align-items: center;
  text-align: center;
}

.separator-card::before,
.separator-card::after {
  content: '';
  flex: 1;
  border-bottom: 1px solid #dee2e6;
}

.separator-card:not(:empty)::before {
  margin-right: 2em;
}

.separator-card:not(:empty)::after {
  margin-left: 2em;
}
</style>