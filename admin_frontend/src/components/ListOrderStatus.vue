<template>
    <div class="card mb-1">
        <div class="card-body py-1 px-3">
        <div class="d-flex align-items-center">
            <span>{{ data_order_status.name }}</span>
            <button @click="$router.push(`/models`)" class="btn btn-icon d-inline ms-auto px-2"><i class="bi bi bi-box-seam"></i></button>
            
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
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ListOrderStatus',
    props: {
        order_status: Object,
    },
    data() {
        return {
            data_order_status: this.order_status,
            update_data_order_status: {
                name: '',
                slug: '',
            },
        }
    },
    created() {
      this.update_data_order_status = { ...this.order_status };
    },
    methods: {
        async deleteOrderStatus() {
            await axios
                .delete(`/order-status/${this.data_order_status.id}`)
                .then(response => {
                    console.log(response.data)
                    this.$emit('orderStatusDeleted');
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async updateOrderStatus() {
            const formData = {
                name: this.update_data_order_status.name,
                slug: this.update_data_order_status.slug,
            }
            try {
                await axios
                .put(`/order-status/${this.data_order_status.id}`, formData)
                .then(response => {
                    console.log(response.data)
                    this.data_order_status = { ...this.update_data_order_status }
                    this.$emit('orderStatusUpdated');
                })
            } catch (error) {
                console.log(error);
            }
        },
    }
}
</script>

<style scoped>

</style>