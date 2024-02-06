<template>
  <div class="container-fluid min-vh-100 d-flex flex-column p-3" style="background-color: rgb(241, 241, 241);">
    <div class="row flex-grow-1">
      <div class="col-sm-2">
        <div class="card text-bg-light p-2" style="min-height: 100%;">
          <ul class="nav nav-pills flex-sm-column flex-row mb-auto justify-content-between text-truncate">
            <!-- Статистика -->
            <li class="mb-2">
              <div class="d-inline-flex gap-1" style="width: 100%;">
                <button @click=" isClickedStatistics = !isClickedStatistics" class="btn btn-outline-primary d-flex justify-content-between" style="width: 100%;" data-bs-toggle="collapse" href="#multiCollapseStatistics" role="button" aria-expanded="false" aria-controls="multiCollapseStatistics">
                  <div>
                    <span><i class="bi bi-bar-chart-fill"></i></span>
                    <span style="padding-left: 1rem;">Статистика</span>
                  </div>
                  <span><i :class="isClickedStatistics ? 'bi-caret-up-fill' : 'bi-caret-right-fill'"></i></span>
                </button>
              </div>
              <div class="row">
                <div class="col">
                  <div class="container">
                  <div class="collapse multi-collapse" id="multiCollapseStatistics">
                    <button @click="$router.push('/')" class="btn btn-outline-primary d-flex justify-content-between my-1" style="width: 100%;">
                      <div>
                        <span><i class="bi bi-table"></i></span>
                        <span style="padding-left: 1rem;">Общая</span>
                      </div>
                    </button>
                    <button @click="$router.push('/product-statistics')" class="btn btn-outline-primary d-flex justify-content-between" style="width: 100%;">
                      <div>
                        <span><i class="bi bi-table"></i></span>
                        <span style="padding-left: 1rem;">Товары</span>
                      </div>
                    </button>
                  </div>
                </div>
                </div>
              </div>
            </li>
            
            <!-- Модели -->
            <li class="mb-2">
              <div class="d-inline-flex gap-1" style="width: 100%;">
                <button @click="isClickedModel = !isClickedModel" class="btn btn-outline-primary d-flex justify-content-between" style="width: 100%;" data-bs-toggle="collapse" href="#multiCollapsModel" role="button" aria-expanded="false" aria-controls="multiCollapsModel">
                  <div>
                    <span><i class="bi bi-box-fill"></i></span>
                    <span style="padding-left: 1rem;">Модели</span>
                  </div>
                  <span><i :class="isClickedModel ? 'bi-caret-up-fill' : 'bi-caret-right-fill'"></i></span>
                </button>
              </div>
              <div class="row">
                <div class="col">
                  <div class="container">
                  <div class="collapse multi-collapse" id="multiCollapsModel">
                    <button @click="$router.push('/big-categories')" class="btn btn-outline-primary d-flex justify-content-between my-1" style="width: 100%;">
                      <div>
                        <span><i class="bi bi-table"></i></span>
                        <span style="padding-left: 1rem;">Разделы</span>
                      </div>
                    </button>
                    <button @click="$router.push('/categories?big_category_id=0')" class="btn btn-outline-primary d-flex justify-content-between mb-1" style="width: 100%;">
                      <div>
                        <span><i class="bi bi-table"></i></span>
                        <span style="padding-left: 1rem;">Категории</span>
                      </div>
                    </button>
                    <button @click="$router.push('/models?big_category_id=0&category_id=0&collection_id=0')" class="btn btn-outline-primary d-flex justify-content-between mb-1" style="width: 100%;">
                      <div>
                        <span><i class="bi bi-table"></i></span>
                        <span style="padding-left: 1rem;">Модели</span>
                      </div>
                    </button>
                    <button @click="$router.push('/products')" class="btn btn-outline-primary d-flex justify-content-between" style="width: 100%;">
                      <div>
                        <span><i class="bi bi-table"></i></span>
                        <span style="padding-left: 1rem;">Продукты</span>
                      </div>
                    </button>
                  </div>
                </div>
                </div>
              </div>
            </li>
            
             <!-- Справочники -->
            <li>
              <div class="d-inline-flex gap-1" style="width: 100%;">
                <button @click="isClickedReference = !isClickedReference" class="btn btn-outline-primary d-flex justify-content-between" style="width: 100%;" data-bs-toggle="collapse" href="#multiCollapseReference" role="button" aria-expanded="false" aria-controls="multiCollapseReference">
                  <div>
                    <span><i class="bi bi-box-fill"></i></span>
                    <span style="padding-left: 1rem;">Справочники</span>
                  </div>
                  <span><i :class="isClickedReference ? 'bi-caret-up-fill' : 'bi-caret-right-fill'"></i></span>
                </button>
              </div>
              <div class="row">
                <div class="col">
                  <div class="container">
                  <div class="collapse multi-collapse" id="multiCollapseReference">
                    <button @click="$router.push('/collections')" class="btn btn-outline-primary d-flex justify-content-between my-1" style="width: 100%;">
                      <div>
                        <span><i class="bi bi-table"></i></span>
                        <span style="padding-left: 1rem;">Коллекции</span>
                      </div>
                    </button>
                    <button @click="$router.push('/sizes')" class="btn btn-outline-primary d-flex justify-content-between mb-1" style="width: 100%;">
                      <div>
                        <span><i class="bi bi-table"></i></span>
                        <span style="padding-left: 1rem;">Размеры</span>
                      </div>
                    </button>
                    <button @click="$router.push('/colors')" class="btn btn-outline-primary d-flex justify-content-between mb-1" style="width: 100%;">
                      <div>
                        <span><i class="bi bi-table"></i></span>
                        <span style="padding-left: 1rem;">Цвета</span>
                      </div>
                    </button>
                    
                  </div>
                </div>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>
      <div class="col-sm-10">
        <router-view/>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'

export default {
    data() {
        return {
          isClickedStatistics: false,
          isClickedModel: false,
          isClickedReference: false,
        }
    },
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}


nav {
  padding: 30px;

  a {
  font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}


.nav-item{
    position:  relative;
}
.nav-links[data-toggle].collapsed:after {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-arrow-down-circle' viewBox='0 0 16 16'%3E%3Cpath fill-rule='evenodd' d='M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.5 4.5a.5.5 0 0 0-1 0v5.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293z'/%3E%3C/svg%3E");
    transition: all 0.5s;
  }
.nav-links[data-toggle]:not(.collapsed):after {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-arrow-up-circle' viewBox='0 0 16 16'%3E%3Cpath fill-rule='evenodd' d='M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-7.5 3.5a.5.5 0 0 1-1 0V5.707L5.354 7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 5.707z'/%3E%3C/svg%3E");
}

// .d-inline-flex.btn-outline-primary {
//   --bs-btn-font-weight: 600;
//   --bs-btn-color: #fff;
//   --bs-btn-bg: #fff;
//   --bs-btn-border-color: #333;
//   --bs-btn-hover-color: #0d6efd;
//   --bs-btn-hover-bg: #0d6efd;
//   --bs-btn-hover-border-color: #0d6efd;
//   --bs-btn-focus-shadow-rgb: #0d6efd;
//   --bs-btn-active-color: #333;
//   --bs-btn-active-bg: #0d6efd;
//   --bs-btn-active-border-color: #0d6efd;
// }



</style>
