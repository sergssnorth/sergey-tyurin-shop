<template>
    <div class="container-fluid text-center" style="height: 100%; display: flex; flex-direction: column;">
        <div class="row mb-3">
            <div class="d-flex align-items-center flex-grow-1">
                <div class="input-group align-items-center">
                    <span @click="searchOrders" class="input-group-text" id="basic-addon1"
                        style="border-radius: 1.5rem 0 0 1.5rem;"><i class="bi bi-search"
                            style="font-size: 16px;"></i></span>
                    <input v-model="search" @keyup.enter="searchOrders" type="text" class="form-control"
                        aria-label="Username" aria-describedby="basic-addon1" style="border-radius: 0 1.5rem 1.5rem 0;">
                </div>
                <div class="d-flex align-items-center">

                    <button @click="" class="btn btn-icon d-inline mx-1 px-2 custom-dropdown-toggle"
                        data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i v-if="selectedSort == 'none'" class="bi bi-filter-circle"></i>
                        <i v-else class="bi bi-filter-circle-fill" style="color: #696cff;"></i>
                    </button>

                    <div class="dropdown-menu" aria-labelledby="userDropdown" style="width: 20rem;">
                        <div class="row">
                            <div class="col">
                                <div class="separator mx-3 mb-2">Сортировка</div>
                                <div class="form-check mx-3 mb-2">
                                    <input class="form-check-input" type="radio" name="exampleRadios"
                                        id="exampleRadios0" value="none" v-model="selectedSort" @change="changeSort" />
                                    <label class="form-check-label" for="exampleRadios0">Отсутствует</label>
                                </div>
                                <div class="form-check mx-3 mb-2">
                                    <input class="form-check-input" type="radio" name="exampleRadios"
                                        id="exampleRadios1" value="name-asc" v-model="selectedSort"
                                        @change="changeSort" />
                                    <label class="form-check-label d-flex align-middle" for="exampleRadios1">
                                        <i class="bi bi-sort-up align-middle" style="margin-right: 0.25rem;"></i>
                                        <span>По имени</span>
                                    </label>
                                </div>
                                <div class="form-check mx-3 mb-2">
                                    <input class="form-check-input" type="radio" name="exampleRadios"
                                        id="exampleRadios2" value="name-desc" v-model="selectedSort"
                                        @change="changeSort" />
                                    <label class="form-check-label d-flex align-middle" for="exampleRadios2">
                                        <i class="bi bi-sort-down align-middle" style="margin-right: 0.25rem;"></i>
                                        <span>По имени</span>
                                    </label>
                                </div>
                                <div class="form-check mx-3 mb-2">
                                    <input ref="selectedSortInputId" class="form-check-input" type="radio"
                                        name="exampleRadios" id="exampleRadios3" value="id-asc" v-model="selectedSort"
                                        @change="changeSort" />
                                    <label class="form-check-label d-flex align-middle" for="exampleRadios3">
                                        <i class="bi bi-sort-up align-middle" style="margin-right: 0.25rem;"></i>
                                        <span>По id</span>
                                    </label>
                                </div>
                                <div class="form-check mx-3 mb-2">
                                    <input ref="selectedSortInputId" class="form-check-input" type="radio"
                                        name="exampleRadios" id="exampleRadios4" value="id-desc" v-model="selectedSort"
                                        @change="changeSort" />
                                    <label class="form-check-label d-flex align-middle" for="exampleRadios4">
                                        <i class="bi bi-sort-down align-middle" style="margin-right: 0.25rem;"></i>
                                        <span>По id</span>
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>

                    <button @click="" class="btn btn-icon d-inline mx-1 px-2 custom-dropdown-toggle"
                        data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i v-if="filterEmployee == 0" class="bi bi-funnel"></i>
                        <i v-else class="bi bi-funnel-fill" style="color: #696cff;"></i>
                    </button>

                    <div id="dropdown-menu-filter" class="dropdown-menu" aria-labelledby="userDropdown"
                        style="width: 20rem;">
                        <div class="row">
                            <div class="col">
                                <div class="separator mx-3 mb-2">Фильтры</div>
                                <select @change="handleEmployeeChange" v-model="filterEmployee"
                                    class="form-select mx-3 mb-2 py-2" style="width: 91%;"
                                    aria-label="Default select example">
                                    <option :value="0">Выберите работника</option>
                                    <option v-for="employe in employees.employees" :key="employe.id"
                                        :value="employee.id">
                                        {{ employee.name }} {{ employee.sname }}
                                    </option>
                                </select>
                                <select @change="handleOrderStatusChange" v-model="filterEmployee"
                                    class="form-select mx-3 mb-2 py-2" style="width: 91%;"
                                    aria-label="Default select example">
                                    <option :value="0">Выберите коллекцию</option>
                                    <option v-for="collection in collections.collections" :key="collection.id"
                                        :value="collection.id">
                                        {{ collection.name }}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <button class="btn btn-icon mx-1 px-2 d-inline text-success" data-bs-toggle="modal"
                        data-bs-target="#сreateModelModal">
                        <i class="bi bi-box-seam" style="font-size: 18px;"></i>
                    </button>

                    <div class="modal fade" id="сreateModelModal" tabindex="-1" aria-labelledby="exampleModalLabel"
                        aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                            <div class="modal-content">
                                <div class="modal-header text-center">
                                    <h1 class="modal-title fs-5" id="exampleModalLabel">Создание модели</h1>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal"
                                        aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                    <select v-model="newOrder.categoryId" class="form-select py-3 mt-2 mb-3"
                                        aria-label="Default select example">
                                        <option :value="0">Категория</option>
                                        <option v-for="category in categories.categories" :key="category.id"
                                            :value="category.id">
                                            {{ category.name }}
                                        </option>
                                    </select>
                                    <select v-model="newOrder.collectionId" class="form-select py-3 mb-3"
                                        aria-label="Default select example">
                                        <option :value="0">Коллекция</option>
                                        <option v-for="collection in collections.collections" :key="collection.id"
                                            :value="collection.id">
                                            {{ collection.name }}
                                        </option>
                                    </select>
                                    <select v-model="newOrder.detailId" class="form-select py-3 mb-3"
                                        aria-label="Default select example">
                                        <option :value="0">Описание</option>
                                        <option v-for="detail in details.details" :key="detail.id" :value="detail.id">
                                            {{ detail.name }}
                                        </option>
                                    </select>
                                    <select v-model="newOrder.sizeGuideId" class="form-select py-3 mb-3"
                                        aria-label="Default select example">
                                        <option :value="0">Размерная сетка</option>
                                        <option v-for="sideGuide in sizeGuides.sizeGuides" :key="sideGuide.id"
                                            :value="sideGuide.id">
                                            {{ sideGuide.name }}
                                        </option>
                                    </select>

                                    <div class="form-floating mt-2 mb-3">
                                        <input type="text" class="form-control" placeholder="name@example.com"
                                            v-model="newOrder.name">
                                        <label for="floatingInput">Имя</label>
                                    </div>
                                    <div class="form-floating mb-2">
                                        <input type="text" class="form-control" placeholder="Password"
                                            v-model="newOrder.slug">
                                        <label for="floatingPassword">Слаг</label>
                                    </div>
                                </div>
                                <div class="modal-footer ">
                                    <button @click="addModel()" type="button" class="btn btn-second w-100"
                                        data-bs-dismiss="modal">Cоздать</button>
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
                    <div v-if="orders.orders.length != 0">
                        <ListOrders 
                        v-for="model in orders.orders" 
                        :key="model.id" :model="model"
                        :categories="categories.categories" 
                        :collections="collections.collections"
                        :details="details.details" 
                        :sizeGuides="sizeGuides.sizeGuides" 
                        
                        :setLoading="setLoading"
                        :loading="loading" 
                        :handleOrderDeleted="handleOrderDeleted"  
                        :handleOrderUpdated="handleOrderUpdated" 
                        :showErrorToast="showErrorToast" />

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
                        <li class="page-item page-item-pointer" v-if="orders.totalPages > 1 && currentPage > 1">
                            <a class="page-link" @click="changePage(currentPage - 1)" aria-label="Предыдущая">
                                <span aria-hidden="true">&laquo;</span>
                            </a>
                        </li>
                        <li class="page-item page-item-pointer" v-for="page in displayedPages" :key="page">
                            <template v-if="page === '...'">
                                <span class="page-link">...</span>
                            </template>
                            <template v-else>
                                <a class="page-link" @click="changePage(page)"
                                    :class="{ 'active': page == currentPage }">{{ page }}</a>
                            </template>
                        </li>
                        <li class="page-item page-item-pointer"
                            v-if="orders.totalPages > 1 && currentPage < orders.totalPages">
                            <a class="page-link" @click="changePage(currentPage + 1)" aria-label="Следующая">
                                <span aria-hidden="true">&raquo;</span>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="successfulCreationOrderToast" class="toast text-bg-success" role="alert" aria-live="assertive"
                aria-atomic="true" data-bs-delay="3000">
                <div class="d-flex">
                    <div class="toast-body">
                        Модель успешно создана!
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"
                        aria-label="Close"></button>
                </div>
            </div>
        </div>
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="errorToast" class="toast text-bg-danger" role="alert" aria-live="assertive" aria-atomic="true"
                data-bs-delay="7000">
                <div class="d-flex">
                    <div class="toast-body" id="errorToastBody">
                        Ошибка ...
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"
                        aria-label="Close"></button>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios'
import { Toast } from 'bootstrap/dist/js/bootstrap.js'

import ListOrders from '@/components/ListOrders'

export default {
    name: 'Order',
    data() {
        return {
            search: '',
            selectedSort: '',

            filterEmployee: 0,
            filterOrderStatus: 0,

            newOrder: {
                userId: 0,
                name: "",
                sname: "",
                lname: "",
                phone: "",
                email: "",
                region: "",
                city: "",
                postal_code: "",
                employeeId: 0,
                orderStatusId: 0,
            },

            orders: {
                totalCount: 0,
                totalPages: 0,
                orders: []
            },

            employees: {
                totalCount: 0,
                totalPages: 0,
                employees: []
            },

            orderStatuses: {
                totalCount: 0,
                totalPages: 0,
                orderStatuses: []
            },

            loading: true,
            currentPage: 1,
        }
    },
    components: {
        ListOrders,
    },
    computed: {
        displayedPages() {
            const totalDisplayPages = 5;
            const startPage = Math.max(1, this.currentPage - 2);
            const endPage = Math.min(this.orders.totalPages, startPage + totalDisplayPages - 1);

            let pages = [];

            if (startPage > 1) {
                pages.push(1, '...');
            }

            for (let i = startPage; i <= endPage; i++) {
                pages.push(i);
            }

            if (endPage < this.orders.totalPages) {
                pages.push('...', this.orders.totalPages);
            }

            return pages;
        }
    },
    async mounted() {
        this.currentPage = localStorage.getItem('ordersCurrentPage');

        if (!this.currentPage) {
            this.currentPage = 1;
            localStorage.setItem('ordersCurrentPage', this.currentPage);
        }

        this.selectedSort = localStorage.getItem('ordersSelectedSort');

        if (!this.selectedSort) {
            this.selectedSort = 'none';
            localStorage.setItem('ordersSelectedSort', this.selectedSort);
        }

        this.filterEmployee = localStorage.getItem('orderFilterEmployee');

        if (!this.filterEmployee) {
            this.filterEmployee = 0;
            localStorage.setItem('orderFilterEmployee', this.filterEmployee);
        }

        this.filterOrderStatus = localStorage.getItem('orderFilterOrderStatus');

        if (!this.filterOrderStatus) {
            this.filterOrderStatus = 0;
            localStorage.setItem('orderFilterOrderStatus', this.filterOrderStatus);
        }


        await this.getOrders(this.currentPage, this.selectedSort, this.filterEmployee, this.filterOrderStatus); // ОСТАНОВИЛСЯ ТУТ ОСТАНОВИЛСЯ ТУТ
        await this.getEmployees()
        await this.getOrderStatuses()
        // await this.getCollections()
        // await this.getDetails()
        // await this.getSizeGuides()
    },
    methods: {
        async getEmployees() {
            try {
                this.loading = true;
                const response = await axios.get(`/employees`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, employees } = response.data;

                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    employees: employees
                };

                this.employees = transformedData;
                console.log(this.employees);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },

        async getOrderStatuses() {
            try {
                this.loading = true;
                const response = await axios.get(`/order-statuses`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, order_statuses } = response.data;

                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    orderStatuses: order_statuses
                };

                this.orderStatuses = transformedData;
                console.log(this.orderStatuses);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },

        

        async getOrders(page, selectedSort, filterEmployee, filterOrderStatus) {
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
            if (filterEmployee != 0) {
                console.log(filterEmployee)
                params.employee_id = filterEmployee;
            }
            if (filterOrderStatus != 0) {
                console.log(filterOrderStatus)
                params.order_status_id = filterOrderStatus;
            }

            try {
                this.loading = true;
                const response = await axios.get(`/orders`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, orders } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    orders: orders
                };

                this.orders = transformedData;
                console.log(this.orders);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },

        async addOrder() {
            const formData = {
                user_id: this.newOrder.userId,
                name: this.newOrder.name,
                sname: this.newOrder.sname, 
                lname: this.newOrder.lname,
                phone: this.newOrder.phone,
                email: this.newOrder.email,
                region: this.newOrder.region,
                city: this.newOrder.city,
                postal_code: this.newOrder.postal_code,
                employee_id: this.newOrder.employeeId,
                order_status_id: this.newOrder.orderStatusId,
            }
            console.log(formData)
            try {
                this.loading = true;
                const response = await axios.post(`/order`, formData);
                if (response.status == 200) {
                    this.showSuccessfulCreationOrderToast()
                    this.newOrder.this.newOrder.userId = null,
                    this.newOrder.name = "",
                    this.newOrder.sname = "",
                    this.newOrder.lname = "",
                    this.newOrder.phone = "",
                    this.newOrder.email = "",
                    this.newOrder.region = "",
                    this.newOrder.city = "",
                    this.newOrder.postal_code = "",
                    this.newOrder.employee_id = "",
                    this.newOrder.order_status_id = ""
                }
                else {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                await this.getOrders(this.currentPage, this.selectedSort, this.filterEmployee);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async searchOrders() {
            try {
                this.currentPage = 1;
                localStorage.setItem('ordersCurrentPage', this.currentPage);
                await this.getOrders(this.currentPage, this.selectedSort, this.filterEmployee);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async changePage(page) {
            this.loading = true;
            localStorage.setItem('ordersCurrentPage', page);
            this.currentPage = page
            await this.getOrders(page, this.selectedSort, this.filterEmployee);
            this.loading = false;
        },
        async changeSort() {
            this.loading = true;
            try {
                this.currentPage = 1;
                localStorage.setItem('ordersCurrentPage', this.currentPage);
                localStorage.setItem('ordersSelectedSort', this.selectedSort);
                await this.getOrders(this.currentPage, this.selectedSort, this.filterEmployee);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },

        async handleEmployeeChange(event) {
            await this.getOrders(this.currentPage, this.selectedSort, this.filterEmployee);
            console.log("Выбранное значение:", event.target.value);
        },
        async handleOrderStatusChange(event) {
            await this.getOrders(this.currentPage, this.selectedSort, this.filterEmployee);
            console.log("Выбранное значение:", event.target.value);
        },
        showSuccessfulCreationOrderToast() {
            const successfulCreation = new Toast(document.getElementById('successfulCreationOrderToast'))
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
        async handleOrderDeleted() {
            await this.getOrders(this.currentPage, this.selectedSort, this.filterEmployee);
        },
        async handleOrderUpdated() {
            await this.getOrders(this.currentPage, this.selectedSort, this.filterEmployee);
        }
    },
    // watch: {
    //     async '$route'(to, from) {
    //         const category = this.$route.query['category'];
    //         if (category) {
    //             console.log('category:', category);
    //             localStorage.setItem('orderFilterEmployee', category);
    //         } else {
    //             localStorage.setItem('orderFilterEmployee', 0);
    //         }
    //         this.filterEmployee = localStorage.getItem('orderFilterEmployee');

    //         await this.getOrders(this.currentPage, this.selectedSort, this.filterEmployee);
    //         await this.getCategories()
    //     }
    // }
    // data() {
    //     return {
    //         filter_big_category_id: 0,
    //         filter_category_id: 0,
    //         filter_collection_id: 0,

    //         big_orders: [],
    //         orders: [],
    //         collections: [],
    //         orders: [],

    //         list_select_big_orders: [],
    //         list_select_orders: [],
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
    //     Listorders
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

    //     this.getOrders(this.filter_big_category_id)

    //         // Копирование значений из big_orders в list_select_big_orders
    //     this.list_select_big_orders = this.big_orders.slice();

    //     // Копирование значений из orders в list_select_orders
    //     this.list_select_orders = this.orders.slice();

    //     // Копирование значений из collections в list_select_collections
    //     this.list_select_collections = this.collections.slice();


    //     this.getOrders(this.filter_big_category_id, this.filter_category_id, this.filter_collection_id)
    // },
    // methods: {
    //     getFilterId() {
    //         console.log('Метод getFilterId')
    //         this.filter_big_category_id = this.$route.query.big_category_id;
    //     },
    //     async getCategories() {
    //         console.log('Метод getCategories')
    //         await axios
    //             .get(`/big_orders`)
    //             .then(response => {
    //                 this.big_orders = response.data
    //                 console.log(this.big_orders)
    //             })
    //             .catch(error => {
    //                 console.log(error)
    //             })
    //     },
    //     async getOrders(filterId) {
    //         console.log('Метод getOrders')
    //         if (filterId !== undefined && filterId !== null) {
    //             console.log('Значение filterId:', filterId);
    //             const params = filterId !== '0' ? { big_category_id: filterId } : {};
    //             console.log(filterId)
    //             await axios
    //                 .get(`/orders`, { params })
    //                 .then(response => {
    //                     this.orders = response.data
    //                     console.log(this.orders)
    //                 })
    //                 .catch(error => {
    //                     console.log(error)
    //                 })
    //         } else {
    //             console.log('Значение filterId отсутствует');
    //             await axios
    //             .get(`/orders`)
    //             .then(response => {
    //                 this.orders = response.data
    //                 console.log(this.orders)
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
    //     async getOrders(big_category_filterId, category_filterId, collection_filterId) {
    //         console.log('Метод getOrders')

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
    //             const response = await axios.get('/orders', { params });
    //             this.orders = response.data;
    //             console.log(this.orders);
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
    //                 // this.getOrders(filterId);
    //                 //this.getOrders(this.big_category_id, this.category_id, this.collection_id)
    //                 const queryString = `?big_category_id=${this.big_category_id}&category_id=${this.category_id}&collection_id=${this.collection_id}`;
    //                 this.$router.push(`/orders${queryString}`);

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
    //             this.$router.push(`/orders${queryString}`);
    //         }
    //         const queryString = `?big_category_id=${this.filter_big_category_id}&category_id=${this.filter_category_id}&collection_id=${this.filter_collection_id}`;

    //         this.$router.push(`/orders${queryString}`);
    //     },
    //     handleBigCategoryFilterChangeCreateModal() {
    //         console.log('Хендлер handleBigCategoryFilterChangeCreateModal');
    //         this.category_id = 0
    //         this.getOrders(this.big_category_id)
    //     },

    //     handleCategoryFilterChange() {
    //         console.log('Хендлер handleCategoryFilterChange');
    //         const queryString = `?big_category_id=${this.filter_big_category_id}&category_id=${this.filter_category_id}&collection_id=${this.filter_collection_id}`;

    //         this.$router.push(`/orders${queryString}`);
    //     },
    //     handleCollectionFilterChange() {
    //         console.log('Хендлер handleCollectionFilterChange');
    //         const queryString = `?big_category_id=${this.filter_big_category_id}&category_id=${this.filter_category_id}&collection_id=${this.filter_collection_id}`;

    //         this.$router.push(`/orders${queryString}`);
    //     },

    //     handleCategoryDeleted() {
    //         console.log('Хендлер handleCategoryDeleted')
    //         const filterId = this.getFilterId()
    //         console.log('filterId')
    //         console.log(filterId)
    //         console.log('filterId')
    //         this.getOrders(filterId);
    //     },
    //     handleCategoryUpdated() {
    //         console.log('Хендлер handleCategoryUpdated')
    //         const filterId = this.getFilterId()
    //         console.log('filterId')
    //         console.log(filterId)
    //         console.log('filterId')
    //         this.getOrders(filterId);
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
    //     this.getOrders(big_category_filterId)
    //     this.getOrders(big_category_filterId, category_filterId, collection_filterId)

    //     next();
    // },
}

</script>