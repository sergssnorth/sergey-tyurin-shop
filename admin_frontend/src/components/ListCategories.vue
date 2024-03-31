<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron"
        :style="cardBodyStyles">
            
            <div class="flex-grow-1 d-flex  align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.5rem;">
                <i class="bi bi-person-circle"></i>
                </span>
                <span>{{ dataCategory.name }}</span>
                <span class="ms-auto" style="color: grey; margin-right: 0rem;"><i class="bi bi-hash"></i></span>
                <span class="" style="color: grey; margin-right: 1.5rem;">{{ dataCategory.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button class="btn btn-icon mx-1 px-2 d-inline text-dark" @click="this.$router.push({ path: '/models', query: { 'category': dataCategory.id } });">
                    <i class="bi bi-layers" style="font-size: 18px;"></i>
                </button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataCategory.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                
                
                <div class="modal fade" :id="'editModal_' + dataCategory.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение клиента</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mb-3">
                                <input type="text" class="form-control" placeholder="name@example.com" v-model="updatedCategory.name">
                                <label for="floatingInput">Имя</label>
                                </div>
                                <div class="form-floating mb-3">
                                <input type="text" class="form-control" placeholder="Password" v-model="updatedCategory.slug">
                                <label for="floatingPassword">Слаг</label>
                                </div>
                            </div>
                            <div class="modal-footer ">
                                <button @click="updateCategory()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Изменить</button>
                            </div>
                        </div>
                    </div>
                </div>

                <button @click="deleteCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
            </div>
        </div>
        <div class="separator-card" v-show="isCollapsed"></div>
        <div :id="'collapseProduct' + dataCategory.id" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
            <div class="card-body">
                <div v-if="modelLoading">
                    <div class="text-center">
                        <div v-show="modelLoading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>

                <div v-if="!modelLoading">
                    <div v-if="dataModels.models.length != 0">
                        <!-- <div v-for="model in dataModels.models" :key="category.id" class="d-flex align-items-center">
                            <span style="margin-right: 0.5em;">{{ model.id }}.</span>
                            <span>{{ model.name }}</span>
                            <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                            <button @click="deleteBigCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                        </div> -->
                        <div v-for="model in dataModels.models" :key="category.id" class="card mb-1" style="border-radius: 1.5rem;">
                            <div class="card-body elementSecondList py-1 px-3 d-flex align-items-center" id="headingExampleTwo" aria-controls="collapseIndicatorChevron">
                                <span style="margin-right: 0.5em;">{{ model.id }}.</span>
                                <span>{{ model.name }}</span>
                                <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                                <button @click="deleteBigCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                            </div>
                        </div>
                        <div class="d-flex align-items-center mt-3">
                            <button class="btn btn-outline-success px-3" style="border-radius: 1.25rem;">
                                <i class="bi bi-layers" style="margin-right: 0.5em;"></i>
                                <span>Добавить модель</span>
                            </button>
                        </div>
                    </div>
                    <div v-else style="text-align: start;">
                        <span>Моделей нет</span>
                        <div class="d-flex align-items-center mt-3">
                            <button class="btn btn-outline-success px-3" style="border-radius: 1.25rem;">
                                <i class="bi bi-layers" style="margin-right: 0.5em;"></i>
                                <span>Добавить модель</span>
                            </button>
                        </div>
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
    name: 'ListCategories',
    props: {
        category: Object,
        bigСategories: Array,
        showErrorToast: Function,
        setLoading: Function,
        loading: Boolean,
        handleCategoryUpdated: Function,
        handleCategoryDeleted: Function,
    },
    data() {
        return {
            isCollapsed : false,
            
            dataCategory : this.category,

            updatedCategory: {
                name: '',
                slug: '',
            },
            
            dataModels : {
                totalCount: 0,
                totalPages: 0,
                categories: []
            },
            
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
        this.updatedCategory = { ...this.category };
    },
    methods: {
        async getModels(categoryId) {
            this.modelLoading = true;
            const params = { category_id: categoryId,
                            offset: 0,
                            limit: 20 }
            try {
                const response = await axios.get(`/models`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, models } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    models: models
                };
                this.dataModels = transformedData;
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.modelLoading = false;
            }
        },
        async updateCategory() {
            const formData = {
                name: this.updatedCategory.name,
                slug: this.updatedCategory.slug
            }
            this.setLoading(true);
            try {
                const response = await axios.put(`/category/${this.dataCategory.id}`, formData);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleCategoryUpdated()
            }
        },
        async deleteCategory() {
            this.setLoading(true);
            try {
                const response = await axios.delete(`/category/${this.dataCategory.id}`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleCategoryDeleted()
            }
        },
        async toggleSeparator(event) {
            console.log("toggleSeparator")
            console.log(this.isCollapsed)
            console.log("toggleSeparator")

            // Подождем, чтобы Vue успел обновить isCollapsed
            await this.$nextTick();

            const collapseTarget = document.getElementById('collapseProduct' + this.dataCategory.id);

            if (!this.isCollapsed) {
                new Collapse(collapseTarget, { toggle: false }).show();
            } else {
                new Collapse(collapseTarget, { toggle: false }).hide();
            }

            this.isCollapsed = !this.isCollapsed;

            if (this.isCollapsed) {
              await this.getModels(this.dataCategory.id);
            }          
        },
    }
}
</script>
