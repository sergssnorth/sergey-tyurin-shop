<template>
    <div class="container-fluid text-center" style="height: 100%; display: flex; flex-direction: column;">
        <div class="row mb-3">
            <div class="d-flex align-items-center flex-grow-1" >
                <div class="input-group align-items-center">
                    <span @click="searchSizeGuide" class="input-group-text" id="basic-addon1" style="border-radius: 1.5rem 0 0 1.5rem;"><i class="bi bi-search" style="font-size: 16px;"></i></span>
                    <input v-model="search" @keyup.enter="searchSizeGuide" type="text" class="form-control" aria-label="Username" aria-describedby="basic-addon1" style="border-radius: 0 1.5rem 1.5rem 0;">
                </div>
                <div class="d-flex align-items-center">
                    
                    <button @click="" class="btn btn-icon d-inline mx-1 px-2 custom-dropdown-toggle" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i v-if="selectedSort == 'none'" class="bi bi-filter-circle"></i>
                        <i v-else class="bi bi-filter-circle-fill" style="color: #696cff;"></i>
                    </button>

                    <div class="dropdown-menu" aria-labelledby="userDropdown" style="width: 20rem;">
                        <div class="row">
                            <div class="col">
                                <div class="separator mx-3 mb-2">Сортировка</div>
                                <div class="form-check mx-3 mb-2">
                                    <input
                                        class="form-check-input"
                                        type="radio"
                                        name="exampleRadios"
                                        id="exampleRadios0"
                                        value="none"
                                        v-model="selectedSort"
                                        @change="changeSort"
                                    />
                                    <label class="form-check-label" for="exampleRadios0">Отсутствует</label>
                                </div>
                                <div class="form-check mx-3 mb-2">
                                    <input
                                        class="form-check-input"
                                        type="radio"
                                        name="exampleRadios"
                                        id="exampleRadios1"
                                        value="name-asc"
                                        v-model="selectedSort"
                                        @change="changeSort"
                                    />
                                    <label class="form-check-label d-flex align-middle" for="exampleRadios1">
                                        <i class="bi bi-sort-up align-middle" style="margin-right: 0.25rem;"></i>
                                        <span>По имени</span>
                                    </label>
                                </div>
                                <div class="form-check mx-3 mb-2">
                                    <input
                                        class="form-check-input"
                                        type="radio"
                                        name="exampleRadios"
                                        id="exampleRadios2"
                                        value="name-desc"
                                        v-model="selectedSort"
                                        @change="changeSort"
                                    />
                                    <label class="form-check-label d-flex align-middle" for="exampleRadios2">
                                        <i class="bi bi-sort-down align-middle" style="margin-right: 0.25rem;"></i>
                                        <span>По имени</span>
                                    </label>
                                </div>
                                <div class="form-check mx-3 mb-2">
                                    <input
                                        ref="selectedSortInputId"
                                        class="form-check-input"
                                        type="radio"
                                        name="exampleRadios"
                                        id="exampleRadios3"
                                        value="id-asc"
                                        v-model="selectedSort"
                                        @change="changeSort"
                                    />
                                    <label class="form-check-label d-flex align-middle" for="exampleRadios3">
                                        <i class="bi bi-sort-up align-middle" style="margin-right: 0.25rem;"></i>
                                        <span>По id</span>
                                    </label>
                                </div>
                                <div class="form-check mx-3 mb-2">
                                    <input
                                        ref="selectedSortInputId"
                                        class="form-check-input"
                                        type="radio"
                                        name="exampleRadios"
                                        id="exampleRadios4"
                                        value="id-desc"
                                        v-model="selectedSort"
                                        @change="changeSort"
                                    />
                                    <label class="form-check-label d-flex align-middle" for="exampleRadios4">
                                        <i class="bi bi-sort-down align-middle" style="margin-right: 0.25rem;"></i>
                                        <span>По id</span>
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>                    

                    <button class="btn btn-icon mx-1 px-2 d-inline text-success" data-bs-toggle="modal" data-bs-target="#сreateCategoryModal">
                        <i class="bi bi-box-seam" style="font-size: 18px;"></i>
                    </button>
                    
                    <div class="modal fade" id="сreateCategoryModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                            <div class="modal-content">
                            <div class="modal-header text-center">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Создание размерной сетки</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mt-2 mb-3">
                                    <input type="text" class="form-control" placeholder="name@example.com" v-model="newSizeGuide.name">
                                    <label for="floatingInput">Имя</label>
                                </div>
                                <div class="mb-3 mx-2" style="text-align: start;">
                                    <label for="formFile" class="form-label">Изображение</label>
                                    <input class="form-control mb-3" type="file" id="formFile" @change="onFileChange">
                                    <img v-if="imagePreview" :src="imagePreview" class="img-fluid" alt="preview" />
                                </div>
                            </div>
                            <div class="modal-footer ">
                                <button @click="addSizeGuide()" type="button" class="btn btn-second w-100" data-bs-dismiss="modal">Cоздать</button>
                            </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row flex-grow-1" id="big-category-list">
            <div class="col d-flex flex-column" style="flex-grow: 1;">
            
                <div v-if="loading">
                    <div class="text-center">
                        <div v-show="loading" class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>
                <div v-if="!loading">
                    <div v-if="sizeGuides.sizeGuides.length != 0">
                        <ListSizeGuides
                        v-for="sizeGuide in sizeGuides.sizeGuides"
                        :key="sizeGuide.id"
                        :sizeGuide="sizeGuide"
                        :setLoading="setLoading"
                        :handleSizeGuideDeleted = "handleSizeGuideDeleted"
                        :handleSizeGuideUpdated = "handleSizeGuideUpdated"
                        :loading="loading"
                        :showErrorToast="showErrorToast"/>
                    </div>
                    <div v-else>
                        <span style="font-size: 1.3rem;">Размерных сеток пока нет ...</span>
                    </div>
                    
                </div>

            </div>
        </div>
        <div class="row">
            <div class="col text-center">
                <nav class="px-0 py-0" aria-label="Навигация по страницам">
                    <ul class="my-2 pagination justify-content-center">
                        <li class="page-item page-item-pointer" v-if="sizeGuides.totalPages > 1 && currentPage > 1">
                            <a class="page-link" @click="changePage(currentPage - 1)" aria-label="Предыдущая">
                            <span aria-hidden="true">&laquo;</span>
                            </a>
                        </li>
                        <li class="page-item page-item-pointer" v-for="page in displayedPages" :key="page">
                            <template v-if="page === '...'">
                            <span class="page-link">...</span>
                            </template>
                            <template v-else>
                            <a class="page-link" @click="changePage(page)" :class="{ 'active': page == currentPage }">{{ page }}</a>
                            </template>
                        </li>
                        <li class="page-item page-item-pointer" v-if="sizeGuides.totalPages > 1 && currentPage < sizeGuides.totalPages">
                            <a class="page-link" @click="changePage(currentPage + 1)" aria-label="Следующая">
                            <span aria-hidden="true">&raquo;</span>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="successfulCreationSizeGuideToast" class="toast text-bg-success" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="3000">
                <div class="d-flex">
                    <div class="toast-body">
                        Размерная сетка успешно создана!
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        </div>
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="errorToast" class="toast text-bg-danger" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="7000">
                <div class="d-flex">
                    <div class="toast-body" id="errorToastBody">
                        Ошибка ...
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { Toast } from 'bootstrap/dist/js/bootstrap.js'

import ListSizeGuides from '@/components/ListSizeGuides'

export default {
    name: 'SizeGuide',
    
    data() {
        return {
            imagePreview: null, 
            search: '',
            selectedSort: '',

            newSizeGuide: {
                name: '',
            },

            sizeGuides : {
                totalCount: 0,
                totalPages: 0,
                sizeGuides: []
            },

            loading : true,
            currentPage: 1,
        }
    },
    components: {
        ListSizeGuides,
    },
    computed: {
        displayedPages() {
            const totalDisplayPages = 5;
            const startPage = Math.max(1, this.currentPage - 2);
            const endPage = Math.min(this.sizeGuides.totalPages, startPage + totalDisplayPages - 1);

            let pages = [];

            if (startPage > 1) {
            pages.push(1, '...');
            }

            for (let i = startPage; i <= endPage; i++) {
            pages.push(i);
            }

            if (endPage < this.sizeGuides.totalPages) {
            pages.push('...', this.sizeGuides.totalPages);
            }

            return pages;
        }
    },
    async mounted() {
        this.currentPage = localStorage.getItem('sizeGuideCurrentPage');

        if (!this.currentPage) {
            this.currentPage = 1;
            localStorage.setItem('sizeGuideCurrentPage', this.currentPage);
        }

        this.selectedSort = localStorage.getItem('sizeGuideSelectedSort');

        if (!this.selectedSort) {
            this.selectedSort = 'none';
            localStorage.setItem('sizeGuideSelectedSort', this.selectedSort);
        }

        await this.getSizeGuides(this.currentPage, this.selectedSort);
    },
    methods: {
        async getSizeGuides(page, selectedSort) {
            console.log("getSizeGuides")
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
                const response = await axios.get(`/size-guides`, { params });
                if (!response.status == 200) {
                    this.showErrorToast(response.status, response.data)
                    console.log(response);
                }
                const { total_count, total_pages, size_guides } = response.data;

                // Преобразование ключей totalCount и totalPages
                const transformedData = {
                    totalCount: total_count,
                    totalPages: total_pages,
                    sizeGuides: size_guides
                };

                this.sizeGuides = transformedData;
                console.log(this.sizeGuides);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async addSizeGuide() {
            const formData = new FormData();
            formData.append('name', this.newSizeGuide.name);

            // Предполагаем, что у вас есть доступ к элементу ввода файла через ref="fileInput"
            const fileInput = document.querySelector('#formFile');
            if (fileInput.files[0]) {
                formData.append('image', fileInput.files[0]);
            }

            try {
                this.loading = true;
                const response = await axios.post(`/size-guide`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });

                if (response.status == 200) { // Проверяем, была ли размерная сетка успешно создана
                    this.showSuccessfulCreationSizeGuideToast();
                    this.newSizeGuide.name = '';
                    // Очищаем поле ввода файла
                    fileInput.value = '';
                } else {
                    this.showErrorToast(response.status, "Не удалось создать размерную сетку.");
                }

                await this.getSizeGuides(this.currentPage, this.selectedSort);
            } catch (error) {
                this.showErrorToast(error.response.status, error.response.data.detail);
            } finally {
                this.loading = false;
            }
        },
        async searchSizeGuide() {
            try {
                this.currentPage = 1;
                localStorage.setItem('sizeGuideCurrentPage',  this.currentPage);
                await this.getSizeGuides(this.currentPage, this.selectedSort);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async changePage(page) {
            this.loading = true;
            localStorage.setItem('sizeGuideCurrentPage', page);
            this.currentPage = page
            await this.getSizeGuides(page, this.selectedSort, this.filterBigCategory);
            this.loading = false;
        },
        async changeSort() {
            this.loading = true;
            try {
                this.currentPage = 1;
                localStorage.setItem('sizeGuideCurrentPage',  this.currentPage);
                localStorage.setItem('sizeGuideSelectedSort',  this.selectedSort);
                await this.getSizeGuides(this.currentPage, this.selectedSort);
            } catch (error) {
                this.showErrorToast(error.code, error.message);
                console.log(error);
            } finally {
                this.loading = false;
            }
        },

        showSuccessfulCreationSizeGuideToast() {
            const successfulCreation = new Toast(document.getElementById('successfulCreationSizeGuideToast'))
            successfulCreation.show()
        },
        showErrorToast(errorCode, errorMessage) {
            const errorCreation = new Toast(document.getElementById('errorToast'));
            const errorBody = document.getElementById('errorToastBody');
            errorBody.textContent = 'Ошибка, ' + errorCode + ', ' + errorMessage;
            errorCreation.show();
        },
        setLoading(loading) {
            console.log("setLoading")
            this.loading = loading;
        },
        async handleSizeGuideDeleted() {
            console.log("handleSizeGuideDeleted")
            await this.getSizeGuides(this.currentPage, this.selectedSort);
        },
        async handleSizeGuideUpdated() {
            console.log("handleSizeGuideUpdated")
            await this.getSizeGuides(this.currentPage, this.selectedSort);
        },
        onFileChange(e) {
            const file = e.target.files[0];
            if (file) {
                // Создаем URL для предпросмотра изображения
                this.imagePreview = URL.createObjectURL(file);
            }
        },

    },
}   

</script>