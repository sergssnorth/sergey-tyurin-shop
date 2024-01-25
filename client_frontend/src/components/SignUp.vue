<template>
    <div class="container-fluid">
        <div class="d-block d-sm-none"><!-- Видно на XS -->
            <div class="row justify-content-center mt-5">
                <div class="col-10">
                    <div class="card">
                        <div class="card-body">
                            <form @submit.prevent="submitForm" class="mb-3">
                                <div class="text-center">
                                    <h1>Регистрация</h1>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="" class="form-control"  placeholder="name@example.com" v-model="username">
                                    <label for="floatingInput">Логин</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="password">
                                    <label for="floatingPassword">Пароль</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="re_password">
                                    <label for="floatingPassword">Повторите пароль</label>
                                </div>
                                <div class="form-check mb-3">
                                    <input class="form-check-input" type="checkbox" id="gridCheck">
                                    <label class="form-check-label" for="gridCheck">
                                        Вы соглашаетесь c условиями <router-link to="/privacy-policies">политики конфиденциальности</router-link> и <router-link to="/personal-data-processing-policy">политикой обработки персональных данных</router-link>
                                    </label>
                                </div>
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Зарегистрироваться</button>
                                </div>
                            </form>
                        </div>
                    </div>    
                </div>
            </div>
        </div>
        <div class="d-none d-sm-block d-md-none"> <!-- Видно на SM -->
            <div class="row justify-content-center mt-5">
                <div class="col-10">
                    <div class="card">
                        <div class="card-body">
                            <form @submit.prevent="submitForm" class="mb-3">
                                <div class="text-center">
                                    <h1>Регистрация</h1>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="" class="form-control"  placeholder="name@example.com" v-model="username">
                                    <label for="floatingInput">Логин</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="password">
                                    <label for="floatingPassword">Пароль</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="re_password">
                                    <label for="floatingPassword">Повторите пароль</label>
                                </div>
                                <div class="form-check mb-3">
                                    <input class="form-check-input" type="checkbox" id="gridCheck">
                                    <label class="form-check-label" for="gridCheck">
                                        Вы соглашаетесь c условиями <router-link to="/privacy-policies">политики конфиденциальности</router-link> и <router-link to="/personal-data-processing-policy">политикой обработки персональных данных</router-link>
                                    </label>
                                </div>
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Зарегистрироваться</button>
                                </div>
                            </form>
                        </div>
                    </div>    
                </div>
            </div>
        </div>
        <div class="d-none d-md-block d-lg-none"><!-- Видно на MD --> 
            <div class="row justify-content-center mt-5">
                <div class="col-8">
                    <div class="card">
                        <div class="card-body">
                            <form @submit.prevent="submitForm" class="mb-3">
                                <div class="text-center">
                                    <h1>Регистрация</h1>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="" class="form-control"  placeholder="name@example.com" v-model="username">
                                    <label for="floatingInput">Логин</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="password">
                                    <label for="floatingPassword">Пароль</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="re_password">
                                    <label for="floatingPassword">Повторите пароль</label>
                                </div>
                                <div class="form-check mb-3">
                                    <input class="form-check-input" type="checkbox" id="gridCheck">
                                    <label class="form-check-label" for="gridCheck">
                                        Вы соглашаетесь c условиями <router-link to="/privacy-policies">политики конфиденциальности</router-link> и <router-link to="/personal-data-processing-policy">политикой обработки персональных данных</router-link>
                                    </label>
                                </div>
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Зарегистрироваться</button>
                                </div>
                            </form>
                        </div>
                    </div>    
                </div>
            </div>
        </div>
        <div class="d-none d-lg-block d-xl-none"><!-- Видно на LG --> 
            <div class="row justify-content-center mt-5">
                <div class="col-6">
                    <div class="card">
                        <div class="card-body">
                            <form @submit.prevent="submitForm" class="mb-3">
                                <div class="text-center">
                                    <h1>Регистрация</h1>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="" class="form-control"  placeholder="name@example.com" v-model="username">
                                    <label for="floatingInput">Логин</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="password">
                                    <label for="floatingPassword">Пароль</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="re_password">
                                    <label for="floatingPassword">Повторите пароль</label>
                                </div>
                                <div class="form-check mb-3">
                                    <input class="form-check-input" type="checkbox" id="gridCheck">
                                    <label class="form-check-label" for="gridCheck">
                                        Вы соглашаетесь c условиями <router-link to="/privacy-policies">политики конфиденциальности</router-link> и <router-link to="/personal-data-processing-policy">политикой обработки персональных данных</router-link>
                                    </label>
                                </div>
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Зарегистрироваться</button>
                                </div>
                            </form>
                        </div>
                    </div>    
                </div>
            </div>
        </div>
        <div class="d-none d-xl-block d-xxl-none"><!-- Видно на XL -->
            <div class="row justify-content-center mt-5">
                <div class="col-4">
                    <div class="card">
                        <div class="card-body">
                            <form @submit.prevent="submitForm" class="mb-3">
                                <div class="text-center">
                                    <h1>Регистрация</h1>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="" class="form-control"  placeholder="name@example.com" v-model="username">
                                    <label for="floatingInput">Логин</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="password">
                                    <label for="floatingPassword">Пароль</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="re_password">
                                    <label for="floatingPassword">Повторите пароль</label>
                                </div>
                                <div class="form-check mb-3">
                                    <input class="form-check-input" type="checkbox" id="gridCheck">
                                    <label class="form-check-label" for="gridCheck">
                                        Вы соглашаетесь c условиями <router-link to="/privacy-policies">политики конфиденциальности</router-link> и <router-link to="/personal-data-processing-policy">политикой обработки персональных данных</router-link>
                                    </label>
                                </div>
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Зарегистрироваться</button>
                                </div>
                            </form>
                        </div>
                    </div>    
                </div>
            </div>
        </div>
        <div class="d-none d-sm-block d-xl-none d-xxl-block d-lg-none d-xl-block d-md-none d-lg-block d-sm-none d-md-block"><!-- Видно на XXL -->
            <div class="row justify-content-center mt-5">
                <div class="col-4">
                    <div class="card">
                        <div class="card-body">
                            <form @submit.prevent="submitForm" class="mb-3">
                                <div class="text-center">
                                    <h1>Регистрация</h1>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="" class="form-control"  placeholder="name@example.com" v-model="username">
                                    <label for="floatingInput">Логин</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="password">
                                    <label for="floatingPassword">Пароль</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="re_password">
                                    <label for="floatingPassword">Повторите пароль</label>
                                </div>
                                <div class="form-check mb-3">
                                    <input class="form-check-input" type="checkbox" id="gridCheck">
                                    <label class="form-check-label" for="gridCheck">
                                        Вы соглашаетесь c условиями <router-link to="/privacy-policies">политики конфиденциальности</router-link> и <router-link to="/personal-data-processing-policy">политикой обработки персональных данных</router-link>
                                    </label>
                                </div>
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Зарегистрироваться</button>
                                </div>
                            </form>
                            <!-- <button type="button" @click="ShowToast" class="btn btn-primary" id="liveToastBtn">Show live toast</button> -->
                        </div>
                    </div>    
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { Toast } from 'bootstrap/dist/js/bootstrap.js'

export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            password: '',
            re_password: '',
            errors: []
        }
    },
    methods: {
        ShowToast() {
            const toastLiveExample = new Toast(document.getElementById('registrationToast'))
            toastLiveExample.show()
        },
        submitForm() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('Поле логин не заполнено!')
            }

            if (this.password === '') {
                this.errors.push('Поле пароль не заполнено!')
            }

            if (this.re_password === '') {
                this.errors.push('Поле поворите пароль не заполнено!')
            }


            if (this.password !== this.re_password) {
                this.errors.push('Поле пароль и повторите пароль не заполнено!')
            }

            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }

                axios
                    .post("/api/v1/users/", formData)
                    .then(response => {
                        const toastLiveExample = new Toast(document.getElementById('registrationToast'))
                        toastLiveExample.show()
                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }
}
</script>


<style lang="scss">
.row {
    padding-bottom: 10rem;
}
 
.card-body a {
    color: #333;
    text-decoration: none;
}
.card-body p {
    color: gray;
    text-decoration: none;
}


</style>