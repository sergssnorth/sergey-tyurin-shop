<template>
    <div class="card mb-1">
        <div class="card-body py-1 px-3">
        <div class="d-flex align-items-center">
            <span>{{ data_size.name }}</span>
            <button @click="$router.push(`/models`)" class="btn btn-icon d-inline ms-auto px-2"><i class="bi bi bi-box-seam"></i></button>
            
            <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
            <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                <div class="modal-content">
                  <div class="modal-header text-center">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Изменить размер</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="name@example.com" v-model="new_name">
                      <label for="floatingInput">Имя</label>
                    </div>
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="Password" v-model="new_slug">
                      <label for="floatingPassword">Слаг</label>
                    </div>
                  </div>
                  <div class="modal-footer">
                    <button @click="updateSize()" type="button" class="btn btn-primary" data-bs-dismiss="modal">Изменить</button>
                  </div>
                </div>
              </div>
            </div>

            <button @click="deleteSize()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
        </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ListSizes',
    props: {
        size: Object,
    },
    data() {
        return {
            data_size: this.size,
        }
    },
    computed: {
        pictureHover () {
            if (this.hover == true) {
                return this.product.get_image2
            } else {
                return this.product.get_image1
            }
        }
    },
    methods: {
        async deleteSize() {
            await axios
                .delete(`/size/${this.data_size.id}`)
                .then(response => {
                    console.log(response.data)
                    this.$emit('sizeDeleted', this.data_size.id);
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async updateSize() {
            const formData = {
                name: this.new_name,
                slug: this.new_slug,
            }
            try {
                await axios
                .put(`/size/${this.data_size.id}`, formData)
                .then(response => {
                    console.log(response.data)
                    const index = this.$parent.sizes.findIndex(size => size.id === this.data_size.id);
                    if (index !== -1) {
                        this.$parent.sizes.splice(index, 1, response.data);
                    }
                    this.$emit('sizeUpdated', this.data_size.id);
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