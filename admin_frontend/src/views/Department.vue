<template>
    <div class="container-fluid text-center" style="height: 100%; display: flex; flex-direction: column;">
        <div class="row mb-3">
            <div class="d-flex align-items-center flex-grow-1">
                <div class="input-group align-items-center">
                    <span @click="searchDepartment" class="input-group-text" id="basic-addon1"
                        style="border-radius: 1.5rem 0 0 1.5rem;"><i class="bi bi-search"
                            style="font-size: 16px;"></i></span>
                    <input v-model="search" @keyup.enter="searchDepartment" type="text" class="form-control"
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

                    <button class="btn btn-icon mx-1 px-2 d-inline text-success" data-bs-toggle="modal"
                        data-bs-target="#сreateCategoryModal">
                        <i class="bi bi-box-seam" style="font-size: 18px;"></i>
                    </button>

                    <div class="modal fade" id="сreateCategoryModal" tabindex="-1" aria-labelledby="exampleModalLabel"
                        aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                            <div class="modal-content">
                                <div class="modal-header text-center">
                                    <h1 class="modal-title fs-5" id="exampleModalLabel">Создание отдела</h1>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal"
                                        aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                    <div class="form-floating mt-2 mb-3">
                                        <input type="text" class="form-control" placeholder="name@example.com"
                                            v-model="newDepartment.name">
                                        <label for="floatingInput">Наименование</label>
                                    </div>
                                </div>
                                <div class="modal-footer ">
                                    <button @click="addDepartment()" type="button" class="btn btn-second w-100"
                                        data-bs-dismiss="modal">Cоздать</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row flex-grow-1" id="department-list">
            <div class="col d-flex flex-column" style="flex-grow: 1;">

                <div v-if="loading">
                    <div class="text-center">
                        <div v-show="loading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>
                <div v-if="!loading">
                    <div v-if="departments.departments.length != 0">
                        <ListDepartments 
                        v-for="department in departments.departments" 
                        :key="department.id"
                        :department="department" 
                        :setLoading="setLoading"
                        :handleDepartmentDeleted="handleDepartmentDeleted"
                        :handleDepartmentUpdated="handleDepartmentUpdated" 
                        :loading="loading"
                        :showErrorToast="showErrorToast" />

                    </div>
                    <div v-else>
                        <span style="font-size: 1.3rem;">Коллекций пока нет ...</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col text-center">
                <nav class="px-0 py-0" aria-label="Навигация по страницам">
                    <ul class="my-2 pagination justify-content-center">
                        <li class="page-item page-item-pointer" v-if="departments.totalPages > 1 && currentPage > 1">
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
                            v-if="departments.totalPages > 1 && currentPage < departments.totalPages">
                            <a class="page-link" @click="changePage(currentPage + 1)" aria-label="Следующая">
                                <span aria-hidden="true">&raquo;</span>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="successfulCreationDepartmentToast" class="toast text-bg-success" role="alert" aria-live="assertive"
                aria-atomic="true" data-bs-delay="3000">
                <div class="d-flex">
                    <div class="toast-body">
                        Отдел успешно создан!
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

import ListDepartments from '@/components/ListDepartments'

export default {
    name: 'Department',
    data() {
        return {
            search: '',
            selectedSort: '',

            newDepartment: {
                name: '',
            },

            departments: {
                totalCount: 0,
                totalPages: 0,
                departments: []
            },

            loading: true,
            currentPage: 1,
        }
    },
    components: {
        ListDepartments,
    },
    computed: {
        displayedPages() {
            const totalDisplayPages = 5;
            const startPage = Math.max(1, this.currentPage - 2);
            const endPage = Math.min(this.departments.totalPages, startPage + totalDisplayPages - 1);

            let pages = [];

            if (startPage > 1) {
                pages.push(1, '...');
            }

            for (let i = startPage; i <= endPage; i++) {
                pages.push(i);
            }

            if (endPage < this.departments.totalPages) {
                pages.push('...', this.departments.totalPages);
            }

            return pages;
        }
    },
    async mounted() {
        this.currentPage = localStorage.getItem('departmentCurrentPage');

        if (!this.currentPage) {
            this.currentPage = 1;
            localStorage.setItem('departmentCurrentPage', this.currentPage);
        }

        this.selectedSort = localStorage.getItem('departmentSelectedSort');

        if (!this.selectedSort) {
            this.selectedSort = 'none';
            localStorage.setItem('departmentSelectedSort', this.selectedSort);
        }

        await this.getDepartments(this.currentPage, this.selectedSort);
    },
    methods: {
        async getDepartments(page, selectedSort) {
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
            try {
                this.loading = true;
                const response = await axios.get(`/departments`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, departments } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    departments: departments
                };
                this.departments = transformedData;
                console.log(this.departments);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async addDepartment() {
            const formData = {
                name: this.newDepartment.name,
                slug: this.newDepartment.slug,
                description: this.newDepartment.description,
            }
            console.log(formData)
            try {
                this.loading = true;
                const response = await axios.post(`/department`, formData);
                if (response.status == 200) {
                    this.showSuccessfulCreationDepartmentToast()
                    this.newDepartment.name = ''
                }
                else {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                await this.getDepartments(this.currentPage, this.selectedSort);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async searchDepartment() {
            try {
                this.currentPage = 1;
                localStorage.setItem('departmentCurrentPage', this.currentPage);
                await this.getDepartments(this.currentPage, this.selectedSort);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async changePage(page) {
            this.loading = true;
            localStorage.setItem('departmentCurrentPage', page);
            this.currentPage = page
            await this.getDepartments(page, this.selectedSort);
            this.loading = false;
        },
        async changeSort() {
            this.loading = true;
            try {
                this.currentPage = 1;
                localStorage.setItem('departmentCurrentPage', this.currentPage);
                localStorage.setItem('departmentSelectedSort', this.selectedSort);
                await this.getDepartments(this.currentPage, this.selectedSort);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        showSuccessfulCreationDepartmentToast() {
            const successfulCreation = new Toast(document.getElementById('successfulCreationDepartmentToast'))
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
        async handleDepartmentDeleted() {
            console.log("handleCategoryDeleted")
            await this.getDepartments(this.currentPage, this.selectedSort);
        },
        async handleDepartmentUpdated() {
            await this.getDepartments(this.currentPage, this.selectedSort);
        }
    },
}

</script>