<template>
    Search: <input v-model="search"><br /><br />
    
    <div v-for="option in filteredOptions" :key="option.value">
      {{ option.text}}
    </div>
  </template>
  
  <script>
  import axios from 'axios'

  
  export default {
      name: 'Order',
    data() {
      return {
          search: '',
          options: [
                  {
                      value: 'apple',
                      text: 'Apple'
                  },
                  
                  {
                      value: 'orange',
                      text: 'Orange'
                  },
  
                  {
                      value: 'grape',
                      text: 'Grape'
                  }
              ],
      }
    },
    computed: {
      filteredOptions() {
        console.log("filteredOptions")
          return this.options.filter((option) => option.value.includes(this.search.toLowerCase()));
      }
    }
  }
    
  </script>
  