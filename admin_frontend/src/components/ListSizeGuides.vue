<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron"
        :style="cardBodyStyles">
            
            <div class="flex-grow-1 d-flex  align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.5rem;">
                <i class="bi bi-person-circle"></i>
                </span>
                <span>{{ dataSizeGuide.name }}</span>
                <span class="ms-auto" style="color: grey; margin-right: 0rem;"><i class="bi bi-hash"></i></span>
                <span class="" style="color: grey; margin-right: 1.5rem;">{{ dataSizeGuide.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button class="btn btn-icon mx-1 px-2 d-inline text-dark" @click="this.$router.push({ path: '/models', query: { 'sizeGuide': dataSizeGuide.id } });">
                    <i class="bi bi-layers" style="font-size: 18px;"></i>
                </button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataSizeGuide.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                
                
                <div class="modal fade" :id="'editModal_' + dataSizeGuide.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение описания</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="updatedSizeGuide.name">
                                    <label for="floatingInput">Имя</label>
                                </div>
                                <div class="mb-3" style="text-align: start;">
                                    <label for="formFileEdit" class="form-label">Изображение</label>
                                    <input class="form-control" type="file" id="formFileEdit" @change="onImageChange">
                                </div>
                                <img v-if="updatedSizeGuide.image" :src="updatedSizeGuide.image" class="img-fluid" alt="preview">
                            </div>
                            <div class="modal-footer">
                                <button @click="updateSizeGuide()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Изменить</button>
                            </div>
                        </div>
                    </div>
                </div>

                <button @click="deleteSizeGuide()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
            </div>
        </div>
        <div class="separator-card" v-show="isCollapsed"></div>
        <div :id="'collapseProduct' + dataSizeGuide.id" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
            <div class="card-body">
                <!-- <div v-if="modelLoading">
                    <div class="text-center">
                        <div v-show="modelLoading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>

                <div v-if="!modelLoading">
                    <div v-if="dataModels.models.length != 0">
                        <div v-for="model in dataModels.models" :key="sizeGuide.id" class="d-flex align-items-center">
                            <span style="margin-right: 0.5em;">{{ model.id }}.</span>
                            <span>{{ model.name }}</span>
                            <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                            <button @click="deleteBigsizeGuide()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                        </div>
                    </div>
                    <div v-else>
                        <span>Моделей нет</span>
                    </div>
                </div> -->
                
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { Collapse } from 'bootstrap/dist/js/bootstrap.js'


export default {
    name: 'ListSizeGuides',
    props: {
        sizeGuide: Object,
        showErrorToast: Function,
        setLoading: Function,
        loading: Boolean,
        handleSizeGuideUpdated: Function,
        handleSizeGuideDeleted: Function,
    },
    data() {
        return {
            isCollapsed : false,
            
            dataSizeGuide : this.sizeGuide,

            updatedSizeGuide: {
                name: '',
                description: '',
            },
            
            // dataModels : {
            //     totalCount: 0,
            //     totalPages: 0,
            //     models: []
            // },
            
            modelLoading: true,
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
        this.updatedSizeGuide = { ...this.sizeGuide };
    },
    methods: {
        // async getModels(sizeGuideId) {
        //     this.modelLoading = true;
        //     const params = { sizeGuide_id: sizeGuideId,
        //                     offset: 0,
        //                     limit: 20 }
        //     try {
        //         const response = await axios.get(`/models`, { params });
        //         if (!response.status == 200) {
        //             this.showErrorToast(response.status, response.data)
        //             console.log(response);
        //         }
        //         const { total_count, total_pages, models } = response.data;

        //         // Преобразование ключей totalCount и totalPages
        //         const transformedData = {
        //             totalCount: total_count,
        //             totalPages: total_pages,
        //             models: models
        //         };
        //         this.dataModels = transformedData;
        //     } catch (error) {
        //         this.showErrorToast(error.code, error.message);
        //         console.error(error);
        //     } finally {
        //         this.modelLoading = false;
        //     }
        // },
        async updateSizeGuide() {
            const formData = {
                name: this.updatedSizeGuide.name,
                description: this.updatedSizeGuide.description
            }
            this.setLoading(true);
            try {
                const response = await axios.put(`/sizeGuide/${this.dataSizeGuide.id}`, formData);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleSizeGuideUpdated()
            }
        },
        async deleteSizeGuide() {
            this.setLoading(true);
            try {
                const response = await axios.delete(`/sizeGuide/${this.dataSizeGuide.id}`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleSizeGuideDeleted()
            }
        },
        onImageChange(e) {
            const file = e.target.files[0];
            if (file) {
                // Создаем URL для предпросмотра изображения
                this.updatedSizeGuide.image = URL.createObjectURL(file);
                // Также сохраняем файл для отправки на сервер
                this.updatedSizeGuide.newImage = file;
            }
        },
        async toggleSeparator(event) {
            console.log("toggleSeparator")
            console.log(this.isCollapsed)
            console.log("toggleSeparator")

            // Подождем, чтобы Vue успел обновить isCollapsed
            await this.$nextTick();

            const collapseTarget = document.getElementById('collapseProduct' + this.dataSizeGuide.id);

            if (!this.isCollapsed) {
                new Collapse(collapseTarget, { toggle: false }).show();
            } else {
                new Collapse(collapseTarget, { toggle: false }).hide();
            }

            this.isCollapsed = !this.isCollapsed;

            // if (this.isCollapsed) {
            //   await this.getModels(this.dataSizeGuide.id);
            // }          
        },
    }
}
</script>
