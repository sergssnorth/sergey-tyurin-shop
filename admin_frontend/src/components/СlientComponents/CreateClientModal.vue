<template>
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
</template>

<script>
import axios from 'axios'

export default {
    name: 'CreateClientModal',
    data() {
        return {
        newClientName: "",
        newClientSlug: "",
        };
    },
    methods: {
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
    },
}
</script>
