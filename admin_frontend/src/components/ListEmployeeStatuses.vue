<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron"
        :style="cardBodyStyles">
            
            <div class="flex-grow-1 d-flex  align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.75rem;">
                <i class="bi bi-lightning-charge"></i>
                </span>
                <span>{{ dataEmployeeStatus.name }}</span>
                <span class="ms-auto"><i class="bi bi-hash"></i></span>
                <span class="" style="margin-right: 1.5rem;">{{ dataEmployeeStatus.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button class="btn btn-icon mx-1 px-2 d-inline text-success" @click="">
                    <i class="bi bi-plus-circle" style="font-size: 18px;"></i>
                </button>

                <button class="btn btn-icon mx-1 px-2 d-inline text-dark" @click="this.$router.push({ path: '/employees', query: { 'employeeStatus': dataEmployeeStatus.id } });">
                    <i class="bi bi-layers" style="font-size: 18px;"></i>
                </button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataEmployeeStatus.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                
                
                <div class="modal fade" :id="'editModal_' + dataEmployeeStatus.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение статуса сотрудника</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-employee="updatedEmployeeStatus.name">
                                    <label for="floatingInput">Имя</label>
                                </div>
                            </div>
                            <div class="modal-footer ">
                                <button @click="updateDepartment()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Изменить</button>
                            </div>
                        </div>
                    </div>
                </div>

                <button @click="deleteDepartment()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
            </div>
        </div>
        <div class="separator-card" v-show="isCollapsed"></div>
        <div :id="'collapseProduct' + dataEmployeeStatus.id" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
            <div class="card-body">
                <div v-if="employeeLoading">
                    <div class="text-center">
                        <div v-show="employeeLoading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>

                <div v-if="!employeeLoading">
                    <div v-if="dataEmployees.employees.length != 0">
                        <div v-for="employee in dataEmployees.employees" :key="employeeStatus.id" class="card mb-1" style="border-radius: 1.5rem;">
                            <div class="card-body elementSecondList py-1 px-3 d-flex align-items-center" id="headingExampleTwo" aria-controls="collapseIndicatorChevron">
                                <span style="margin-right: 0.5em;">{{ employee.id }}.</span>
                                <span>{{ employee.name }} {{ employee.sname }}</span>
                                <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                                <button @click="deleteBigCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                            </div>    
                        </div>
                    </div>
                    <div v-else>
                        <span>Сотрудников нет</span>
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
    name: 'ListDepartment',
    props: {
        employeeStatus: Object,

        showErrorToast: Function,
        setLoading: Function,
        loading: Boolean,
        handleEmployeeStatusUpdated: Function,
        handleEmployeeStatusDeleted: Function,
    },
    data() {
        return {
            isCollapsed : false,
            
            dataEmployeeStatus : this.employeeStatus,

            updatedEmployeeStatus: {
                name: '',
            },
            
            dataEmployees : {
                totalCount: 0,
                totalPages: 0,
                employees: []
            },
            
            employeeLoading: true,
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
        this.updatedEmployeeStatus = { ...this.employeeStatus };
    },
    methods: {
        async getEmployees(employeeStatusId) {
            this.employeeLoading = true;
            const params = {employee_status_id: employeeStatusId,
                            offset: 0,
                            limit: 20 }
            try {
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
                this.dataEmployees = transformedData;
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.employeeLoading = false;
            }
        },
        async updateDepartment() {
            const formData = {
                name: this.updatedEmployeeStatus.name,
            }
            this.setLoading(true);
            try {
                const response = await axios.put(`/employee-status/${this.dataEmployeeStatus.id}`, formData);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleEmployeeStatusUpdated()
            }
        },
        async deleteDepartment() {
            this.setLoading(true); // Включить индикатор загрузки
            try {
                const response = await axios.delete(`/employee-status/${this.dataEmployeeStatus.id}`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleEmployeeStatusDeleted()
            }
        },
        async toggleSeparator(event) {
            console.log("toggleSeparator")
            console.log(this.isCollapsed)
            console.log("toggleSeparator")

            // Подождем, чтобы Vue успел обновить isCollapsed
            await this.$nextTick();

            const collapseTarget = document.getElementById('collapseProduct' + this.dataEmployeeStatus.id);

            if (!this.isCollapsed) {
                new Collapse(collapseTarget, { toggle: false }).show();
            } else {
                new Collapse(collapseTarget, { toggle: false }).hide();
            }

            this.isCollapsed = !this.isCollapsed;

            if (this.isCollapsed) {
              await this.getEmployees(this.dataEmployeeStatus.id);
            }          
        },
    }
}
</script>
