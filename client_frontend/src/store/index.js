import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
        items: [],
    },
    favorite: {
      items: [],
    },
    isAuthenticated: false,
    token: '',
    isLoading: false,
    activeHeart: false,
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }

      if (localStorage.getItem('favorite')) {
        state.favorite = JSON.parse(localStorage.getItem('favorite'))
      } else {
        localStorage.setItem('favorite', JSON.stringify(state.favorite))
      }

      if (localStorage.getItem('token')) {
          state.token = localStorage.getItem('token')
          state.isAuthenticated = true
      } else {
          state.token = ''
          state.isAuthenticated = false
      } 
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.product.id === item.product.id && i.size === item.size)
      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      } else {
        state.cart.items.push(item)
      }
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    addToFavorite(state, item) {
      const exists = state.favorite.items.filter(i => i.product.id === item.product.id)
      if (exists.length) {
        console.log("Уже есть")
      } else {
        state.favorite.items.push(item)
      }
      localStorage.setItem('favorite', JSON.stringify(state.favorite))
    },

      actionToFavorite(state, item) {
      const exists = state.favorite.items.filter(i => i.product.id === item.product.id)
      if (exists.length) {
        const newItems = state.favorite.items.filter(i => i.product.id !== item.product.id)
        state.favorite.items = newItems
        localStorage.setItem('favorite', JSON.stringify(state.favorite))

      } else {
        state.favorite.items.push(item)
        localStorage.setItem('favorite', JSON.stringify(state.favorite))
      }
    },

    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
        state.token = token
        state.isAuthenticated = true
    },  
    removeToken(state) {
        state.token = ''
        state.isAuthenticated = false
    },
    clearCart(state) {
      state.cart = { items: [] }
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    clearFavorite(state, item) {
      state.favorite = { items: [] }
      localStorage.setItem('favorite', JSON.stringify(state.favorite))
    },
  },
  actions: {
  },
  modules: {
  }
})
