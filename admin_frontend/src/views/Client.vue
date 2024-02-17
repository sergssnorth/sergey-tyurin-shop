<template>
    <div class="container-fluid text-center" style="height: 100%; display: flex; flex-direction: column;">
        <div class="row mb-3">
            
            <div class="d-flex align-items-center flex-grow-1">
                <div class="input-group align-items-center">
                    <span class="input-group-text" id="basic-addon1" style="border-radius: 1.5rem 0 0 1.5rem;"><i class="bi bi-search" style="font-size: 16px;"></i></span>
                    <input v-model="search" type="text" class="form-control" aria-label="Username" aria-describedby="basic-addon1" style="border-radius: 0 1.5rem 1.5rem 0;">
                </div>
                <div class="d-flex align-items-center">
                    
                    <button @click="" class="btn btn-icon d-inline mx-1 px-2 custom-dropdown-toggle" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i class="bi bi-filter-circle"></i>
                    </button>

                    <div class="dropdown-menu" aria-labelledby="userDropdown" style="width: 20rem;">
                        <div class="row">
                            <div class="col">
                                <div class="separator mx-3 mb-2">Сортировка</div>
                                <div class="form-check form-switch mx-3 mb-2">
                                    <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
                                    <label class="form-check-label" for="flexSwitchCheckDefault">По ID</label>
                                </div>
                                <div class="form-check form-switch mx-3">
                                    <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
                                    <label class="form-check-label" for="flexSwitchCheckDefault">По Имени</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    
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
                    
                    <button @click="deleteCategory()" class="btn btn-icon d-inline text-success mx-1" style="padding: 0.25rem;"><i class="bi bi-person-add" style="font-size: 18px;"></i></button>    
                </div>
            </div>
        </div>
        <div class="row flex-grow-1" style="overflow-y: auto;">
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
                    v-for="client in filteredClients"
                    v-bind:key="client.id"
                    v-bind:client="client"
                    @clientDeleted="handleClientDeleted" 
                    @clientUpdated="handleClientUpdated"/>
                </div>

            </div>
        </div>
        <div class="row">
            <div class="col text-center">
                <nav class="px-0 py-0" aria-label="Page navigation">
                    <ul class="my-2 pagination justify-content-center">
                        <!-- Здесь вставьте код для пагинации Bootstrap -->
                        <li class="page-item">
                            <a class="page-link" href="#" aria-label="Previous">
                                <span aria-hidden="true">&laquo;</span>
                            </a>
                        </li>
                        <li class="page-item"><a class="page-link" href="#">1</a></li>
                        <li class="page-item"><a class="page-link" href="#">2</a></li>
                        <li class="page-item"><a class="page-link" href="#">3</a></li>
                        <li class="page-item">
                            <a class="page-link" href="#" aria-label="Next">
                                <span aria-hidden="true">&raquo;</span>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ListClients from '@/components/ListClients.vue'

export default {
    name: 'Client',
    data() {
        return {
            search: '',
            clients : [],
            loading : true
        }
    },
    computed: {
        filteredClients() {
            console.log("filteredClients")
            const clients =  this.clients.filter((client) => client.name.includes(this.search.toLowerCase()));
            return clients
      }
    },
    components: {
        ListClients
    },
    async mounted() {
        await this.getClients()
    },

    methods: {
        async getClients() {
            try {
                const response = await axios.get(`/clients`);
                this.clients = response.data;
                console.log(this.clients);
            } catch (error) {
                console.log(error);
            } finally {
                this.loading = false; // Установите loading в false после успешной загрузки или ошибки
            }
        },
        async getOrders() {
            await axios
                .get(`/clients`)
                .then(response => {
                    this.clients = response.data
                    console.log(this.clients)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        handleClientDeleted() {
          this.getClients();

        },
        handleClientUpdated() {
          console.log("handleCollectionUpdated")
          this.getClients();
        },
    },
    beforeRouteUpdate(to, from, next) {
        console.log('Хук beforeRouteUpdate');
        const big_category_filterId = to.query.big_category_id;
        const category_filterId = to.query.category_id;
        const collection_filterId = to.query.collection_id;

        this.filter_big_category_id = to.query.big_category_id;
        this.filter_category_id = to.query.category_id;
        this.filter_collection_id = to.query.collection_id;
        //this.filter_big_category_id = filterId
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


</style>
