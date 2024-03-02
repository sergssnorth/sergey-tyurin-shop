
<template>
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
</template>
  
<script>
  export default {
    name: 'SortingClient',
    data() {
        return {
            
        };
    },
    methods: {
        showSuccessfulCreationСlientToast() {
            const successfulCreation = new Toast(document.getElementById('successfulCreationСlientToast'))
            successfulCreation.show()
        },
        showErrorToast(errorCode, errorMessage) {
            const errorCreation = new Toast(document.getElementById('errorToast'));
            const errorBody = document.getElementById('errorToastBody');
            errorBody.textContent = 'Ошибка, ' + errorCode + ', ' + errorMessage;
            errorCreation.show();
        }
    },
}
</script>
