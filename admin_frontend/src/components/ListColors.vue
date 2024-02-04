<template>
    <div class="card mb-1">
        <div class="card-body py-1 px-3">
        <div class="d-flex align-items-center">
            <span>{{ data_color.name }}</span>
            <button @click="$router.push(`/models`)" class="btn btn-icon d-inline ms-auto px-2"><i class="bi bi bi-box-seam"></i></button>
            
            <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + data_color.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
            <div class="modal fade" :id="'editModal_' + data_color.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                <div class="modal-content">
                  <div class="modal-header text-center">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Изменить размер, {{ data_color.name }}</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="name@example.com" v-model="update_data_color.name">
                      <label for="floatingInput">Имя</label>
                    </div>
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="Password" v-model="update_data_color.slug">
                      <label for="floatingPassword">Слаг</label>
                    </div>
                  </div>
                  <div class="modal-footer">
                    <button @click="updateColor()" type="button" class="btn btn-primary" data-bs-dismiss="modal">Изменить</button>
                  </div>
                </div>
              </div>
            </div>

            <button @click="deleteColor()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
        </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ListColors',
    props: {
        color: Object,
    },
    data() {
        return {
            data_color: this.color,
            update_data_color: {
                name: '',
                slug: '',
            },
        }
    },
    created() {
      this.update_data_color = { ...this.color };
    },
    methods: {
        async deleteColor() {
            await axios
                .delete(`/color/${this.data_color.id}`)
                .then(response => {
                    console.log(response.data)
                    this.$emit('colorDeleted');
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async updateColor() {
            const formData = {
                name: this.update_data_color.name,
                slug: this.update_data_color.slug,
            }
            try {
                await axios
                .put(`/color/${this.data_color.id}`, formData)
                .then(response => {
                    console.log(response.data)
                    this.data_color = { ...this.update_data_color }
                    this.$emit('colorUpdated');
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