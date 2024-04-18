<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron">
            
            <div class="flex-grow-1 d-flex  align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.75rem;">
                <i class="bi bi-file-image"></i>
                </span>
                <span>{{ dataColor.name }}</span>
                <span class="ms-auto"><i class="bi bi-hash"></i></span>
                <span class="" style="margin-right: 1.5rem;">{{ dataColor.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button class="btn btn-icon mx-1 px-2 d-inline text-success" @click="">
                    <i class="bi bi-plus-circle" style="font-size: 18px;"></i>
                </button>

                <button class="btn btn-icon mx-1 px-2 d-inline text-dark" @click="this.$router.push({ path: '/models', query: { 'color': dataColor.id } });">
                    <i class="bi bi-layers" style="font-size: 18px;"></i>
                </button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataColor.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                
                
                <div class="modal fade" :id="'editModal_' + dataColor.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение размера</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="updatedColor.name">
                                    <label for="floatingInput">Имя</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" placeholder="Password" v-model="updatedColor.slug">
                                    <label for="floatingPassword">Слаг</label>
                                </div>
                            </div>
                            <div class="modal-footer ">
                                <button @click="updateColor()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Изменить</button>
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
        showErrorToast: Function,
        setLoading: Function,
        loading: Boolean,
        handleColorUpdated: Function,
        handleColorDeleted: Function,
   
    },
    data() {
        return { 
            dataColor : this.color,

            updatedColor: {
                name: '',
                slug: '',
            },
        }
    },
    created() {
        this.updatedColor = { ...this.color };
    },
    methods: {
        async updateColor() {
            const formData = {
                name: this.updatedColor.name,
                slug: this.updatedColor.slug,
            }
            this.setLoading(true);
            try {
                const response = await axios.put(`/color/${this.dataColor.id}`, formData);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleColorUpdated()
            }
        },
        async deleteColor() {
            this.setLoading(true); // Включить индикатор загрузки
            try {
                const response = await axios.delete(`/color/${this.dataColor.id}`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleColorDeleted()
            }
        },
    }

  }
</script>

<style scoped>

</style>