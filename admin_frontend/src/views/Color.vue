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
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Создать раздел</h1>
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
                    <button @click="addColor()" type="button" class="btn btn-primary" data-bs-dismiss="modal">Cоздать</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col">
            <ListColors 
              v-for="color in colors"
              v-bind:key="color.id"
              v-bind:color="color"
              @colorDeleted="handleColorDeleted" 
              @colorUpdated="handleColorUpdated"/>
          </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ListColors from '@/components/ListColors'

export default {
    name: 'Color',
    data() {
        return {
            colors: [],
            name: '',
            slug: '',
        }
    },
    components: {
        ListColors
    },
    mounted() {
        this.getColors() 
    },
    methods: {
        async getColors() {
            await axios
                .get(`/colors`)
                .then(response => {
                    this.colors = response.data
                    console.log(this.colors)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async addColor() {
            const formData = {
                name: this.name,
                slug: this.slug
            }
            await axios
                .post(`/color`, formData)
                .then(response => {
                    console.log(response.data)
                    this.getColors();
                })
                .catch(error => {
                    console.log(error)
                })
        },
        handleColorDeleted() {
            this.getColors();
        },
        handleColorUpdated() {
            this.getColors();
        },
    }
}   

</script>