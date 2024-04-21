<template>
    <div class="container-fluid text-center" style="height: 100%; display: flex; flex-direction: column;">
        <div class="row mb-3">
            <div class="d-flex align-items-center flex-grow-1" >
                <div class="input-group align-items-center">
                    <span @click="searchEmployees" class="input-group-text" id="basic-addon1" style="border-radius: 1.5rem 0 0 1.5rem;"><i class="bi bi-search" style="font-size: 16px;"></i></span>
                    <input v-model="search" @keyup.enter="searchEmployees" type="text" class="form-control" aria-label="Username" aria-describedby="basic-addon1" style="border-radius: 0 1.5rem 1.5rem 0;">
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
                        <i v-if="filterEmployeeStatus == 0" class="bi bi-funnel"></i>
                        <i v-else class="bi bi-funnel-fill" style="color: #696cff;"></i>
                    </button>

                    <div id="dropdown-menu-filter" class="dropdown-menu" aria-labelledby="userDropdown" style="width: 20rem;">
                        <div class="row">
                            <div class="col">
                                <div class="separator mx-3 mb-2">Фильтры</div>
                                <select @change="handleEmployeeStatusChange" v-model="filterEmployeeStatus" class="form-select mx-3 mb-2 py-2" style="width: 91%;" aria-label="Default select example">
                                    <option :value="0">Выберите cтатус</option>
                                    <option v-for="employeeStatus in employeeStatuses.employeeStatuses" :key="employeeStatus.id" :value="employeeStatus.id">
                                        {{ employeeStatus.name }}
                                    </option>
                                </select>
                                <select @change="handleDepartmentChange" v-model="filterDepartment" class="form-select mx-3 mb-2 py-2" style="width: 91%;" aria-label="Default select example">
                                    <option :value="0">Выберите отдел</option>
                                    <option v-for="department in departments.departments" :key="department.id" :value="department.id">
                                        {{ department.name }}
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
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Создание сотрудника</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mt-2 mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="newEmployee.userId">
                                    <label for="floatingInput">Id пользвателя</label>
                                </div>
                                <div class="form-floating mt-2 mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="newEmployee.name">
                                    <label for="floatingInput">Имя</label>
                                </div>
                                <div class="form-floating mt-2 mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="newEmployee.sname">
                                    <label for="floatingInput">Фамилия</label>
                                </div>
                                <select v-model="newEmployee.employeeStatusId" class="form-select py-3 mt-2 mb-3" aria-label="Default select example">
                                    <option :value="0">Статус сотрудника</option>
                                    <option v-for="employeeStatus in employeeStatuses.employeeStatuses" :key="employeeStatus.id" :value="employeeStatus.id">
                                        {{ employeeStatus.name }}
                                    </option>
                                </select>
                                <select v-model="newEmployee.departmentId" class="form-select py-3 mb-3" aria-label="Default select example">
                                    <option :value="0">Отдел</option>
                                    <option v-for="department in departments.departments" :key="department.id" :value="department.id">
                                        {{ department.name }}
                                    </option>
                                </select>

                            </div>
                            <div class="modal-footer ">
                                <button @click="addEmployee()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Cоздать</button>
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
                    <div v-if="employees.employees.length != 0">
                        <ListEmployees
                        v-for="employee in employees.employees"
                        :key="employee.id"
                        :employee="employee"
                        :employeeStatuses="employeeStatuses.employeeStatuses"
                        :departments="departments.departments"

                        :setLoading="setLoading"
                        :loading="loading"
                        :handleEmployeeDeleted = "handleEmployeeDeleted"
                        :handleEmployeeUpdated = "handleEmployeeUpdated"
                        :showErrorToast="showErrorToast"/>

                    </div>
                    <div v-else>
                        <span style="font-size: 1.3rem;">Сотрудников пока нет ...</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col text-center">
                <nav class="px-0 py-0" aria-label="Навигация по страницам">
                    <ul class="my-2 pagination justify-content-center">
                        <li class="page-item page-item-pointer" v-if="employees.totalPages > 1 && currentPage > 1">
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
                        <li class="page-item page-item-pointer" v-if="employees.totalPages > 1 && currentPage < employees.totalPages">
                            <a class="page-link" @click="changePage(currentPage + 1)" aria-label="Следующая">
                            <span aria-hidden="true">&raquo;</span>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="successfulCreationEmployeeToast" class="toast text-bg-success" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="3000">
                <div class="d-flex">
                    <div class="toast-body">
                        Сотрудник успешно создан!
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

import ListEmployees from '@/components/ListEmployees'

export default {
    name: 'Employee',
    
    data() {
        return {
            search: '',
            selectedSort: '',

            filterEmployeeStatus: 0,
            filterDepartment: 0,

            newEmployee: {
                userId: 0,
                name: "",
                sname: "",
                employeeStatusId: 0,
                departmentId: 0
            },

            employees : {
                totalCount: 0,
                totalPages: 0,
                employees: []
            },

            departments: {
                totalCount: 0,
                totalPages: 0,
                departments: []
            },

            employeeStatuses: {
                totalCount: 0,
                totalPages: 0,
                employeeStatuses: []
            },

            loading : true,
            currentPage: 1,
        }
    },
    components: {
        ListEmployees,
    },
    computed: {
        displayedPages() {
            const totalDisplayPages = 5;
            const startPage = Math.max(1, this.currentPage - 2);
            const endPage = Math.min(this.employees.totalPages, startPage + totalDisplayPages - 1);

            let pages = [];

            if (startPage > 1) {
            pages.push(1, '...');
            }

            for (let i = startPage; i <= endPage; i++) {
            pages.push(i);
            }

            if (endPage < this.employees.totalPages) {
            pages.push('...', this.employees.totalPages);
            }

            return pages;
        }
    },
    created() {
        const employeeStatus = this.$route.query['employee-status'];
        if (employeeStatus) {
            console.log('employeeStatus:', employeeStatus);
            localStorage.setItem('modelFilterEmployeeStatus', employeeStatus);
        } else {
            localStorage.setItem('modelFilterEmployeeStatus', 0);
        }

        const department = this.$route.query['department'];
        if (department) {
            console.log('department:', department);
            localStorage.setItem('modelFilterDepartment', department);
        } else {
            localStorage.setItem('modelFilterDepartment', 0);
        }
    },
    async mounted() {
        this.currentPage = localStorage.getItem('employeesCurrentPage');

        if (!this.currentPage) {
            this.currentPage = 1;
            localStorage.setItem('employeesCurrentPage', this.currentPage);
        }

        this.selectedSort = localStorage.getItem('employeesSelectedSort');

        if (!this.selectedSort) {
            this.selectedSort = 'none';
            localStorage.setItem('employeesSelectedSort', this.selectedSort);
        }

        this.filterEmployeeStatus = localStorage.getItem('modelFilterEmployeeStatus');

        if (!this.filterEmployeeStatus) {
            this.filterEmployeeStatus = 0;
            localStorage.setItem('modelFilterEmployeeStatus', this.filterEmployeeStatus);
        }

        this.filterDepartment = localStorage.getItem('modelFilterDepatment');

        if (!this.filterDepartment) {
            this.filterDepartment = 0;
            localStorage.setItem('modelFilterDepatment', this.filterDepartment);
        }


        await this.getEmployees(this.currentPage, this.selectedSort, this.filterEmployeeStatus, this.filterDepartment);
        await this.getDepartments()
        await this.getEmployeeStatuses()
    },
    methods: {
        async getDepartments() {
            try {
                this.loading = true;
                const response = await axios.get(`/departments`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, departments } = response.data;

                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    departments: departments
                };

                this.departments = transformedData;
                console.log(this.categories);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async getEmployeeStatuses() {
            try {
                this.loading = true;
                const response = await axios.get(`/employee-statuses`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, employee_statuses } = response.data;

                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    employeeStatuses: employee_statuses
                };

                this.employeeStatuses = transformedData;
                console.log(this.collections);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },

        async getEmployees(page, selectedSort, filterEmployeeStatus, filterDepartment) {
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
            if (filterEmployeeStatus != 0) {
                console.log(filterEmployeeStatus)
                params.employee_status_id = filterEmployeeStatus;
            }
            if (filterDepartment != 0) {
                console.log(filterDepartment)
                params.department_id = filterDepartment;
            }

            try {
                this.loading = true;
                const response = await axios.get(`/employees`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, employees } = response.data;

                // Преобразование ключей totalCount и totalPages
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

        async addEmployee() {
            const formData = {
                user_id: this.newEmployee.userId,
                employee_status_id: this.newEmployee.employeeStatusId,
                department_id: this.newEmployee.departmentId,
            }
            console.log(formData)
            try {
                this.loading = true;
                const response = await axios.post(`/employee`, formData);
                if (response.status == 200) {
                    this.showSuccessfulCreationEmployeeToast()
                    this.newEmployee.userId = 0,
                    this.newEmployee.employeeStatusId = 0,
                    this.newEmployee.departmentId = 0
                }
                else {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                await this.getEmployees(this.currentPage, this.selectedSort, this.filterEmployeeStatus);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async searchEmployees() {
            try {
                this.currentPage = 1;
                localStorage.setItem('employeesCurrentPage',  this.currentPage);
                await this.getEmployees(this.currentPage, this.selectedSort, this.filterEmployeeStatus, this.filterDepartment);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async changePage(page) {
            this.loading = true;
            localStorage.setItem('employeesCurrentPage', page);
            this.currentPage = page
            await this.getEmployees(page, this.selectedSort, this.filterEmployeeStatus, this.filterDepartment);
            this.loading = false;
        },
        async changeSort() {
            this.loading = true;
            try {
                this.currentPage = 1;
                localStorage.setItem('employeesCurrentPage',  this.currentPage);
                localStorage.setItem('employeesSelectedSort',  this.selectedSort);
                await this.getEmployees(this.currentPage, this.selectedSort, this.filterEmployeeStatus, this.filterDepartment);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },

        async handleEmployeeStatusChange(event) {
            await this.getEmployees(this.currentPage, this.selectedSort, this.filterEmployeeStatus, this.filterDepartment);
            console.log("Выбранное значение:", event.target.value);
        },
        async handleDepartmentChange(event) {
            await this.getEmployees(this.currentPage, this.selectedSort, this.filterEmployeeStatus, this.filterDepartment);
            console.log("Выбранное значение:", event.target.value);
        },
        showSuccessfulCreationEmployeeToast() {
            const successfulCreation = new Toast(document.getElementById('successfulCreationEmployeeToast'))
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
        async handleEmployeeDeleted() {
            await this.getEmployees(this.currentPage, this.selectedSort, this.filterEmployeeStatus, this.filterDepartment);
        },
        async handleEmployeeUpdated() {
            await this.getEmployees(this.currentPage, this.selectedSort, this.filterEmployeeStatus, this.filterDepartment);
        }
    },
    watch: {
        async '$route'(to, from) {
            const employeeStatus = this.$route.query['employee-status'];
            if (employeeStatus) {
                console.log('employeeStatus:', employeeStatus);
                localStorage.setItem('modelFilterEmployeeStatus', employeeStatus);
            } else {
                localStorage.setItem('modelFilterEmployeeStatus', 0);
            }

            const department = this.$route.query['department'];
            if (department) {
                console.log('department:', department);
                localStorage.setItem('modelFilterDepartment', department);
            } else {
                localStorage.setItem('modelFilterDepartment', 0);
            }

            this.filterEmployeeStatus = localStorage.getItem('modelFilterEmployeeStatus')
            this.filterDepartment = localStorage.getItem('modelFilterDepartment')

            await this.getEmployees(this.currentPage, this.selectedSort, this.filterEmployeeStatus, this.filterDepartment);
            await this.getDepartments()
            await this.getEmployeeStatuses()
        }
    }
}   

</script>
