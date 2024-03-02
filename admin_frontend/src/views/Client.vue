<template>
    <div class="container-fluid text-center" style="height: 100%; display: flex; flex-direction: column;">
        <div class="row mb-3">
            
            <div class="d-flex align-items-center flex-grow-1">
                <div class="input-group align-items-center">
                    <span @click="searchClients" class="input-group-text" id="basic-addon1" style="border-radius: 1.5rem 0 0 1.5rem;"><i class="bi bi-search" style="font-size: 16px;"></i></span>
                    <input v-model="search" @keyup.enter="searchClients" type="text" class="form-control" aria-label="Username" aria-describedby="basic-addon1" style="border-radius: 0 1.5rem 1.5rem 0;">
                </div>
                <div class="d-flex align-items-center">
                    
                    <button @click="" class="btn btn-icon d-inline mx-1 px-2 custom-dropdown-toggle" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i v-if="selectedSort == 'none'" class="bi bi-filter-circle"></i>
                        <i v-else class="bi bi-filter-circle-fill" style="color: #696cff;"></i>
                    </button>

                    <SortingClient/>

                    <button @click="" class="btn btn-icon d-inline mx-1 px-2 custom-dropdown-toggle" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i class="bi bi-funnel"></i>            
                    </button>

                    <div class="dropdown-menu" aria-labelledby="userDropdown" style="width: 20rem;">
                        <div class="row">
                            <div class="col">
                                <div class="separator mx-3 mb-2">Фильтры</div>
                                <select class="form-select mx-3 mb-2" style="width: 91%;" required aria-label="select example">
                                    <option value="">Open</option>
                                    <option value="1">One</option>
                                    <option value="2">Two</option>
                                    <option value="3">Three</option>
                                </select>
                                <select class="form-select mx-3 mb-2" style="width: 91%;" required aria-label="select example">
                                    <option value="">Open</option>
                                    <option value="1">One</option>
                                    <option value="2">Two</option>
                                    <option value="3">Three</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    


                    <button class="btn btn-icon mx-1 px-2 d-inline text-success" data-bs-toggle="modal" data-bs-target="#сreateUserModal">
                        <i class="bi bi-person-add" style="font-size: 18px;"></i>
                    </button>
                    
                    <div class="modal fade" id="сreateUserModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                            <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Создание клиента</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mt-2 mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="newClientName">
                                    <label for="floatingInput">Имя</label>
                                </div>
                                <div class="form-floating mb-2">
                                    <input type="text" class="form-control" placeholder="Password" v-model="newClientSlug">
                                    <label for="floatingPassword">Слаг</label>
                                </div>
                            </div>
                            <div class="modal-footer ">
                                <button @click="addClient()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Cоздать</button>
                            </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row flex-grow-1" id="clientlist">
            <div class="col d-flex flex-column" style="flex-grow: 1;">
            
                <div v-if="loading">
                    <div class="text-center">
                        <div v-show="loading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>
                <div v-if="!loading">
                    <div class="col d-flex flex-column" style="flex-grow: 1;"></div>
                    <ListClients
                    v-for="client in clients.clients"
                    v-bind:key="client.id"
                    v-bind:client="client"
                    @clientDeleted="handleClientDeleted" 
                    @clientUpdated="handleClientUpdated"/>
                </div>

            </div>
        </div>
        <div class="row">
            <div class="col text-center">
                <nav class="px-0 py-0" aria-label="Навигация по страницам">
                    <ul class="my-2 pagination justify-content-center">
                        <li class="page-item page-item-pointer" v-if="clients.total_pages > 1 && current_page > 1">
                            <a class="page-link" @click="changePage(current_page - 1)" aria-label="Предыдущая">
                            <span aria-hidden="true">&laquo;</span>
                            </a>
                        </li>
                        <li class="page-item page-item-pointer" v-for="page in displayedPages" :key="page">
                            <template v-if="page === '...'">
                            <span class="page-link">...</span>
                            </template>
                            <template v-else>
                            <a class="page-link" @click="changePage(page)" :class="{ 'active': page == current_page }">{{ page }}</a>
                            </template>
                        </li>
                        <li class="page-item page-item-pointer" v-if="clients.total_pages > 1 && current_page < clients.total_pages">
                            <a class="page-link" @click="changePage(current_page + 1)" aria-label="Следующая">
                            <span aria-hidden="true">&raquo;</span>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
        <!-- <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="successfulCreationСlientToast" class="toast text-bg-success" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="1500">
                <div class="d-flex">
                    <div class="toast-body">
                        Пользователь успешно создан!
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        </div>
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="errorToast" class="toast text-bg-danger" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="7000">
                <div class="d-flex">
                    <div class="toast-body" id="errorToastBody">
                        Ошибка при создании пользователя.
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        </div> -->
        <ToastClient />
    </div>
</template>

<script>
import axios from 'axios'

import CreateClientModal from '@/components/СlientComponents/CreateClientModal.vue'
import SortingClient from '@/components/СlientComponents/SortingClient.vue'
import ToastClient from '@/components/СlientComponents/ToastClient.vue'
import ListClients from '@/components/ListClients.vue'

export default {
    name: 'Client',
    data() {
        return {
            search: '',
            isActiveFilter: true,
            selectedSort: '',

            clients : {
                total_count: 0,
                total_pages: 0,
                clients: []
            },

            loading : true,
            current_page: 1,
        }
    },
    components: {
        CreateClientModal,
        SortingClient,
        ToastClient,
        ListClients,
    },
    computed: {
        displayedPages() {
            const totalDisplayPages = 5;
            const startPage = Math.max(1, this.current_page - 2);
            const endPage = Math.min(this.clients.total_pages, startPage + totalDisplayPages - 1);

            let pages = [];

            if (startPage > 1) {
            pages.push(1, '...');
            }

            for (let i = startPage; i <= endPage; i++) {
            pages.push(i);
            }

            if (endPage < this.clients.total_pages) {
            pages.push('...', this.clients.total_pages);
            }

            return pages;
        }
    },
    async mounted() {
        this.current_page = localStorage.getItem('clientCurrentPage');

        if (!this.current_page) {
            this.current_page = 1;
            localStorage.setItem('clientCurrentPage', this.current_page);
        }

        this.selectedSort = localStorage.getItem('clientSelectedSort');

        if (!this.selectedSort) {
            this.selectedSort = 'none';
            localStorage.setItem('clientSelectedSort', this.selectedSort);
        }

        await this.getClients(this.current_page, this.selectedSort);
    },
    methods: {
        async getClients(page, selectedSort) {
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
                const response = await axios.get(`/clients`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                this.clients = response.data;
                console.log(this.clients);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async addClient() {
            const formData = {
                name: this.newClientName,
                slug: this.newClientSlug
            }
            try {
                this.loading = true;
                const response = await axios.post(`/client`, formData);
                if (response.status == 200) {
                    this.showSuccessfulCreationСlientToast()
                }
                else {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                await this.getClients(this.current_page, this.selectedSort);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async searchClients() {
            try {
                this.current_page = 1;
                localStorage.setItem('clientCurrentPage',  this.current_page);
                await this.getClients(this.current_page, this.selectedSort);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async changePage(page) {
            this.loading = true;
            localStorage.setItem('clientCurrentPage', page);
            this.current_page = page
            await this.getClients(page, this.selectedSort);
            this.loading = false;
        },
        async changeSort() {
            this.loading = true;
            try {
                this.current_page = 1;
                localStorage.setItem('clientCurrentPage',  this.current_page);
                await this.getClients(this.current_page, this.selectedSort);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        handleClientDeleted() {
          this.getClients();

        },
        handleClientUpdated() {
          console.log("handleCollectionUpdated")
          this.getClients();
        },
        // showSuccessfulCreationСlientToast() {
        //     const successfulCreation = new Toast(document.getElementById('successfulCreationСlientToast'))
        //     successfulCreation.show()
        // },
        // showErrorToast(errorCode, errorMessage) {
        //     const errorCreation = new Toast(document.getElementById('errorToast'));
        //     const errorBody = document.getElementById('errorToastBody');
        //     errorBody.textContent = 'Ошибка, ' + errorCode + ', ' + errorMessage;
        //     errorCreation.show();
        // },
    },
    beforeRouteUpdate(to, from, next) {
        console.log('Хук beforeRouteUpdate');
        const big_category_filterId = to.query.big_category_id;
        const category_filterId = to.query.category_id;
        const collection_filterId = to.query.collection_id;

        this.filter_big_category_id = to.query.big_category_id;
        this.filter_category_id = to.query.category_id;
        this.filter_collection_id = to.query.collection_id;

        this.getCategories(big_category_filterId)
        this.getModels(big_category_filterId, category_filterId, collection_filterId)

        next();
    },
}   

</script>

<style lang="scss">

i {
    font-size: 18px;
}

.custom-badge {
    font-size: 14px; 
    color: #333;
}

.page-item-pointer{ 
    cursor: pointer;
}
.page-item-pointer{ 
    cursor: pointer;
}


.separator {
  display: flex;
  align-items: center;
  text-align: center;
}

.separator::before,
.separator::after {
  content: '';
  flex: 1;
  border-bottom: 1px solid #b4b4b4;
}

.separator:not(:empty)::before {
  margin-right: 1rem;
}

.separator:not(:empty)::after {
  margin-left: 1rem;
}

button.btn {
    border-radius: 0.75rem;
}

#clientlist {
    overflow-y: auto;
}

#clientlist::-webkit-scrollbar {
    width: 8px;
}

#clientlist::-webkit-scrollbar-track {
    border-radius: 8px;
    background-color: #e7e7e7;
    border: 1px solid #cacaca;
}

#clientlist::-webkit-scrollbar-thumb {
    border-radius: 8px;
    background-color: #696cff;
}

input {
    border-radius: 0;
}

.input-group-text:hover {
    cursor: pointer;
}

input:focus,
input:active {
    box-shadow: none !important;
}
</style>
