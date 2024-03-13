<template>
    <div class="container-fluid text-center" style="height: 100%; display: flex; flex-direction: column;">
        <div class="row align-items-center mb-3">
            <div class="col-2">
                <select v-model="filter_big_category_id" class="form-select" aria-label="Default select example" @change="handleBigCategoryFilterChange">
                    <option :value="0">Все разделы</option>
                    <option v-for="big_category in big_categories" :key="big_category.id" :value="big_category.id">
                        {{ big_category.name }}
                    </option>
                </select>
            </div>
            <div class="col-2">
                <select v-model="filter_category_id" class="form-select" aria-label="Default select example" @change="handleCategoryFilterChange">
                    <option :value="0">Все категории</option>
                    <option v-for="category in categories" :key="category.id" :value="category.id">
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
                            <option v-for="big_category in big_categories" :key="big_category.id" :value="big_category.id">
                                {{ big_category.name }}
                            </option>
                        </select>

                        <select v-model="category_id" class="form-select py-3 mb-3" aria-label="Default select example">
                            <option :value="0">Выберите категорию</option>
                            <option v-for="category in categories" :key="category.id" :value="category.id">
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
              v-bind:big_categories="big_categories"
              v-bind:categories="categories"
              v-bind:collections="collections"
              @categoryDeleted="handleCategoryDeleted" 
              @categoryUpdated="handleCategoryUpdated"/>
          </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ListModels from '@/components/ListModels'

export default {
    name: 'Category',
    data() {
        return {
            filter_big_category_id: 0,
            filter_category_id: 0,
            filter_collection_id: 0,

            big_categories: [],
            categories: [],
            collections: [],
            models: [],

            list_select_big_categories: [],
            list_select_categories: [],
            list_select_collections: [],
            
            name: '',
            slug: '',
            description: '',
            big_category_id: 0,
            category_id: 0,
            collection_id: 0,
            FilterId: '',
        }
    },
    components: {
        ListModels
    },
    mounted() {
        console.log("mounted")
        this.getBigCategories()
        this.getCollections()
        this.getFilterId()

        const { big_category_id, category_id, collection_id } = this.$route.query;

        if (big_category_id !== '0') {
            const parsedBigCategoryId = parseInt(big_category_id, 10);
            this.filter_big_category_id = parsedBigCategoryId
        }

        if (category_id !== '0') {
            const parsedCategoryId = parseInt(category_id, 10);
            this.filter_category_id = parsedCategoryId
        }

        if (collection_id !== '0') {
            const parsedCollectionId = parseInt(collection_id, 10);
            this.filter_collection_id = parsedCollectionId
        }

        this.getCategories(this.filter_big_category_id)

            // Копирование значений из big_categories в list_select_big_categories
        this.list_select_big_categories = this.big_categories.slice();

        // Копирование значений из categories в list_select_categories
        this.list_select_categories = this.categories.slice();

        // Копирование значений из collections в list_select_collections
        this.list_select_collections = this.collections.slice();


        this.getModels(this.filter_big_category_id, this.filter_category_id, this.filter_collection_id)
    },
    methods: {
        getFilterId() {
            console.log('Метод getFilterId')
            this.filter_big_category_id = this.$route.query.big_category_id;
        },
        async getBigCategories() {
            console.log('Метод getBigCategories')
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
        async getCategories(filterId) {
            console.log('Метод getCategories')
            if (filterId !== undefined && filterId !== null) {
                console.log('Значение filterId:', filterId);
                const params = filterId !== '0' ? { big_category_id: filterId } : {};
                console.log(filterId)
                await axios
                    .get(`/categories`, { params })
                    .then(response => {
                        this.categories = response.data
                        console.log(this.categories)
                    })
                    .catch(error => {
                        console.log(error)
                    })
            } else {
                console.log('Значение filterId отсутствует');
                await axios
                .get(`/categories`)
                .then(response => {
                    this.categories = response.data
                    console.log(this.categories)
                })
                .catch(error => {
                    console.log(error)
                })
            }
        },
        async getCollections() {
            console.log('Метод getBigCategories')
            await axios
                .get(`/collections`)
                .then(response => {
                    this.collections = response.data
                    console.log(this.collections)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async getModels(big_category_filterId, category_filterId, collection_filterId) {
            console.log('Метод getModels')
            
            const params = {};

            if (big_category_filterId !== undefined && big_category_filterId !== null) {
                console.log('Значение big_category_filterId:', big_category_filterId);
                const parsedBigCategoryId = parseInt(big_category_filterId, 10);

                if (!isNaN(parsedBigCategoryId) && parsedBigCategoryId !== 0) {
                    params.big_category_id = parsedBigCategoryId;
                }
            }

            if (category_filterId !== undefined && category_filterId !== null) {
                console.log('Значение category_filterId:', category_filterId);
                const parsedCategoryId = parseInt(category_filterId, 10);

                if (!isNaN(parsedCategoryId) && parsedCategoryId !== 0) {
                    params.category_id = parsedCategoryId;
                }
            }

            if (collection_filterId !== undefined && collection_filterId !== null) {
                console.log('Значение collection_filterId:', collection_filterId);
                const parsedCollectionId = parseInt(collection_filterId, 10);

                if (!isNaN(parsedCollectionId) && parsedCollectionId !== 0) {
                    params.collection_id = parsedCollectionId;
                }
            }

            console.log(params);

            try {
                const response = await axios.get('/models', { params });
                this.models = response.data;
                console.log(this.models);
            } catch (error) {
                console.log(error);
            }
        },
        
        async addModel() {
            // let filterId;

            const formData = {
                name: this.name,
                slug: this.slug,
                description: this.description,
                category_id: this.category_id,
                collection_id: this.collection_id
            }
            console.log(formData)
            await axios
                .post(`/model`, formData)
                .then(response => {
                    console.log(response.data)
                    // filterId = this.getFilterId()
                    // this.getCategories(filterId);
                    //this.getModels(this.big_category_id, this.category_id, this.collection_id)
                    const queryString = `?big_category_id=${this.big_category_id}&category_id=${this.category_id}&collection_id=${this.collection_id}`;
                    this.$router.push(`/models${queryString}`);
                    
                    this.name = '',
                    this.slug = '',
                    this.description = '',
                    this.big_category_id = 0,
                    this.category_id = 0,
                    this.collection_id = 0

                })
                .catch(error => {
                    console.log(error)
                })
        },
        handleBigCategoryFilterChange() {
            
            console.log('Хендлер handleBigCategoryFilterChange');
            if (this.filter_category_id != 0) {
                this.filter_category_id = 0   
                const queryString = `?big_category_id=${this.filter_big_category_id}&category_id=${this.filter_category_id}&collection_id=${this.filter_collection_id}`;
                this.$router.push(`/models${queryString}`);
            }
            const queryString = `?big_category_id=${this.filter_big_category_id}&category_id=${this.filter_category_id}&collection_id=${this.filter_collection_id}`;

            this.$router.push(`/models${queryString}`);
        },
        handleBigCategoryFilterChangeCreateModal() {
            console.log('Хендлер handleBigCategoryFilterChangeCreateModal');
            this.category_id = 0
            this.getCategories(this.big_category_id)
        },

        handleCategoryFilterChange() {
            console.log('Хендлер handleCategoryFilterChange');
            const queryString = `?big_category_id=${this.filter_big_category_id}&category_id=${this.filter_category_id}&collection_id=${this.filter_collection_id}`;

            this.$router.push(`/models${queryString}`);
        },
        handleCollectionFilterChange() {
            console.log('Хендлер handleCollectionFilterChange');
            const queryString = `?big_category_id=${this.filter_big_category_id}&category_id=${this.filter_category_id}&collection_id=${this.filter_collection_id}`;

            this.$router.push(`/models${queryString}`);
        },

        handleCategoryDeleted() {
            console.log('Хендлер handleCategoryDeleted')
            const filterId = this.getFilterId()
            console.log('filterId')
            console.log(filterId)
            console.log('filterId')
            this.getCategories(filterId);
        },
        handleCategoryUpdated() {
            console.log('Хендлер handleCategoryUpdated')
            const filterId = this.getFilterId()
            console.log('filterId')
            console.log(filterId)
            console.log('filterId')
            this.getCategories(filterId);
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