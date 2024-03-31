<template>
    <div class="container-fluid text-center" style="height: 100%; display: flex; flex-direction: column;">
        <div class="row mb-3">
            <div class="d-flex align-items-center flex-grow-1" >
                <div class="input-group align-items-center">
                    <span @click="searchProducts" class="input-group-text" id="basic-addon1" style="border-radius: 1.5rem 0 0 1.5rem;"><i class="bi bi-search" style="font-size: 16px;"></i></span>
                    <input v-model="search" @keyup.enter="searchProducts" type="text" class="form-control" aria-label="Username" aria-describedby="basic-addon1" style="border-radius: 0 1.5rem 1.5rem 0;">
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
                        <i v-if="filterModel == 0" class="bi bi-funnel"></i>
                        <i v-else class="bi bi-funnel-fill" style="color: #696cff;"></i>
                    </button>

                    <div id="dropdown-menu-filter" class="dropdown-menu" aria-labelledby="userDropdown" style="width: 20rem;">
                        <div class="row">
                            <div class="col">
                                <div class="separator mx-3 mb-2">Фильтры</div>
                                <select @change="handleModelChange" v-model="filterModel" class="form-select mx-3 mb-2 py-2" style="width: 91%;" aria-label="Default select example">
                                    <option :value="0">Выберите модель</option>
                                    <option v-for="model in models.models" :key="model.id" :value="model.id">
                                        {{ model.name }}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <button class="btn btn-icon mx-1 px-2 d-inline text-success" data-bs-toggle="modal" data-bs-target="#сreateproductModal">
                        <i class="bi bi-box-seam" style="font-size: 18px;"></i>
                    </button>
                    
                    <div class="modal fade" id="сreateproductModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                            <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Создание продукта</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">


                                <div class="form-floating mt-2 mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="newProduct.name">
                                    <label for="floatingInput">Имя</label>
                                </div>
                                <div class="form-floating mb-2">
                                    <input type="text" class="form-control" placeholder="Password" v-model="newProduct.slug">
                                    <label for="floatingPassword">Слаг</label>
                                </div>

                            </div>
                            <div class="modal-footer ">
                                <button @click="addProduct()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Cоздать</button>
                            </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row flex-grow-1" id="model-list">
            <div class="col d-flex flex-column" style="flex-grow: 1;">
            
                <div v-if="loading">
                    <div class="text-center">
                        <div v-show="loading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>
                <div v-if="!loading">
                    <div v-if="products.products.length != 0">
                        <ListProducts
                        v-for="product in products.products"
                        :key="product.id"
                        :product="product"
                        :bigproducts="bigproducts"
                        :setLoading="setLoading"
                        :handleProductDeleted = "handleProductDeleted"
                        :handleProductUpdated = "handleProductUpdated"
                        :loading="loading"
                        :showErrorToast="showErrorToast"/>
                    </div>
                    <div v-else>
                        <span style="font-size: 1.3rem;">Продуктов пока нет ...</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col text-center">
                <nav class="px-0 py-0" aria-label="Навигация по страницам">
                    <ul class="my-2 pagination justify-content-center">
                        <li class="page-item page-item-pointer" v-if="products.totalPages > 1 && currentPage > 1">
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
                        <li class="page-item page-item-pointer" v-if="products.totalPages > 1 && currentPage < products.totalPages">
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
                        Продукт успешно создан!
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
</template>

<script>
import axios from 'axios'
import { Toast } from 'bootstrap/dist/js/bootstrap.js'

import ListProducts from '@/components/ListProducts'

export default {
    name: 'Product',
    
    data() {
        return {
            search: '',
            selectedSort: '',
            filterModel: 0,

            newProduct: {
                name: '',
                slug: '',
            },

            products : {
                totalCount: 0,
                totalPages: 0,
                products: []
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
        ListProducts,
    },
    computed: {
        displayedPages() {
            const totalDisplayPages = 5;
            const startPage = Math.max(1, this.currentPage - 2);
            const endPage = Math.min(this.products.totalPages, startPage + totalDisplayPages - 1);

            let pages = [];

            if (startPage > 1) {
            pages.push(1, '...');
            }

            for (let i = startPage; i <= endPage; i++) {
            pages.push(i);
            }

            if (endPage < this.products.totalPages) {
            pages.push('...', this.products.totalPages);
            }

            return pages;
        }
    },
    created() {
        const model = this.$route.query['model'];
        if (model) {
            console.log('model:', model);
            localStorage.setItem('productfilterMode', model);
        } else {
            localStorage.setItem('productfilterMode', 0);
        }
    },
    async mounted() {
        this.currentPage = localStorage.getItem('productCurrentPage');

        if (!this.currentPage) {
            this.currentPage = 1;
            localStorage.setItem('productCurrentPage', this.currentPage);
        }

        this.selectedSort = localStorage.getItem('productSelectedSort');

        if (!this.selectedSort) {
            this.selectedSort = 'none';
            localStorage.setItem('productSelectedSort', this.selectedSort);
        }

        this.filterModel = localStorage.getItem('productfilterMode');

        if (!this.filterModel) {
            this.filterModel = 0;
            localStorage.setItem('productfilterMode', this.filterModel);
        }

        await this.getProducts(this.currentPage, this.selectedSort, this.filterModel);
        await this.getModels()
    },
    methods: {
        async getProducts(page, selectedSort, filterModel) {
            console.log("getProducts")
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
            if (filterModel !== 0) {
                console.log(filterModel)
                params.model_id = filterModel;
            }

            try {
                this.loading = true;
                const response = await axios.get(`/products`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, products } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    products: products
                };

                this.products = transformedData;
                console.log(this.products);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async getModels() {
            try {
                this.loading = true;
                const response = await axios.get(`/models`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, models } = response.data;

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
        async addProduct() {
            const formData = {
                name: this.newProduct.name,
                slug: this.newProduct.slug
            }
            console.log(formData)
            try {
                this.loading = true;
                const response = await axios.post(`/product`, formData);
                if (response.status == 200) {
                    this.showSuccessfulCreationProductToast()
                    this.newProduct.name = '',
                    this.newProduct.slug = ''
                }
                else {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                await this.getProducts(this.currentPage, this.selectedSort, this.filterModel);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async searchProducts() {
            try {
                this.currentPage = 1;
                localStorage.setItem('productCurrentPage',  this.currentPage);
                await this.getProducts(this.currentPage, this.selectedSort, this.filterModel);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async changePage(page) {
            this.loading = true;
            localStorage.setItem('productCurrentPage', page);
            this.currentPage = page
            await this.getProducts(page, this.selectedSort, this.filterModel);
            this.loading = false;
        },
        async changeSort() {
            this.loading = true;
            try {
                this.currentPage = 1;
                localStorage.setItem('productCurrentPage',  this.currentPage);
                localStorage.setItem('productSelectedSort',  this.selectedSort);
                await this.getProducts(this.currentPage, this.selectedSort, this.filterModel);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },

        async handleModelChange(event) {
            await this.getProducts(this.currentPage, this.selectedSort, this.filterModel);
            console.log("Выбранное значение:", event.target.value);
        },
        showSuccessfulCreationProductToast() {
            const successfulCreation = new Toast(document.getElementById('successfulCreationModelToast'))
            successfulCreation.show()
        },
        showErrorToast(errorCode, errorMessage) {
            const errorCreation = new Toast(document.getElementById('errorToast'));
            const errorBody = document.getElementById('errorToastBody');
            errorBody.textContent = 'Ошибка, ' + errorCode + ', ' + errorMessage;
            errorCreation.show();
        },
        setLoading(loading) {
            console.log("setLoading")
            this.loading = loading;
        },
        async handleProductDeleted() {
            console.log("handleProductDeleted")
            await this.getProducts(this.currentPage, this.selectedSort, this.filterModel);
        },
        async handleProductUpdated() {
            console.log("handleProductUpdated")
            await this.getProducts(this.currentPage, this.selectedSort, this.filterModel);
        }

    },
    watch: {
        async '$route'(to, from) {
            const model = this.$route.query['model'];
            if (model) {
                console.log('model:', model);
                localStorage.setItem('productfilterMode', model);
            } else {
                localStorage.setItem('productfilterMode', 0);
            }
            this.filterModel = localStorage.getItem('productfilterMode');

            await this.getProducts(this.currentPage, this.selectedSort, this.filterModel);
            await this.getModels()
        }
    }
}   

</script>