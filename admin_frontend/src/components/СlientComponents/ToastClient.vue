<template>
    <div class="toast-container position-fixed bottom-0 end-0 p-3">
        <div id="successfulCreationСlientToast" class="toast text-bg-success" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="1500">
            <div class="d-flex">
                <div class="toast-body">
                    Пользователь успешно создан!
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        </div>
    </div>
    <div class="toast-container position-fixed bottom-0 end-0 p-3">
        <div id="errorToast" class="toast text-bg-danger" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="7000">
            <div class="d-flex">
                <div class="toast-body" id="errorToastBody">
                    Ошибка при создании пользователя.
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        </div>
    </div>
</template>

<script>
import { Toast } from 'bootstrap/dist/js/bootstrap.js'

export default {
    name: 'ToastClient',
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
