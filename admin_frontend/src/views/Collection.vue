<template>
    <div class="container-fluid text-center">
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
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Создать коллекцию</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="name@example.com" v-model="new_name">
                      <label for="floatingInput">Имя</label>
                    </div>
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="Password" v-model="new_slug">
                      <label for="floatingPassword">Слаг</label>
                    </div>
                    <div class="form-floating mb-3">
                      <input type="text" class="form-control" placeholder="Password" v-model="new_description">
                      <label for="floatingPassword">Описание</label>
                    </div>
                  </div>
                  <div class="modal-footer ">
                    <button @click="addCollection()" type="button" class="btn btn-primary" data-bs-dismiss="modal">Cоздать</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col">
            <ListCollections
              v-for="collection in collections"
              v-bind:key="collection.id"
              v-bind:collection="collection"
              @collectionDeleted="handleCollectionDeleted" 
              @collectionUpdated="handleCollectionUpdated"/>
          </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ListCollections from '@/components/ListCollections'

export default {
    name: 'Collection',
    data() {
        return {
            collections: [],
            new_name: '',
            new_slug: '',
            new_description: '',
        }
    },
    components: {
        ListCollections
    },
    mounted() {
        this.getCollections() 
    },
    methods: {
        async getCollections() {
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
        async addCollection() {
            const formData = {
                name: this.new_name,
                slug: this.new_slug,
                description: this.new_description,
            }
            await axios
                .post(`/collection`, formData)
                .then(response => {
                    console.log(response.data)
                    this.new_name = ''
                    this.new_slug = ''
                    this.new_description = ''
                    this.getCollections();
                })
                .catch(error => {
                    console.log(error)
                })
        },
        handleCollectionDeleted() {
          this.getCollections();

        },
        handleCollectionUpdated() {
          console.log("handleCollectionUpdated")
          this.getCollections();
        },
    }
}   

</script>