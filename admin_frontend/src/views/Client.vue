<template>
    <div class="container-fluid text-center">
        <div class="row mb-3">
            <div class="d-flex align-items-center flex-grow-1">
                <div class="input-group align-items-center">
                    <span class="input-group-text" id="basic-addon1"><i class="bi bi-search"></i></span>
                    <input v-model="search" type="text" class="form-control" aria-label="Username" aria-describedby="basic-addon1">
                </div>
                <div class="d-flex align-items-center m-3">
                    <button @click="deleteCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>    
                    <button @click="deleteCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                    <button @click="deleteCategory()" class="btn btn-icon d-inline text-danger px-2"><i class="bi bi-trash3"></i></button>
                </div>
            </div>
        </div>  
        <div class="row">

            <!-- <div v-for="client in filteredClients" :key="client.id"> -->
                
            </div>
            <ListClients
              v-for="client in filteredClients"
              v-bind:key="client.id"
              v-bind:client="client"
              @clientDeleted="handleClientDeleted" 
              @clientUpdated="handleClientUpdated"/>
        <!-- </div>   -->
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

        
        }
    },
    computed: {
        filteredClients() {
        console.log("filteredClients")
            const clients =  this.clients.filter((client) => client.name.includes(this.search.toLowerCase()));
            console.log(clients)
            return clients
        //   return this.options.filter((option) => option.value.includes(this.search.toLowerCase()));
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