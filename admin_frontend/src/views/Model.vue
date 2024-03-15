<template>
    <div class="container-fluid text-center" style="height: 100%; display: flex; flex-direction: column;">
        <div class="row mb-3">
            <div class="d-flex align-items-center flex-grow-1" >
                <div class="input-group align-items-center">
                    <span @click="searchModels" class="input-group-text" id="basic-addon1" style="border-radius: 1.5rem 0 0 1.5rem;"><i class="bi bi-search" style="font-size: 16px;"></i></span>
                    <input v-model="search" @keyup.enter="searchModels" type="text" class="form-control" aria-label="Username" aria-describedby="basic-addon1" style="border-radius: 0 1.5rem 1.5rem 0;">
                </div>
                <div class="d-flex align-items-center">
                    
                    <button @click="" class="btn btn-icon d-inline mx-1 px-2 custom-dropdown-toggle" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i v-if="selectedSort == 'none'" class="bi bi-filter-circle"></i>
                        <i v-else class="bi bi-filter-circle-fill" style="color: #696cff;"></i>
                    </button>

                    <div class="dropdown-menu" aria-labelledby="userDropdown" style="width: 20rem;">
                        <div class="row">
                            <div class="col">
                                <div class="separator mx-3 mb-2">Сортировка</div>
                                <div class="form-check mx-3 mb-2">
                                    <input
                                        class="form-check-input"
                                        type="radio"
                                        name="exampleRadios"
                                        id="exampleRadios0"
                                        value="none"
                                        v-model="selectedSort"
                                        @change="changeSort"
                                    />
                                    <label class="form-check-label" for="exampleRadios0">Отсутствует</label>
                                </div>
                                <div class="form-check mx-3 mb-2">
                                    <input
                                        class="form-check-input"
                                        type="radio"
                                        name="exampleRadios"
                                        id="exampleRadios1"
                                        value="name-asc"
                                        v-model="selectedSort"
                                        @change="changeSort"
                                    />
                                    <label class="form-check-label d-flex align-middle" for="exampleRadios1">
                                        <i class="bi bi-sort-up align-middle" style="margin-right: 0.25rem;"></i>
                                        <span>По имени</span>
                                    </label>
                                </div>
                                <div class="form-check mx-3 mb-2">
                                    <input
                                        class="form-check-input"
                                        type="radio"
                                        name="exampleRadios"
                                        id="exampleRadios2"
                                        value="name-desc"
                                        v-model="selectedSort"
                                        @change="changeSort"
                                    />
                                    <label class="form-check-label d-flex align-middle" for="exampleRadios2">
                                        <i class="bi bi-sort-down align-middle" style="margin-right: 0.25rem;"></i>
                                        <span>По имени</span>
                                    </label>
                                </div>
                                <div class="form-check mx-3 mb-2">
                                    <input
                                        ref="selectedSortInputId"
                                        class="form-check-input"
                                        type="radio"
                                        name="exampleRadios"
                                        id="exampleRadios3"
                                        value="id-asc"
                                        v-model="selectedSort"
                                        @change="changeSort"
                                    />
                                    <label class="form-check-label d-flex align-middle" for="exampleRadios3">
                                        <i class="bi bi-sort-up align-middle" style="margin-right: 0.25rem;"></i>
                                        <span>По id</span>
                                    </label>
                                </div>
                                <div class="form-check mx-3 mb-2">
                                    <input
                                        ref="selectedSortInputId"
                                        class="form-check-input"
                                        type="radio"
                                        name="exampleRadios"
                                        id="exampleRadios4"
                                        value="id-desc"
                                        v-model="selectedSort"
                                        @change="changeSort"
                                    />
                                    <label class="form-check-label d-flex align-middle" for="exampleRadios4">
                                        <i class="bi bi-sort-down align-middle" style="margin-right: 0.25rem;"></i>
                                        <span>По id</span>
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>                    

                    <button @click="" class="btn btn-icon d-inline mx-1 px-2 custom-dropdown-toggle" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i v-if="filterCategory == 0" class="bi bi-funnel"></i>
                        <i v-else class="bi bi-funnel-fill" style="color: #696cff;"></i>
                    </button>

                    <div id="dropdown-menu-filter" class="dropdown-menu" aria-labelledby="userDropdown" style="width: 20rem;">
                        <div class="row">
                            <div class="col">
                                <div class="separator mx-3 mb-2">Фильтры</div>
                                <select @change="handleCategoryChange" v-model="filterCategory" class="form-select mx-3 mb-2 py-2" style="width: 91%;" aria-label="Default select example">
                                    <option :value="0">Выберите категорию</option>
                                    <option v-for="category in categories.categories" :key="category.id" :value="category.id">
                                        {{ category.name }}
                                    </option>
                                </select>
                                <select @change="handleCollectionChange" v-model="filterCategory" class="form-select mx-3 mb-2 py-2" style="width: 91%;" aria-label="Default select example">
                                    <option :value="0">Выберите коллекцию</option>
                                    <option v-for="collection in collections.collections" :key="collection.id" :value="collection.id">
                                        {{ collection.name }}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <button class="btn btn-icon mx-1 px-2 d-inline text-success" data-bs-toggle="modal" data-bs-target="#сreateModelModal">
                        <i class="bi bi-box-seam" style="font-size: 18px;"></i>
                    </button>
                    
                    <div class="modal fade" id="сreateModelModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                            <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Создание категории</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <select v-model="newModel.categoryId" class="form-select py-3" aria-label="Default select example">
                                    <option :value="0">Создание категории</option>
                                    <option v-for="category in categories.categories" :key="category.id" :value="category.id">
                                        {{ category.name }}
                                    </option>
                                </select>
                                <select v-model="newModel.collectionId" class="form-select py-3" aria-label="Default select example">
                                    <option :value="0">Создание категории</option>
                                    <option v-for="collection in collections.collections" :key="collection.id" :value="collection.id">
                                        {{ collection.name }}
                                    </option>
                                </select>
                                <div class="form-floating mt-2 mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="newModel.name">
                                    <label for="floatingInput">Имя</label>
                                </div>
                                <div class="form-floating mb-2">
                                    <input type="text" class="form-control" placeholder="Password" v-model="newModel.slug">
                                    <label for="floatingPassword">Слаг</label>
                                </div>

                            </div>
                            <div class="modal-footer ">
                                <button @click="addModel()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Cоздать</button>
                            </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row flex-grow-1" id="big-category-list">
            <div class="col d-flex flex-column" style="flex-grow: 1;">
            
                <div v-if="loading">
                    <div class="text-center">
                        <div v-show="loading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>
                <div v-if="!loading">
                    <div v-if="models.models.length != 0">
                        <ListModels
                        v-for="model in models.models"
                        v-bind:key="model.id"
                        v-bind:model="model"
                        v-bind:categories="categories"
                        v-bind:collections="collections"
                        @modelDeleted="handleModelDeleted" 
                        @modelUpdated="handleModelUpdated"
                        :showErrorToast="showErrorToast"/>
                    </div>
                    <div v-else>
                        <span style="font-size: 1.3rem;">Моделей пока нет ...</span>
                    </div>
                    
                </div>

            </div>
        </div>
        <div class="row">
            <div class="col text-center">
                <nav class="px-0 py-0" aria-label="Навигация по страницам">
                    <ul class="my-2 pagination justify-content-center">
                        <li class="page-item page-item-pointer" v-if="models.totalPages > 1 && currentPage > 1">
                            <a class="page-link" @click="changePage(currentPage - 1)" aria-label="Предыдущая">
                            <span aria-hidden="true">&laquo;</span>
                            </a>
                        </li>
                        <li class="page-item page-item-pointer" v-for="page in displayedPages" :key="page">
                            <template v-if="page === '...'">
                            <span class="page-link">...</span>
                            </template>
                            <template v-else>
                            <a class="page-link" @click="changePage(page)" :class="{ 'active': page == currentPage }">{{ page }}</a>
                            </template>
                        </li>
                        <li class="page-item page-item-pointer" v-if="models.totalPages > 1 && currentPage < models.totalPages">
                            <a class="page-link" @click="changePage(currentPage + 1)" aria-label="Следующая">
                            <span aria-hidden="true">&raquo;</span>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="successfulCreationModelToast" class="toast text-bg-success" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="3000">
                <div class="d-flex">
                    <div class="toast-body">
                        Модель успешно создана!
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        </div>
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="errorToast" class="toast text-bg-danger" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="7000">
                <div class="d-flex">
                    <div class="toast-body" id="errorToastBody">
                        Ошибка ...
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        </div>
    </div>

    <!-- <div class="container-fluid text-center" style="height: 100%; display: flex; flex-direction: column;">
        <div class="row align-items-center mb-3">
            <div class="col-2">
                <select v-model="filter_big_category_id" class="form-select" aria-label="Default select example" @change="handleBigCategoryFilterChange">
                    <option :value="0">Все разделы</option>
                    <option v-for="big_category in big_models" :key="big_category.id" :value="big_category.id">
                        {{ big_category.name }}
                    </option>
                </select>
            </div>
            <div class="col-2">
                <select v-model="filter_category_id" class="form-select" aria-label="Default select example" @change="handleCategoryFilterChange">
                    <option :value="0">Все категории</option>
                    <option v-for="category in models" :key="category.id" :value="category.id">
                        {{ category.name }}
                    </option>
                </select>
            </div>
            <div class="col-2">
                <select v-model="filter_collection_id" class="form-select" aria-label="Default select example" @change="handleCollectionFilterChange">
                    <option :value="0">Все коллекции</option>
                    <option v-for="collection in collections" :key="collection.id" :value="collection.id">
                        {{ collection.name }}
                    </option>
                </select>
            </div>
            <div class="col-5">
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
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Создать модель</h1>
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
                        <div class="form-floating mb-3">
                        <input type="text" class="form-control" placeholder="Password" v-model="description">
                        <label for="floatingPassword">Описание</label>
                        </div>
                        
                        <select v-model="big_category_id" class="form-select py-3 mb-3" aria-label="Default select example" @change="handleBigCategoryFilterChangeCreateModal">
                            <option :value="0">Выберите раздел</option>
                            <option v-for="big_category in big_models" :key="big_category.id" :value="big_category.id">
                                {{ big_category.name }}
                            </option>
                        </select>

                        <select v-model="category_id" class="form-select py-3 mb-3" aria-label="Default select example">
                            <option :value="0">Выберите категорию</option>
                            <option v-for="category in models" :key="category.id" :value="category.id">
                                {{ category.name }}
                            </option>
                        </select>

                        <select v-model="collection_id" class="form-select py-3 mb-3" aria-label="Default select example">
                            <option :value="0">Выберите коллекцию</option>
                            <option v-for="collection in collections" :key="collection.id" :value="collection.id">
                                {{ collection.name }}
                            </option>
                        </select>

                    </div>
                    <div class="modal-footer ">
                        <button @click="addModel()" type="button" class="btn btn-primary" data-bs-dismiss="modal">Cоздать</button>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
        <div class="row flex-grow-1" style="overflow-y: auto;">
          <div class="col d-flex flex-column" style="flex-grow: 1;">
            <ListModels 
              v-for="model in models"
              v-bind:key="model.id"
              v-bind:model="model"
              v-bind:big_models="big_models"
              v-bind:models="models"
              v-bind:collections="collections"
              @categoryDeleted="handleCategoryDeleted" 
              @categoryUpdated="handleCategoryUpdated"/>
          </div>
        </div>
    </div> -->
</template>

<script>
import axios from 'axios'
import { Toast } from 'bootstrap/dist/js/bootstrap.js'

import ListModels from '@/components/ListModels'

export default {
    name: 'Model',
    data() {
        return {
            search: '',
            selectedSort: '',

            filterCategory: 0,
            filterCollection: 0,

            newModel: {
                categoryId: 0,
                collectionId: 0,
                name: '',
                slug: '',
            },

            categories : {
                totalCount: 0,
                totalPages: 0,
                categories: []
            },

            collections : {
                totalCount: 0,
                totalPages: 0,
                collections: []
            },

            models : {
                totalCount: 0,
                totalPages: 0,
                models: []
            },

            loading : true,
            currentPage: 1,
        }
    },
    components: {
        ListModels,
    },
    computed: {
        displayedPages() {
            const totalDisplayPages = 5;
            const startPage = Math.max(1, this.currentPage - 2);
            const endPage = Math.min(this.models.totalPages, startPage + totalDisplayPages - 1);

            let pages = [];

            if (startPage > 1) {
            pages.push(1, '...');
            }

            for (let i = startPage; i <= endPage; i++) {
            pages.push(i);
            }

            if (endPage < this.models.totalPages) {
            pages.push('...', this.models.totalPages);
            }

            return pages;
        }
    },
    created() {
        const category = this.$route.query['category'];
        if (category) {
            console.log('category:', category);
            localStorage.setItem('modelFilterCategory', category);
        } else {
            localStorage.setItem('modelFilterCategory', 0);
        }
    },
    async mounted() {
        this.currentPage = localStorage.getItem('modelsCurrentPage');

        if (!this.currentPage) {
            this.currentPage = 1;
            localStorage.setItem('modelsCurrentPage', this.currentPage);
        }

        this.selectedSort = localStorage.getItem('modelsSelectedSort');

        if (!this.selectedSort) {
            this.selectedSort = 'none';
            localStorage.setItem('modelsSelectedSort', this.selectedSort);
        }

        this.filterCategory = localStorage.getItem('modelFilterCategory');

        if (!this.filterCategory) {
            this.filterCategory = 0;
            localStorage.setItem('modelFilterCategory', this.filterCategory);
        }

        await this.getModels(this.currentPage, this.selectedSort, this.filterCategory);
        await this.getCategories()
    },
    methods: {
        async getCategories() {
            try {
                this.loading = true;
                const response = await axios.get(`/categories`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, categories } = response.data;

                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    categories: categories
                };

                this.categories = transformedData;
                console.log(this.categories);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async getCollections() {
            try {
                this.loading = true;
                const response = await axios.get(`/collections`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, collections } = response.data;

                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    collections: collections
                };

                this.collections = transformedData;
                console.log(this.collections);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },

        async getModels(page, selectedSort, filterCategory, filterCollection) {
            const offset = (page - 1) * 50
            let params = {
                offset: offset,
                limit: 50
            };
            if (this.search !== "") {
                params.search = this.search;
            }
            if (selectedSort !== "none") {
                console.log(selectedSort)
                const [sortBy, order] = selectedSort.split("-");
                params.sort_by = sortBy;
                params.order = order;
            }
            if (filterCategory !== 0) {
                console.log(filterCategory)
                params.category_id = filterCategory;
            }
            if (filterCollection !== 0) {
                console.log(filterCollection)
                params.collection_id = filterCollection;
            }

            try {
                this.loading = true;
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

                this.models = transformedData;
                console.log(this.models);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async addModel() {
            const formData = {
                category_id: this.newModel.categoryId,
                collection_id: this.newModel.collectionId,
                name: this.newModel.name,
                slug: this.newModel.slug
            }
            console.log(formData)
            try {
                this.loading = true;
                const response = await axios.post(`/category`, formData);
                if (response.status == 200) {
                    this.showSuccessfulCreationModelToast()
                }
                else {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                await this.getModels(this.currentPage, this.selectedSort, this.filterCategory);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async searchModels() {
            try {
                this.currentPage = 1;
                localStorage.setItem('modelsCurrentPage',  this.currentPage);
                await this.getModels(this.currentPage, this.selectedSort, this.filterCategory);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async changePage(page) {
            this.loading = true;
            localStorage.setItem('modelsCurrentPage', page);
            this.currentPage = page
            await this.getModels(page, this.selectedSort, this.filterCategory);
            this.loading = false;
        },
        async changeSort() {
            this.loading = true;
            try {
                this.currentPage = 1;
                localStorage.setItem('modelsCurrentPage',  this.currentPage);
                localStorage.setItem('modelsSelectedSort',  this.selectedSort);
                await this.getModels(this.currentPage, this.selectedSort, this.filterCategory);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },

        async handleCategoryChange(event) {
            await this.getModels(this.currentPage, this.selectedSort, this.filterCategory);
            console.log("Выбранное значение:", event.target.value);
        },
        async handleCollectionChange(event) {
            await this.getModels(this.currentPage, this.selectedSort, this.filterCategory);
            console.log("Выбранное значение:", event.target.value);
        },
        showSuccessfulCreationModelToast() {
            const successfulCreation = new Toast(document.getElementById('successfulCreationModelToast'))
            successfulCreation.show()
        },
        showErrorToast(errorCode, errorMessage) {
            const errorCreation = new Toast(document.getElementById('errorToast'));
            const errorBody = document.getElementById('errorToastBody');
            errorBody.textContent = 'Ошибка, ' + errorCode + ', ' + errorMessage;
            errorCreation.show();
        },
        async handleModelDeleted() {
            await this.getModels(this.currentPage, this.selectedSort, this.filterCategory);
        },
        async handleModelUpdated() {
            await this.getModels(this.currentPage, this.selectedSort, this.filterCategory);
        }
    },
    watch: {
        async '$route'(to, from) {
            const category = this.$route.query['category'];
            if (category) {
                console.log('category:', category);
                localStorage.setItem('modelFilterCategory', category);
            } else {
                localStorage.setItem('modelFilterCategory', 0);
            }
            this.filterCategory = localStorage.getItem('modelFilterCategory');

            await this.getModels(this.currentPage, this.selectedSort, this.filterCategory);
            await this.getCategories()
        }
    }
    // data() {
    //     return {
    //         filter_big_category_id: 0,
    //         filter_category_id: 0,
    //         filter_collection_id: 0,

    //         big_models: [],
    //         models: [],
    //         collections: [],
    //         models: [],

    //         list_select_big_models: [],
    //         list_select_models: [],
    //         list_select_collections: [],
            
    //         name: '',
    //         slug: '',
    //         description: '',
    //         big_category_id: 0,
    //         category_id: 0,
    //         collection_id: 0,
    //         FilterId: '',
    //     }
    // },
    // components: {
    //     ListModels
    // },
    // mounted() {
    //     console.log("mounted")
    //     this.getCategories()
    //     this.getCollections()
    //     this.getFilterId()

    //     const { big_category_id, category_id, collection_id } = this.$route.query;

    //     if (big_category_id !== '0') {
    //         const parsedBigCategoryId = parseInt(big_category_id, 10);
    //         this.filter_big_category_id = parsedBigCategoryId
    //     }

    //     if (category_id !== '0') {
    //         const parsedCategoryId = parseInt(category_id, 10);
    //         this.filter_category_id = parsedCategoryId
    //     }

    //     if (collection_id !== '0') {
    //         const parsedCollectionId = parseInt(collection_id, 10);
    //         this.filter_collection_id = parsedCollectionId
    //     }

    //     this.getModels(this.filter_big_category_id)

    //         // Копирование значений из big_models в list_select_big_models
    //     this.list_select_big_models = this.big_models.slice();

    //     // Копирование значений из models в list_select_models
    //     this.list_select_models = this.models.slice();

    //     // Копирование значений из collections в list_select_collections
    //     this.list_select_collections = this.collections.slice();


    //     this.getModels(this.filter_big_category_id, this.filter_category_id, this.filter_collection_id)
    // },
    // methods: {
    //     getFilterId() {
    //         console.log('Метод getFilterId')
    //         this.filter_big_category_id = this.$route.query.big_category_id;
    //     },
    //     async getCategories() {
    //         console.log('Метод getCategories')
    //         await axios
    //             .get(`/big_models`)
    //             .then(response => {
    //                 this.big_models = response.data
    //                 console.log(this.big_models)
    //             })
    //             .catch(error => {
    //                 console.log(error)
    //             })
    //     },
    //     async getModels(filterId) {
    //         console.log('Метод getModels')
    //         if (filterId !== undefined && filterId !== null) {
    //             console.log('Значение filterId:', filterId);
    //             const params = filterId !== '0' ? { big_category_id: filterId } : {};
    //             console.log(filterId)
    //             await axios
    //                 .get(`/models`, { params })
    //                 .then(response => {
    //                     this.models = response.data
    //                     console.log(this.models)
    //                 })
    //                 .catch(error => {
    //                     console.log(error)
    //                 })
    //         } else {
    //             console.log('Значение filterId отсутствует');
    //             await axios
    //             .get(`/models`)
    //             .then(response => {
    //                 this.models = response.data
    //                 console.log(this.models)
    //             })
    //             .catch(error => {
    //                 console.log(error)
    //             })
    //         }
    //     },
    //     async getCollections() {
    //         console.log('Метод getCategories')
    //         await axios
    //             .get(`/collections`)
    //             .then(response => {
    //                 this.collections = response.data
    //                 console.log(this.collections)
    //             })
    //             .catch(error => {
    //                 console.log(error)
    //             })
    //     },
    //     async getModels(big_category_filterId, category_filterId, collection_filterId) {
    //         console.log('Метод getModels')
            
    //         const params = {};

    //         if (big_category_filterId !== undefined && big_category_filterId !== null) {
    //             console.log('Значение big_category_filterId:', big_category_filterId);
    //             const parsedBigCategoryId = parseInt(big_category_filterId, 10);

    //             if (!isNaN(parsedBigCategoryId) && parsedBigCategoryId !== 0) {
    //                 params.big_category_id = parsedBigCategoryId;
    //             }
    //         }

    //         if (category_filterId !== undefined && category_filterId !== null) {
    //             console.log('Значение category_filterId:', category_filterId);
    //             const parsedCategoryId = parseInt(category_filterId, 10);

    //             if (!isNaN(parsedCategoryId) && parsedCategoryId !== 0) {
    //                 params.category_id = parsedCategoryId;
    //             }
    //         }

    //         if (collection_filterId !== undefined && collection_filterId !== null) {
    //             console.log('Значение collection_filterId:', collection_filterId);
    //             const parsedCollectionId = parseInt(collection_filterId, 10);

    //             if (!isNaN(parsedCollectionId) && parsedCollectionId !== 0) {
    //                 params.collection_id = parsedCollectionId;
    //             }
    //         }

    //         console.log(params);

    //         try {
    //             const response = await axios.get('/models', { params });
    //             this.models = response.data;
    //             console.log(this.models);
    //         } catch (error) {
    //             console.log(error);
    //         }
    //     },
        
    //     async addModel() {
    //         // let filterId;

    //         const formData = {
    //             name: this.name,
    //             slug: this.slug,
    //             description: this.description,
    //             category_id: this.category_id,
    //             collection_id: this.collection_id
    //         }
    //         console.log(formData)
    //         await axios
    //             .post(`/model`, formData)
    //             .then(response => {
    //                 console.log(response.data)
    //                 // filterId = this.getFilterId()
    //                 // this.getModels(filterId);
    //                 //this.getModels(this.big_category_id, this.category_id, this.collection_id)
    //                 const queryString = `?big_category_id=${this.big_category_id}&category_id=${this.category_id}&collection_id=${this.collection_id}`;
    //                 this.$router.push(`/models${queryString}`);
                    
    //                 this.name = '',
    //                 this.slug = '',
    //                 this.description = '',
    //                 this.big_category_id = 0,
    //                 this.category_id = 0,
    //                 this.collection_id = 0

    //             })
    //             .catch(error => {
    //                 console.log(error)
    //             })
    //     },
    //     handleBigCategoryFilterChange() {
            
    //         console.log('Хендлер handleBigCategoryFilterChange');
    //         if (this.filter_category_id != 0) {
    //             this.filter_category_id = 0   
    //             const queryString = `?big_category_id=${this.filter_big_category_id}&category_id=${this.filter_category_id}&collection_id=${this.filter_collection_id}`;
    //             this.$router.push(`/models${queryString}`);
    //         }
    //         const queryString = `?big_category_id=${this.filter_big_category_id}&category_id=${this.filter_category_id}&collection_id=${this.filter_collection_id}`;

    //         this.$router.push(`/models${queryString}`);
    //     },
    //     handleBigCategoryFilterChangeCreateModal() {
    //         console.log('Хендлер handleBigCategoryFilterChangeCreateModal');
    //         this.category_id = 0
    //         this.getModels(this.big_category_id)
    //     },

    //     handleCategoryFilterChange() {
    //         console.log('Хендлер handleCategoryFilterChange');
    //         const queryString = `?big_category_id=${this.filter_big_category_id}&category_id=${this.filter_category_id}&collection_id=${this.filter_collection_id}`;

    //         this.$router.push(`/models${queryString}`);
    //     },
    //     handleCollectionFilterChange() {
    //         console.log('Хендлер handleCollectionFilterChange');
    //         const queryString = `?big_category_id=${this.filter_big_category_id}&category_id=${this.filter_category_id}&collection_id=${this.filter_collection_id}`;

    //         this.$router.push(`/models${queryString}`);
    //     },

    //     handleCategoryDeleted() {
    //         console.log('Хендлер handleCategoryDeleted')
    //         const filterId = this.getFilterId()
    //         console.log('filterId')
    //         console.log(filterId)
    //         console.log('filterId')
    //         this.getModels(filterId);
    //     },
    //     handleCategoryUpdated() {
    //         console.log('Хендлер handleCategoryUpdated')
    //         const filterId = this.getFilterId()
    //         console.log('filterId')
    //         console.log(filterId)
    //         console.log('filterId')
    //         this.getModels(filterId);
    //     },
    // },
    // beforeRouteUpdate(to, from, next) {
    //     console.log('Хук beforeRouteUpdate');
    //     const big_category_filterId = to.query.big_category_id;
    //     const category_filterId = to.query.category_id;
    //     const collection_filterId = to.query.collection_id;

    //     this.filter_big_category_id = to.query.big_category_id;
    //     this.filter_category_id = to.query.category_id;
    //     this.filter_collection_id = to.query.collection_id;
    //     //this.filter_big_category_id = filterId
    //     this.getModels(big_category_filterId)
    //     this.getModels(big_category_filterId, category_filterId, collection_filterId)

    //     next();
    // },
}   

</script>