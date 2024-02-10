<template>
    <div class="container-fluid">
        <div class="row align-items-center mb-3">
            <div class="col-11">
                <div class="separator">{{ model.name }}</div>
            </div>
            
            <div class="col-1">
                <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#exampleModal"><i class="bi bi-file-earmark-plus" style="font-size: 20px"></i></button>
                <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                    <div class="modal-content">
                    <div class="modal-header text-center">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Добавить цвет</h1>
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
        <div class="row">
            <div class="col">
                <ListProduct 
                v-for="product in products"
                v-bind:key="product.id"
                v-bind:product="product"
                @productDeleted="handleCategoryDeleted" 
                @productUpdated="handleCategoryUpdated"/>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ListProduct from '@/components/ListProduct'

export default {
    name: 'Product',
    data() {
        return {
            model_id: 0,
            model: {},
            products: [],
        }
    },
    components: {
        ListProduct
    },

    mounted() {
        
        this.model_id = this.$route.params.model_id
        this.getModels(this.model_id)
        this.getProducts(this.model_id)
       
    },
    methods: {
        async getModels(model_id) {
            console.log('Метод getModels')
            
            const params = {};

            if (model_id !== undefined && model_id !== null) {
                console.log('Значение big_category_filterId:', model_id);
                const parsedModelId = parseInt(model_id, 10);

                if (!isNaN(parsedModelId) && parsedModelId !== 0) {
                    params.model_id = parsedModelId;
                }
            }
            console.log(params);

            try {
                const response = await axios.get('/models', { params });
                this.model = response.data[0];
                console.log(this.model);
            } catch (error) {
                console.log(error);
            }
        },
        async getProducts(model_id) {
            const params = { model_id: model_id}
            await axios
                .get(`/products`, { params })
                .then(response => {
                    this.products = response.data
                    console.log(this.collections)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async addProduct() {
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
    }
}

</script>

<style lang="scss">

.no-collapse {
  pointer-events: none;
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
  margin-right: 2em;
}

.separator:not(:empty)::after {
  margin-left: 2em;
}
</style>
