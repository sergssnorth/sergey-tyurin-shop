<template>
    <div class="container-fluid">
        <div class="d-block d-sm-none"> <!-- Видно на XS -->
            <div class="row justify-content-center mt-5">
                <div class="col-10">
                    <div class="card">
                        <div class="card-body">
                            <form @submit.prevent="submitForm" class="mb-3">
                                <div class="text-center">
                                    <h1>Вход</h1>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="" class="form-control" placeholder="name@example.com" v-model="username">
                                    <label for="floatingInput">Логин</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="password">
                                    <label for="floatingPassword">Пароль</label>
                                </div>
                                
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Войти</button>
                                </div>
                            </form>
                            <p class="card-text text-center">Или <router-link to="/sign-up">зарегистрируйтесь</router-link> прямо сейчас!</p>
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
                                    <h1>Вход</h1>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="" class="form-control" placeholder="name@example.com" v-model="username">
                                    <label for="floatingInput">Логин</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="password">
                                    <label for="floatingPassword">Пароль</label>
                                </div>
                                
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Войти</button>
                                </div>
                            </form>
                            <p class="card-text text-center">Или <router-link to="/sign-up">зарегистрируйтесь</router-link> прямо сейчас!</p>
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
                                    <h1>Вход</h1>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="" class="form-control" placeholder="name@example.com" v-model="username">
                                    <label for="floatingInput">Логин</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="password">
                                    <label for="floatingPassword">Пароль</label>
                                </div>
                                
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Войти</button>
                                </div>
                            </form>
                            <p class="card-text text-center">Или <router-link to="/sign-up">зарегистрируйтесь</router-link> прямо сейчас!</p>
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
                                    <h1>Вход</h1>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="" class="form-control" placeholder="name@example.com" v-model="username">
                                    <label for="floatingInput">Логин</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="password">
                                    <label for="floatingPassword">Пароль</label>
                                </div>
                                
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Войти</button>
                                </div>
                            </form>
                            <p class="card-text text-center">Или <router-link to="/sign-up">зарегистрируйтесь</router-link> прямо сейчас!</p>
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
                                    <h1>Вход</h1>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="" class="form-control" id="floatingInput" placeholder="name@example.com" v-model="username">
                                    <label for="floatingInput">Логин</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="password">
                                    <label for="floatingPassword">Пароль</label>
                                </div>
                                
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Войти</button>
                                </div>
                            </form>

                            <p class="card-text text-center">Или <router-link to="/sign-up">зарегистрируйтесь</router-link> прямо сейчас!</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
            <div class="d-none d-sm-block d-xl-none d-xxl-block d-lg-none d-xl-block d-md-none d-lg-block d-sm-none d-md-block"> <!-- Видно на всех -->
                <div class="row justify-content-center mt-5">
                <div class="col-4">
                    <div class="card">
                        <div class="card-body">
                            <form @submit.prevent="submitForm" class="mb-3">
                                <div class="text-center">
                                    <h1>Вход</h1>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="" class="form-control" placeholder="name@example.com" v-model="username">
                                    <label for="floatingInput">Логин</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="password" class="form-control" placeholder="Password" v-model="password">
                                    <label for="floatingPassword">Пароль</label>
                                </div>
                                
                                <div class="d-grid text-center">
                                    <button type="submit" class="btn btn-dark">Войти</button>
                                </div>
                            </form>

                            <p class="card-text text-center">Или <router-link to="/sign-up">зарегистрируйтесь</router-link> прямо сейчас!</p>
                        </div>
                    </div>
                
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: '',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Log In | Djackets'
    },
    methods: {
        async submitForm() {
            this.errors = []
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")

            if (this.username === '') {
                this.errors.push('Поле логин не заполнено!')
            }

            if (this.password === '') {
                this.errors.push('Поле пароль не заполнено!')
            }

            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }

                console.log(formData)
                
                await axios
                    .post("/api/v1/token/login/", formData)
                    .then(response => {
                        console.log(response)
                        const auth_token = response.data.auth_token

                        this.$store.commit('setToken', auth_token)
                        
                        axios.defaults.headers.common["Authorization"] = "Token " + auth_token

                        localStorage.setItem("token", auth_token)

                        const toPath = this.$route.query.to || '/'

                        this.$router.push(toPath)
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else {
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