<template>
    <div class="card mb-1" style="border-radius: 1.5rem;">
        <div class="card-body elementList py-1 px-3 d-flex" id="headingExampleTwo" aria-controls="collapseIndicatorChevron"
        :style="cardBodyStyles">
            
            <div class="flex-grow-1 d-flex  align-items-center" @click="toggleSeparator" style="">
                <span style="margin-right: 0.75rem;">
                <i class="bi bi-person-vcard"></i>
                </span>
                <span>{{ dataEmployee.name }} {{ dataEmployee.sname }}</span>
                <span class="ms-auto"><i class="bi bi-hash"></i></span>
                <span class="" style="margin-right: 1.5rem;">{{ dataEmployee.id }}</span>
            </div>
            
            <div class="vr" style="margin-right: 1.15rem;"></div>
            <div class="123123">
                <button class="btn btn-icon mx-1 px-2 d-inline text-success" @click="">
                    <i class="bi bi-plus-circle" style="font-size: 18px;"></i>
                </button>
                <button class="btn btn-icon mx-1 px-2 d-inline text-dark" @click="this.$router.push({ path: '/employees', query: { 'employee': dataEmployee.id } });">
                    <i class="bi bi-layers" style="font-size: 18px;"></i>
                </button>

                <button data-bs-toggle="modal" :data-bs-target="'#editModal_' + dataEmployee.id" class="btn btn-icon d-inline text-primary px-2"><i class="bi bi-pen"></i></button>
                
                
                <div class="modal fade" :id="'editModal_' + dataEmployee.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Изменение модели</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mt-2 mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="updatedEmployee.userId">
                                    <label for="floatingInput">Id пользвателя</label>
                                </div>
                                <div class="form-floating mt-2 mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="updatedEmployee.name">
                                    <label for="floatingInput">Имя</label>
                                </div>
                                <div class="form-floating mt-2 mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="updatedEmployee.sname">
                                    <label for="floatingInput">Фамилия</label>
                                </div>
                                <select v-model="updatedEmployee.employeeStatusId" class="form-select py-3 mt-2 mb-3" aria-label="Default select example">
                                    <option :value="0">Статус сотрудника</option>
                                    <option v-for="employeeStatus in employeeStatuses" :key="employeeStatus.id" :value="employeeStatus.id">
                                        {{ employeeStatus.name }}
                                    </option>
                                </select>
                                <select v-model="updatedEmployee.departmentId" class="form-select py-3 mb-3" aria-label="Default select example">
                                    <option :value="0">Отдел</option>
                                    <option v-for="department in departments" :key="department.id" :value="department.id">
                                        {{ department.name }}
                                    </option>
                                </select>
                            </div>
                            <div class="modal-footer ">
                                <button @click="updateEmployee()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Изменить</button>
                            </div>
                        </div>
                    </div>
                </div>
                <button @click="deleteEmployee()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
            </div>
        </div>
        <div class="separator-card" v-show="isCollapsed"></div>
        <div :id="'collapseEmployee' + dataEmployee.id" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
            <div class="card-body">
                <div v-if="ordersLoading">
                    <div class="text-center">
                        <div v-show="ordersLoading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>

                <div v-if="!ordersLoading">
                    <div v-if="dataOrdes.orders.length != 0">
                        <div v-for="order in dataOrdes.orders" :key="order.id" class="card mb-2" style="border-radius: 1.5rem;">
                            <div class="card-body elementSecondList py-1 px-3 d-flex align-items-center" id="headingExampleTwo" aria-controls="collapseIndicatorChevron">
                                <span style="margin-right: 0.5em;">{{ order.id }}.</span>
                                <span>{{ order.email }}</span>
                                <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-icon d-inline text-primary ms-auto px-2"><i class="bi bi-pen"></i></button>
                                <button @click="deleteProduct()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                            </div>
                        </div>
                    </div>
                    <div v-else style="text-align: start;">
                        <span>Продуктов нет</span>

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
    name: 'ListEmployees',
    props: {
        employee: Object,
        employeeStatuses: Array,
        departments: Array,

        showErrorToast: Function,
        setLoading: Function,
        loading: Boolean,
        handleEmployeeUpdated: Function,
        handleEmployeeDeleted: Function,
    },
    data() {
        return {
            isCollapsed : false,

            dataEmployee : this.employee,

            updatedEmployee: {
                userId: 0,
                name: "",
                sname: "",
                employeeStatusId: 0,
                departmentId: 0
            },
            
            dataOrdes : {
                totalCount: 0,
                totalPages: 0,
                orders: []
            },
            
            ordersLoading: true,
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
        this.updatedEmployee.userId = this.employee.userId === null ? 0 : this.employee.userId
        this.updatedEmployee.name =  this.employee.name === null ? "" : this.employee.name;
        this.updatedEmployee.sname = this.employee.sname === null ? "" : this.employee.sname;
        this.updatedEmployee.employeeStatusId = this.employee.employeeStatusId === null ? 0 : this.employee.employeeStatusId;
        this.updatedEmployee.departmentId = this.employee.departmentId === null ? 0 : this.employee.departmentId;
        console.log(this.employee)
    },
    methods: {
        async getOrders(employeeId) {
            this.ordersLoading = true;
            const params = { employee_id: employeeId,
                            offset: 0,
                            limit: 20 }
            try {
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
                this.dataOrdes = transformedData;
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.ordersLoading = false;
            }
        },
        async updateEmployee() {
            const formData = {
                userId: this.updatedEmployee.userId,
                name: this.updatedEmployee.name,
                sname: this.updatedEmployee.sname,
                employeeStatusId: this.updatedEmployee.employeeStatusId,
                departmentId: this.updatedEmployee.departmentId,
            }
            this.setLoading(true);
            try {
                const response = await axios.put(`/employee/${this.dataEmployee.id}`, formData);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleEmployeeUpdated()
            }
        },
        async deleteEmployee() {
            this.setLoading(true);
            try {
                const response = await axios.delete(`/employee/${this.dataEmployee.id}`);
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.error(error);
            } finally {
                this.setLoading(false);
                await this.handleEmployeeDeleted()
            }
        },
        async toggleSeparator(event) {
            console.log("toggleSeparator")
            console.log(this.isCollapsed)
            console.log("toggleSeparator")

            // Подождем, чтобы Vue успел обновить isCollapsed
            await this.$nextTick();

            const collapseTarget = document.getElementById('collapseEmployee' + this.dataEmployee.id);

            if (!this.isCollapsed) {
                new Collapse(collapseTarget, { toggle: false }).show();
            } else {
                new Collapse(collapseTarget, { toggle: false }).hide();
            }

            this.isCollapsed = !this.isCollapsed;

            if (this.isCollapsed) {
              await this.getOrders(this.dataEmployee.id);
            }          
        },
    }
}
</script>
