<template>
    <div class="container-fluid text-center" style="height: 100%; display: flex; flex-direction: column;">
        <div class="row mb-3">
            
            <div class="d-flex align-items-center flex-grow-1">
                <div class="input-group align-items-center">
                    <span @click="searchBigCategories" class="input-group-text" id="basic-addon1" style="border-radius: 1.5rem 0 0 1.5rem;"><i class="bi bi-search" style="font-size: 16px;"></i></span>
                    <input v-model="search" @keyup.enter="searchBigCategories" type="text" class="form-control" aria-label="Username" aria-describedby="basic-addon1" style="border-radius: 0 1.5rem 1.5rem 0;">
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
                    
                    <button @click="deleteCategory()" class="btn btn-icon d-inline text-success mx-1" style="padding: 0.25rem;"><i class="bi bi-plus-square" style="font-size: 18px;"></i></button>    
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
                    <ListBigCategories 
                      v-for="big_category in big_categories"
                      v-bind:key="big_category.id"
                      v-bind:big_category="big_category"
                      @bigCategoryDeleted="handleBigCategoryDeleted" 
                      @bigCategoryUpdated="handleBigCategoryUpdated"/>
          
                </div>

            </div>
        </div>
        <div class="row">
            <div class="col text-center">
                <nav class="px-0 py-0" aria-label="Page navigation">
                    <ul class="my-2 pagination justify-content-center">
                        <li class="page-item" v-if="clients.total_pages > 1 && clients.current_page > 1">
                            <a class="page-link" @click="changePage(clients.current_page - 1)" aria-label="Previous">
                                <span aria-hidden="true">&laquo;</span>
                            </a>
                        </li>
                        <li class="page-item" v-for="page in Array.from({ length: clients.total_pages }, (_, i) => i + 1)">
                            <a class="page-link" @click="changePage(page)" :class="{ 'active': page === clients.current_page }">{{ page }}</a>
                        </li>
                        <li class="page-item" v-if="clients.total_pages > 1 && clients.current_page < clients.total_pages">
                            <a class="page-link" @click="changePage(clients.current_page + 1)" aria-label="Next">
                                <span aria-hidden="true">&raquo;</span>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </div>
    <!-- <div class="container-fluid text-center">
        <div class="row align-items-center mb-3">
          <div class="col-11">
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
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Создать раздел</h1>
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
                  </div>
                  <div class="modal-footer ">
                    <button @click="addBigCategory()" type="button" class="btn btn-primary" data-bs-dismiss="modal">Cоздать</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col">
            <ListBigCategories 
              v-for="big_category in big_categories"
              v-bind:key="big_category.id"
              v-bind:big_category="big_category"
              @bigCategoryDeleted="handleBigCategoryDeleted" 
              @bigCategoryUpdated="handleBigCategoryUpdated"/>
          </div>
        </div>
    </div> -->
</template>

<script>
import axios from 'axios'
import ListBigCategories from '@/components/ListBigCategories'

export default {
    name: 'BigCategory',
    data() {
        return {
            search: '',
            big_categories : {
                total_count: 0,
                total_pages: 0,
                big_categories: []
            },
            loading : true,
            
            name: '',
            slug: '',
        }
    },
    components: {
        ListBigCategories
    },
    async mounted() {
        let bigCategoryPage = localStorage.getItem('bigCategoryPage');

        if (!bigCategoryPage) {
            bigCategoryPage = 1;
            localStorage.setItem('bigCategoryPage', bigCategoryPage);
        }

        await this.getClients(clientPage);

        this.getBigCategories() 
    },
    methods: {
        async getBigCategories() {
            await axios
                .get(`/big_categories`)
                .then(response => {
                    this.big_categories = response.data
                    console.log(this.big_categories)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async addBigCategory() {
            const formData = {
                name: this.name,
                slug: this.slug
            }
            await axios
                .post(`/big_category`, formData)
                .then(response => {
                    console.log(response.data)
                    this.getBigCategories();
                })
                .catch(error => {
                    console.log(error)
                })
        },
        handleBigCategoryDeleted() {
          this.getBigCategories();
        },
        handleBigCategoryUpdated() {
        // Обновляем список категорий после обновления
          this.getBigCategories();
        },
    }
}   

</script>