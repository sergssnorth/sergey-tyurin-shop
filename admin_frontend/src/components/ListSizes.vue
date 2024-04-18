<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron">
            
            <div class="flex-grow-1 d-flex  align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.75rem;">
                <i class="bi bi-file-code"></i>
                </span>
                <span>{{ dataSize.name }}</span>
                <span class="ms-auto"><i class="bi bi-hash"></i></span>
                <span class="" style="margin-right: 1.5rem;">{{ dataSize.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button class="btn btn-icon mx-1 px-2 d-inline text-success" @click="">
                    <i class="bi bi-plus-circle" style="font-size: 18px;"></i>
                </button>
                <button class="btn btn-icon mx-1 px-2 d-inline text-dark" @click="this.$router.push({ path: '/models', query: { 'size': dataSize.id } });">
                    <i class="bi bi-layers" style="font-size: 18px;"></i>
                </button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataSize.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                
                
                <div class="modal fade" :id="'editModal_' + dataSize.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение размера</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="updatedSize.name">
                                    <label for="floatingInput">Имя</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" placeholder="Password" v-model="updatedSize.slug">
                                    <label for="floatingPassword">Слаг</label>
                                </div>
                            </div>
                            <div class="modal-footer ">
                                <button @click="updateSize()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Изменить</button>
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
        showErrorToast: Function,
        setLoading: Function,
        loading: Boolean,
        handleSizeUpdated: Function,
        handleSizeDeleted: Function,
   
    },
    data() {
        return { 
            dataSize : this.size,

            updatedSize: {
                name: '',
                slug: '',
            },
        }
    },
    created() {
        this.updatedSize = { ...this.size };
    },
    methods: {
        async updateSize() {
            const formData = {
                name: this.updatedSize.name,
                slug: this.updatedSize.slug,
            }
            this.setLoading(true);
            try {
                const response = await axios.put(`/size/${this.dataSize.id}`, formData);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleSizeUpdated()
            }
        },
        async deleteSize() {
            this.setLoading(true); // Включить индикатор загрузки
            try {
                const response = await axios.delete(`/size/${this.dataSize.id}`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleSizeDeleted()
            }
        },
    }

  }
</script>

<style scoped>

</style>