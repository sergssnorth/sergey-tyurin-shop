<template>
    <nav class="navbar fixed-top navbar-expand-lg shadow-sm px-3 mb-5 bg-body">
        <div class="container-fluid px-0 justify-content-between">
            
            <div class="d-lg-none d-flex align-items-center">
                <button class="navbar-toggler" type="button" @click = "turnOnNavbar" data-bs-toggle="collapse" data-bs-target="#navbarCategories" aria-controls="navbarCategories" aria-expanded="false" aria-label="Toggle navigation">
                    <i class="bi bi-heart" style="font-size: 20px"></i>
                </button>
                <router-link to="/my-account">
                    <i class="px-2 bi bi-person-circle" style="font-size: 24px"></i>
                </router-link>
            </div>
            

            <div class="d-lg-none">
                <router-link to="/">
                    <a class="navbar-brand" href="#" style="padding: 0; margin: 0;">
                        <img src="@/assets/ShortLogo.png" width="89" height="28">
                    </a>
                </router-link>
            </div>

            <div class="d-lg-none">
                <div class="">
                    <template v-if="favoriteTotalLength > 0">
                        <router-link to="/favorite">
                            <i class="px-2 bi bi-bookmark-heart position-relative" style="font-size: 24px">
                                <span class="badge position-absolute bottom-0 start-85 translate-middle bg-dark border border-light rounded-circle">
                                    {{ favoriteTotalLength }}
                                    <span class="visually-hidden">unread messages</span>
                                </span>
                            </i>
                        </router-link>
                    </template>
                    
                    <template v-else>
                        <router-link to="/favorite">
                            <i class="px-2 bi bi-bookmark-heart" style="font-size: 24px"></i>
                        </router-link>
                    </template>
    

                    <template v-if="cartTotalLength > 0">
                        <router-link to="/cart">
                            <i class="px-2 bi bi-bag position-relative" style="font-size: 24px">
                                <span class="badge position-absolute top-10 start-55 translate-middle-x rounded-pill bg-dark border border-light rounded-circle">
                                    {{ cartTotalLength }}
                                    <span class="visually-hidden">unread messages</span>
                                </span>
                            </i>
                        </router-link>
                    </template>

                    <template v-else>
                        <router-link to="/cart">
                            <i class="px-2 bi bi-bag" style="font-size: 24px"></i>
                        </router-link>
                    </template>
                </div>
            </div>


            <div class="collapse navbar-collapse" id="navbarCategories">

                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li v-for="big_category in categories" class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            {{big_category[0].big_category.name}}
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li v-for="category in big_category"><a class="dropdown-item">
                                <router-link v-bind:to="category.get_absolute_url" class="custom_a is-size-6" @click="showMobileMenu =!showMobileMenu">
                                    {{ category.name }}
                                </router-link></a>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>  

        

            <div class="collapse navbar-collapse justify-content-center" id="navbarLogo">
                <router-link to="/">
                    <a class="navbar-brand" href="#" style="margin-right: 0">
                        <img src="@/assets/LogoST.png" width="168" height="28">
                    </a>
                </router-link>
            </div>
            
            <div class="collapse navbar-collapse justify-content-end" id="navbarMenu">
                <div class="">
                    <router-link to="/my-account">
                        <i class="px-2 bi bi-person-circle" style="font-size: 24px"></i>
                    </router-link>

                    <template v-if="favoriteTotalLength > 0">
                        <router-link to="/favorite">
                            <i class="px-2 bi bi-bookmark-heart position-relative" style="font-size: 24px">
                                <span class="badge position-absolute bottom-0 start-85 translate-middle bg-dark border border-light rounded-circle">
                                    {{ favoriteTotalLength }}
                                    <span class="visually-hidden">unread messages</span>
                                </span>
                            </i>
                        </router-link>
                    </template>
                    
                    <template v-else>
                        <router-link to="/favorite">
                            <i class="px-2 bi bi-bookmark-heart" style="font-size: 24px"></i>
                        </router-link>
                    </template>
    

                    <template v-if="cartTotalLength > 0">
                        <router-link to="/cart">
                            <i class="px-2 bi bi-bag position-relative" style="font-size: 24px">
                                <span class="badge position-absolute top-10 start-55 translate-middle-x rounded-pill bg-dark border border-light rounded-circle">
                                    {{ cartTotalLength }}
                                    <span class="visually-hidden">unread messages</span>
                                </span>
                            </i>
                        </router-link>
                    </template>

                    <template v-else>
                        <router-link to="/cart">
                            <i class="px-2 bi bi-bag" style="font-size: 24px"></i>
                        </router-link>
                    </template>
                </div>
            </div>
        </div>
    </nav>


    <section class="section is-spaced" style="">
        <div class="toast-container position-fixed top-0 end-0 p-3">
            <div id="registrationToast" class="toast text-bg-dark" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="1500">
                <div class="toast-header">
                <strong class="me-auto">Сергей Тюрин</strong>
                <small>Сейчас</small>
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div class="toast-body">
                    Вы успешно зарегистрировались!
                </div>
            </div>
        </div>

      <router-view/>
    </section>
    
    <div class="container">
        <footer class="row row-cols-1 row-cols-sm-2 row-cols-md-5 py-5 border-top">
            <div class="col mb-3">
            <a href="/" class="d-flex align-items-center mb-3 link-body-emphasis text-decoration-none">
                <svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
            </a>
            <p class="text-body-secondary">&copy; 2023</p>
            </div>

            <div class="col mb-3">

            </div>

            <div class="col mb-3">
            <h5>Section</h5>
            <ul class="nav flex-column">
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Home</a></li>
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Features</a></li>
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Pricing</a></li>
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">FAQs</a></li>
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">About</a></li>
            </ul>
            </div>

            <div class="col mb-3">
            <h5>Section</h5>
            <ul class="nav flex-column">
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Home</a></li>
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Features</a></li>
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Pricing</a></li>
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">FAQs</a></li>
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">About</a></li>
            </ul>
            </div>

            <div class="col mb-3">
            <h5>Section</h5>
            <ul class="nav flex-column">
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Home</a></li>
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Features</a></li>
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">Pricing</a></li>
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">FAQs</a></li>
                <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-body-secondary">About</a></li>
            </ul>
            </div>
        </footer>
        </div>
    
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            visibleNavbar: false,
            showCategoryMen: false,
            showMobileMenu: false,
            cart: {
                items: []
            },
            favorite: {
                items: []
            },
            big_categories: [],
            categories: [],

        }
    },
    beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
    },
    async mounted() {
        document.body.classList.add('has-navbar-fixed-top')
        this.cart = this.$store.state.cart
        this.favorite = this.$store.state.favorite
        await this.getBigCategories()
        await this.getCategories()
    },
    computed: {
        cartTotalLength() {
            let totalLength = 0
            console.log("Карта")
            console.log(this.cart.items)
            console.log("Карта")
            for (let i = 0; i < this.cart.items.length; i++) {
                totalLength += this.cart.items[i].quantity
            }
            if (totalLength == 0) {
                return ''
            }
            console.log("totalLength")
            console.log(totalLength)
            console.log("totalLength")
            return totalLength
        },
        favoriteTotalLength() {
            let totalLength = 0
            for (let i = 0; i < this.favorite.items.length; i++) {
                totalLength += 1
            }
            if (totalLength == 0) {
                return totalLength
            }
            return totalLength
        }
    },
    methods: {
        turnOnNavbar() {
            this.visibleNavbar = !this.visibleNavbar
        },
        async getBigCategories() {
            this.$store.commit('setIsLoading', true)
            await axios
                .get('/api/v1/big-categories/')
                    .then(response => {
                        this.big_categories = response.data
                        console.log(this.big_categories)
                    })
                    .catch(error => {
                        console.log(error)
                    })
            this.$store.commit('setIsLoading', false)
        },

        async getCategories() {
            this.$store.commit('setIsLoading', true)

            
            var big_categories = this.big_categories
            await Promise.all(
                big_categories.map(async (big_category) => {
                await axios
                    .get(`/api/v1/categories/${big_category.slug}/`)
                    .then(response => {
                        this.categories.push(response.data)
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }))
            console.log("1")
            console.log(this.categories)
            console.log("1")
            
            this.$store.commit('setIsLoading', false)
        },
    }
}
</script>


<style lang="scss">
@import "../node_modules/bootstrap/scss/functions";
@import "../node_modules/bootstrap/scss/variables";
@import "../node_modules/bootstrap/scss/variables-dark";


body { padding-top: 72px; }

@media (max-width: 991px) {
    nav.navbar {
        min-height: 52px;
        --bs-navbar-toggler-focus-width: 0.10rem;
    }

    body { padding-top: 52px; }


}



nav {
    min-height: 72px;
}

i {
    font-style: normal;
}

a.dropdown-item {
    color: #000;
    text-decoration: none;
}

a.dropdown-item:active {
    color: #000;
    background-color: white;
    text-decoration: none;
}

a.dropdown-item a{
    color: #000;
    text-decoration: none;
}


span.badge {
    --bs-badge-font-size: 0.5em;
    --bs-badge-font-weight: 700;
}


button.navbar-toggler {
    color: $gray-800;
    border-color: $gray-800;
}

button.navbar-toggler:focus {
    color: $black;
    border-color: $black;
}


a#navbarDropdown {
    color: $gray-800;
}

a#navbarDropdown:hover {
    color: $black;
}

a#navbarDropdown:active {
    color: $black;
}

.bi-bag {
    color: $gray-800;
}

.bi-bag:hover {
    color: $black;
}

.bi-person-circle {
    color: $gray-800;
}

.bi-person-circle:hover {
    color: $black;
}

.bi-bookmark-heart {
    color: $gray-800;
}

.bi-bookmark-heart:hover {
    color: $black;
}


#app {
    font-family: 'Geologica', sans-serif;
    font-weight: 500;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
}
</style>
