<template>
    <div class="container-fluid text-center">
        <div class="row align-items-center mb-3">
          <div class="col-11">
            <div class="input-group align-items-center">
              <span class="input-group-text" id="basic-addon1"><i class="bi bi-search"></i></span>
              <input type="text" class="form-control" aria-label="Username" aria-describedby="basic-addon1">
            </div>
          </div>
          <div class="col-1">
            <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#exampleModal"><i class="bi bi-file-earmark-plus" style="font-size: 20px"></i></button>
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                <div class="modal-content">
                  <div class="modal-header text-center">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Создать статус заказа</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="name@example.com" v-model="name">
                      <label for="floatingInput">Имя</label>
                    </div>
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="Password" v-model="slug">
                      <label for="floatingPassword">Слаг</label>
                    </div>
                  </div>
                  <div class="modal-footer ">
                    <button @click="addOrderStatus()" type="button" class="btn btn-primary" data-bs-dismiss="modal">Cоздать</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col">
            <ListOrderStatus 
              v-for="order_status in order_statuses"
              v-bind:key="order_status.id"
              v-bind:order_status="order_status"
              @orderStatusDeleted="handleOrderStatusDeleted" 
              @orderStatusUpdated="handleOrderStatusUpdated"/>
          </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ListOrderStatus from '@/components/ListOrderStatus'

export default {
    name: 'OrderStatus',
    data() {
        return {
            order_statuses: [],
            name: '',
            slug: '',
        }
    },
    components: {
        ListOrderStatus
    },
    mounted() {
        this.getOrderStatus() 
    },
    methods: {
        async getOrderStatus() {
            await axios
                .get(`/order-statuses`)
                .then(response => {
                    this.order_statuses = response.data
                    console.log(this.order_statuses)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async addOrderStatus() {
            const formData = {
                name: this.name,
                slug: this.slug
            }
            await axios
                .post(`/order-status`, formData)
                .then(response => {
                    console.log(response.data)
                    this.getOrderStatus();
                })
                .catch(error => {
                    console.log(error)
                })
        },
        handleOrderStatusDeleted() {
            this.getOrderStatus();
        },
        handleOrderStatusUpdated() {
            this.getOrderStatus();
        },
    }
}   

</script>