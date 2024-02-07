<template>
    <div class="container-fluid">
        <div class="row align-items-center mb-3">
            <div class="col-11">
                <div class="separator">Product name</div>
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
        <div class="row">
            <div class="col">
                <ListProduct 
                v-for="product in products"
                v-bind:key="product.id"
                v-bind:product="product"
                @productDeleted="handleCategoryDeleted" 
                @productUpdated="handleCategoryUpdated"/>

            </div>
            <div>
                <div class="card mb-1">
                    <a href="#collapseIndicatorChevron" class="card-body py-1 px-3 d-flex align-items-center" id="headingExampleTwo" data-bs-toggle="collapse" aria-expanded="false" aria-controls="collapseIndicatorChevron">
                        <span>Привет</span>
                        <span class="ms-auto" style="color: grey; margin-right: 0.5rem;"><i class="bi bi-boxes"></i></span>
                        <span class="" style="color: grey; margin-right: 1.5rem;">Привет</span>
                        <div class="vr" style="margin-right: 1.15rem;"></div>
                        <button class="btn btn-icon d-inline px-2"><i class="bi bi bi-box-seam"></i></button>
                        
                        
                    </a>


                    <div id="collapseIndicatorChevron" class="collapse" aria-labelledby="headingExampleTwo" data-bs-parent="#collapseIndicatorExampleOne" >
                    <div class="card-body">
                        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred.
                        <button class="btn">Text</button>
                    </div>
                    
                    </div>
                </div>
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
            products: [],
        }
    },
    components: {
        ListProduct
    },

    mounted() {
        this.model_id = this.$route.params.model_id
        this.getProducts(this.model_id)
    },
    methods: {
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
