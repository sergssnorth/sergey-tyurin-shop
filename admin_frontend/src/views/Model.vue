<template>
    <div class="container-fluid text-center">
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
            <div class="col-7">
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
                        <select v-model="big_category_id" class="form-select py-3" aria-label="Default select example">
                            <option :value="0">Выберите раздел</option>
                            <option v-for="big_category in big_categories" :key="big_category.id" :value="big_category.id">
                                {{ big_category.name }}
                            </option>
                        </select>
                    </div>
                    <div class="modal-footer ">
                        <button @click="addCategory()" type="button" class="btn btn-primary" data-bs-dismiss="modal">Cоздать</button>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
        <div class="row">
          <div class="col">
            <ListCategories 
              v-for="category in categories"
              v-bind:key="category.id"
              v-bind:category="category"
              v-bind:big_categories="big_categories"
              @categoryDeleted="handleCategoryDeleted" 
              @categoryUpdated="handleCategoryUpdated"/>
          </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ListCategories from '@/components/ListCategories'

export default {
    name: 'Category',
    data() {
        return {
            filter_big_category_id: 0,
            filter_category_id: 0,

            big_categories: [],
            categories: [],
            models: [],

            name: '',
            slug: '',
            big_category_id: 0,
            FilterId: '',
        }
    },
    components: {
        ListCategories
    },
    mounted() {
        console.log("mounted")
        this.getBigCategories()
        this.FilterId = this.getFilterId()
        this.getCategories(this.FilterId)
    },
    methods: {
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
        getFilterId() {
            console.log('Метод getFilterId')
            const filterId = this.$route.query.big_category_id;
            this.filter_big_category_id = filterId
            return filterId
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
        async getModels(filterId) {
            console.log('Метод getModels')
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
        async addCategory() {
            let filterId;

            const formData = {
                name: this.name,
                slug: this.slug,
                big_category_id: this.big_category_id
            }
            console.log(formData)
            await axios
                .post(`/category`, formData)
                .then(response => {
                    console.log(response.data)
                    filterId = this.getFilterId()
                    this.getCategories(filterId);
                    this.name = '',
                    this.slug = '',
                    this.big_category_id = 0
                })
                .catch(error => {
                    console.log(error)
                })
        },
        handleBigCategoryFilterChange() {
            
            console.log('Хендлер handleBigCategoryFilterChange');
            if (this.filter_category_id != 0) {
                this.filter_category_id = 0   
                const queryString = `?big_category_id=${this.filter_big_category_id}&category_id=${this.filter_category_id}`;
                this.$router.push(`/models${queryString}`);
            }
            const queryString = `?big_category_id=${this.filter_big_category_id}&category_id=${this.filter_category_id}`;

            this.$router.push(`/models${queryString}`);
        },

        handleCategoryFilterChange() {
            console.log('Хендлер handleCategoryFilterChange');
            const queryString = `?big_category_id=${this.filter_big_category_id}&category_id=${this.filter_category_id}`;

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
        const filterId = to.query.big_category_id;
        this.filter_big_category_id = filterId
        this.getCategories(filterId)

        next();
    },
}   

</script>