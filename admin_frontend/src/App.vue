<template>
  <div class="container-fluid min-vh-100 d-flex flex-column" style="background-color: #f5f5f9 ">
    <div class="row">
        <div class="col d-flex align-items-center justify-content-start" style="height: 1vh;"></div>
    </div>
    <!-- <div class="row" style="background-color: #684DFE; border-radius: 1rem 1rem 1rem 1rem; margin-left: 0.15rem; margin-right: 0.15rem;"> -->
    <div class="row" style="background: rgb(3,195,236);background: linear-gradient(90deg, rgba(105,108,255,1) 0%, rgba(3,195,236,1) 100%); 
    border-radius: 1rem 1rem 1rem 1rem; margin-left: 0.15rem; margin-right: 0.15rem; box-shadow: 0px 0px 74px 27px rgba(0, 0, 0, 0.15);">
      <div class="col d-flex align-items-center justify-content-start" style="height: 5vh;">
        <!-- Левая часть (ссылка на главную страницу) -->
        <a href="/" class="text-light mx-1" style="text-decoration: none;">
          <span style="font-family: 'Geologica', sans-serif; font-weight: 400; font-size: 20px;">Сергей Тюрин</span>
            <!-- <img src="@/assets/LogoST.png" width="89" height="28" alt="Home" style=" margin-right: 8px;"> -->
        </a>
      </div>
      <div class="col-auto d-flex align-items-center justify-content-end mx-2">
          <!-- Правая часть (иконка уведомлений, dropdown с изображением пользователя и кнопка выхода) -->
          <span class="text-light me-3">
              <!-- Иконка уведомлений системы -->
              <i class="bi bi-bell"></i>
          </span>

          <span class="text-light me-3">
              <!-- Иконка уведомлений заказов -->
              <i class="bi bi-cart"></i>
          </span>

          <div class="dropdown">
              <!-- Кружок с изображением пользователя и кнопка выхода внутри dropdown -->
              <a class="text-light custom-dropdown-toggle" href="#" role="button" id="userDropdown" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  <img src="@/assets/57.webp" alt="User" style="width: 24px; height: 24px; border-radius: 50%;">
              </a>
              <div class="dropdown-menu" aria-labelledby="userDropdown">
                  <button class="dropdown-item" @click="handleLogout">Выйти</button>
              </div>
          </div>
      </div>
    </div>
    <div class="row">
        <div class="col d-flex align-items-center justify-content-start" style="height: 1vh;"></div>
    </div>
    <div class="row flex-grow-1">
      <div class="col-sm-2" >
        <!-- <div class="card p-2" style="min-height: 100%; 
        background: rgb(105,108,255); background: linear-gradient(0deg, rgba(3,195,236,1) 0%, rgba(105,108,255,1) 100%); 
        border-radius: 1.5rem; box-shadow: 0px 0px 74px 27px rgba(0, 0, 0, 0.15);"> -->
        <div class="card p-2" style="min-height: 100%;  
        border-radius: 1.5rem; box-shadow: 0px 0px 74px 27px rgba(0, 0, 0, 0.12);">
          <ul class="nav nav-pills flex-sm-column flex-row mb-auto justify-content-between text-truncate">
            <!-- Статистика -->
            <li class="mb-2">
              <div class="d-inline-flex gap-1" style="width: 100%;">
                <button @click=" isClickedStatistic = !isClickedStatistic" class="btn btn-navigation d-flex justify-content-between" style="width: 100%; border-radius: 1rem;" data-bs-toggle="collapse" href="#multiCollapseStatistic" role="button" aria-expanded="false" aria-controls="multiCollapseStatistic">
                  <div>
                    <span><i class="bi bi-bar-chart-fill"></i></span>
                    <span style="padding-left: 1rem;">Статистика</span>
                  </div>
                  <span><i :class="isClickedStatistic ? 'bi-caret-up-fill' : 'bi-caret-right-fill'"></i></span>
                </button>
              </div>
              <div class="row">
                <div class="col">
                  <div class="container">
                  <div class="collapse multi-collapse" id="multiCollapseStatistic">
                    <button @click="$router.push('/')" :class="{'active': currentPath === '/'}" class="btn btn-navigation-second d-flex justify-content-between mt-1" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-bar-chart-fill"></i></span>
                        <span style="padding-left: 1rem;">Общая</span>
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
                <button @click="isClickedModel = !isClickedModel" :class="{'active': isClickedModel}" class="btn btn-navigation d-flex justify-content-between" style="width: 100%; border-radius: 1.5rem;" data-bs-toggle="collapse" href="#multiCollapseModel" role="button" aria-expanded="false" aria-controls="multiCollapseModel">
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
                  <div class="collapse multi-collapse" id="multiCollapseModel">
                    <button @click="$router.push('/categories')" :class="{'active': currentPath === '/categories'}" class="btn btn-navigation-second d-flex justify-content-between my-1" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-box-seam-fill"></i></span>
                        <span style="padding-left: 1rem;">Категории</span>
                      </div>
                    </button>
                    <button @click="$router.push('/models')" :class="{'active': currentPath === '/models'}" class="btn btn-navigation-second d-flex justify-content-between mb-1" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-layers-fill"></i></span>
                        <span style="padding-left: 1rem;">Модели</span>
                      </div>
                    </button>

                    <button @click="$router.push('/products')" :class="{'active': currentPath === '/products'}" class="btn btn-navigation-second d-flex justify-content-between" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-box-fill"></i></span>
                        <span style="padding-left: 1rem;">Продукты</span>
                      </div>
                    </button>
                  </div>
                </div>
                </div>
              </div>
            </li>
            

            <!-- Ценообразование -->
            <li class="mb-2">
              <div class="d-inline-flex gap-1" style="width: 100%;">
                <button @click="isClickedPriceList = !isClickedPriceList" :class="{'active': isClickedPriceList}" class="btn btn-navigation d-flex justify-content-between" style="width: 100%; border-radius: 1.5rem;" data-bs-toggle="collapse" href="#multiCollapsePriceList" role="button" aria-expanded="false" aria-controls="multiCollapsePriceList">
                  <div>
                    <span><i class="bi bi-currency-dollar"></i></span>
                    <span style="padding-left: 1rem;">Ценообразование</span>
                  </div>
                  <span><i :class="isClickedPriceList ? 'bi-caret-up-fill' : 'bi-caret-right-fill'"></i></span>
                </button>
              </div>
              <div class="row">
                <div class="col">
                  <div class="container">
                  <div class="collapse multi-collapse" id="multiCollapsePriceList">
                    <button @click="$router.push('/price-lists')" :class="{'active': currentPath === '/price-lists'}" class="btn btn-navigation-second d-flex justify-content-between mt-1" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-currency-dollar"></i></span>
                        <span style="padding-left: 1rem;">Прайс-лист</span>
                      </div>
                    </button>
                  </div>
                </div>
                </div>
              </div>
            </li>

             <!-- Справочники -->
            <li class="mb-2">
              <div class="d-inline-flex gap-1" style="width: 100%;">
                <button @click="toggleReferenceCollapse" :class="{'active': isClickedReference}" class="btn btn-navigation d-flex justify-content-between" style="width: 100%; border-radius: 1.5rem;" data-bs-toggle="collapse" data-bs-target="#multiCollapseReference" href="#multiCollapseReference" role="button" aria-expanded="false" aria-controls="multiCollapseReference">
                  <div>
                    <span><i class="bi bi-file-text-fill"></i></span>
                    <span style="padding-left: 1rem;">Справочники</span>
                  </div>
                  <span><i :class="isClickedReference ? 'bi-caret-up-fill' : 'bi-caret-right-fill'"></i></span>
                </button>
              </div>
              <div class="row">
                <div class="col">
                  <div class="container">
                  <div class="collapse multi-collapse" id="multiCollapseReference">
                    <button @click="$router.push('/collections')" :class="{'active': currentPath === '/collections'}" class="btn btn-navigation-second d-flex justify-content-between my-1" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-file-zip-fill"></i></span>
                        <span style="padding-left: 1rem;">Коллекции</span>
                      </div>
                    </button>
                    <button @click="$router.push('/sizes')" :class="{'active': currentPath === '/sizes'}" class="btn btn-navigation-second d-flex justify-content-between mb-1" style="width: 100%;  border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-file-code-fill"></i></span>
                        <span style="padding-left: 1rem;">Размеры</span>
                      </div>
                    </button>
                    <button @click="$router.push('/size-guides')" :class="{'active': currentPath === '/size-guides'}" class="btn btn-navigation-second d-flex justify-content-between mb-1" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-file-spreadsheet-fill"></i></span>
                        <span style="padding-left: 1rem;">Размерные сетки</span>
                      </div>
                    </button>
                    <button @click="$router.push('/colors')" :class="{'active': currentPath === '/colors'}" class="btn btn-navigation-second d-flex justify-content-between mb-1" style="width: 100%;  border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-file-image-fill"></i></span>
                        <span style="padding-left: 1rem;">Цвета</span>
                      </div>
                    </button>
                    <button @click="$router.push('/order-status')" :class="{'active': currentPath === '/order-status'}" class="btn btn-navigation-second d-flex justify-content-between mb-1" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-file-check-fill"></i></span>
                        <span style="padding-left: 1rem;">Статусы заказов</span>
                      </div>
                    </button>
                    <button @click="$router.push('/details')" :class="{'active': currentPath === '/details'}" class="btn btn-navigation-second d-flex justify-content-between" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-file-font-fill"></i></span>
                        <span style="padding-left: 1rem;">Описание</span>
                      </div>
                    </button>
                  </div>
                </div>
                </div>
              </div>
            </li>

            <!-- Заказы -->
            <li class="mb-2">
              <div class="d-inline-flex gap-1" style="width: 100%;">
                <button @click="isClickedOrder = !isClickedOrder" :class="{'active': isClickedOrder}" class="btn btn-navigation d-flex justify-content-between" style="width: 100%; border-radius: 1.5rem;" data-bs-toggle="collapse" href="#multiCollapseOrder" role="button" aria-expanded="false" aria-controls="multiCollapseOrder">
                  <div>
                    <span><i class="bi bi-bag-fill"></i></span>
                    <span style="padding-left: 1rem;">Заказы</span>
                  </div>
                  <span><i :class="isClickedOrder ? 'bi-caret-up-fill' : 'bi-caret-right-fill'"></i></span>
                </button>
              </div>
              <div class="row">
                <div class="col">
                  <div class="container">
                  <div class="collapse multi-collapse" id="multiCollapseOrder">
                    <button @click="$router.push('/orders')" :class="{'active': currentPath === '/orders'}" class="btn btn-navigation-second d-flex justify-content-between mt-1" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-bag-fill"></i></span>
                        <span style="padding-left: 1rem;">Все заказы</span>
                      </div>
                    </button>
                  </div>
                </div>
                </div>
              </div>
            </li>

            <!-- Пользователи -->
            <li class="mb-2">
              <div class="d-inline-flex gap-1" style="width: 100%;">
                <button @click="isClickedUser = !isClickedUser" :class="{'active': isClickedUser}" class="btn btn-navigation d-flex justify-content-between" style="width: 100%; border-radius: 1.5rem;" data-bs-toggle="collapse" href="#multiCollapseUser" role="button" aria-expanded="false" aria-controls="multiCollapseUser">
                  <div>
                    <span><i class="bi bi-people-fill"></i></span>
                    <span style="padding-left: 1rem;">Пользователи</span>
                  </div>
                  <span><i :class="isClickedUser ? 'bi-caret-up-fill' : 'bi-caret-right-fill'"></i></span>
                </button>
              </div>
              <div class="row">
                <div class="col">
                  <div class="container">
                  <div class="collapse multi-collapse" id="multiCollapseUser">
                    <button @click="$router.push('/users')" :class="{'active': currentPath === '/users'}" class="btn btn-navigation-second d-flex justify-content-between my-1" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-person-fill"></i></span>
                        <span style="padding-left: 1rem;">Пользователи</span>
                      </div>
                    </button>
                    <button @click="$router.push('/employees')" :class="{'active': currentPath === '/employees'}" class="btn btn-navigation-second d-flex justify-content-between my-1" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-person-vcard-fill"></i></span>
                        <span style="padding-left: 1rem;">Сотрудники</span>
                      </div>
                    </button>
                    <button @click="$router.push('/departments')" :class="{'active': currentPath === '/departments'}" class="btn btn-navigation-second d-flex justify-content-between my-1" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-diagram-3-fill"></i></span>
                        <span style="padding-left: 1rem;">Отделы</span>
                      </div>
                    </button>
                    <button @click="$router.push('/employee-statuses')" :class="{'active': currentPath === '/employee-statuses'}" class="btn btn-navigation-second d-flex justify-content-between" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-lightning-charge-fill"></i></span>
                        <span style="padding-left: 1rem;">Статусы сотрудников</span>
                      </div>
                    </button>
                  </div>
                </div>
                </div>
              </div>
            </li>

            <!-- Склад -->
            <li class="mb-2">
              <div class="d-inline-flex gap-1" style="width: 100%;">
                <button @click="isClickedWarehouse = !isClickedWarehouse" :class="{'active': isClickedWarehouse}" class="btn btn-navigation d-flex justify-content-between" style="width: 100%; border-radius: 1.5rem;" data-bs-toggle="collapse" href="#multiCollapseWarehouse" role="button" aria-expanded="false" aria-controls="multiCollapseWarehouse">
                  <div>
                    <span><i class="bi bi-house-fill"></i></span>
                    <span style="padding-left: 1rem;">Склад</span>
                  </div>
                  <span><i :class="isClickedWarehouse ? 'bi-caret-up-fill' : 'bi-caret-right-fill'"></i></span>
                </button>
              </div>
              <div class="row">
                <div class="col">
                  <div class="container">
                  <div class="collapse multi-collapse" id="multiCollapseWarehouse">
                    <button @click="$router.push('/warehouses')" :class="{'active': currentPath === '/warehouses'}" class="btn btn-navigation-second d-flex justify-content-between mt-1" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-house-fill"></i></span>
                        <span style="padding-left: 1rem;">Все cклады</span>
                      </div>
                    </button>
                  </div>
                </div>
                </div>
              </div>
            </li>

            <!-- Отчеты -->
            <li class="mb-2">
              <div class="d-inline-flex gap-1" style="width: 100%; border-radius: 1.5rem;">
                <button @click="isClickedReport = !isClickedReport" :class="{'active': isClickedReport}" class="btn btn-navigation d-flex justify-content-between" style="width: 100%; border-radius: 1.5rem;" data-bs-toggle="collapse" href="#multiCollapseReport" role="button" aria-expanded="false" aria-controls="multiCollapseReport">
                  <div>
                    <span><i class="bi bi-file-text-fill"></i></span>
                    <span style="padding-left: 1rem;">Отчеты</span>
                  </div>
                  <span><i :class="isClickedReport ? 'bi-caret-up-fill' : 'bi-caret-right-fill'"></i></span>
                </button>
              </div>
              <div class="row">
                <div class="col">
                  <div class="container">
                  <div class="collapse multi-collapse" id="multiCollapseReport">
                    <button @click="$router.push('/reports')" :class="{'active': currentPath === '/reports'}" class="btn btn-navigation-second d-flex justify-content-between mt-1" style="width: 100%; border-radius: 1.5rem;">
                      <div>
                        <span><i class="bi bi-file-text-fill"></i></span>
                        <span style="padding-left: 1rem;">Все отчеты</span>
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
      <div class="col-sm-10 d-flex flex-column" style="max-height: 92vh;">
        <router-view/>
      </div>
    </div>
    <div class="row">
        <div class="col d-flex align-items-center justify-content-start" style="height: 1vh;"></div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import bootstrap from 'bootstrap/dist/js/bootstrap.js'
export default {
    data() {
        return {
          currentPath: '',
          isClickedStatistic: false,
          multiCollapseStatistic: null,

          isClickedModel: false,
          multiCollapseModel: null,

          isClickedPriceList: false,
          multiCollapsePriceList: null,

          isClickedReference: false,
          multiCollapseReference: null,
          
          isClickedOrder: false,
          multiCollapseOrder: null,

          isClickedUser: false,
          multiCollapseUser: null,

          isClickedWarehouse: false,
          multiCollapseWarehouse: null,

          isClickedReport: false,
        }
    },
    methods: {
      toggleStatisticCollapse() {
        if (!this.multiCollapseStatistic) {
          this.multiCollapseStatistic = new bootstrap.Collapse(document.getElementById('multiCollapseStatistic'));
        }
        this.multiCollapseStatistic.toggle();
        this.isClickedStatistic = !this.isClickedStatistic;
      },
      toggleModelCollapse() {
        if (!this.multiCollapseModel) {
          this.multiCollapseModel = new bootstrap.Collapse(document.getElementById('multiCollapseModel'));
        }
        this.multiCollapseModel.toggle();
        this.isClickedModel = !this.isClickedModel;
      },
      togglePriceListCollapse() {
        if (!this.multiCollapsePriceList) {
          this.multiCollapsePriceList = new bootstrap.Collapse(document.getElementById('multiCollapsePriceList'));
        }
        this.multiCollapsePriceList.toggle();
        this.isClickedModel = !this.isClickedModel;
      },
      toggleReferenceCollapse() {
        if (!this.multiCollapseReference) {
          this.multiCollapseReference = new bootstrap.Collapse(document.getElementById('multiCollapseReference'));
        }
        this.multiCollapseReference.toggle();
        this.isClickedReference = !this.isClickedReference;
      },
      toggleOrderCollapse() {
        if (!this.multiCollapseOrder) {
          this.multiCollapseOrder = new bootstrap.Collapse(document.getElementById('multiCollapseOrder'));
        }
        this.multiCollapseOrder.toggle();
        this.isClickedOrder = !this.isClickedOrder;
      },
      toggleUserCollapse() {
        if (!this.multiCollapseUser) {
          this.multiCollapseUser = new bootstrap.Collapse(document.getElementById('multiCollapseUser'));
        }
        this.multiCollapseUser.toggle();
        this.isClickedUser = !this.isClickedUser;
      },
      toggleWarehouseCollapse() {
        if (!this.multiCollapseWarehouse) {
          this.multiCollapseWarehouse = new bootstrap.Collapse(document.getElementById('multiCollapseWarehouse'));
        }
        this.multiCollapseWarehouse.toggle();
        this.isClickedWarehouse = !this.isClickedWarehouse;
      },


      checkCurrentRoute(to, from) {
        const StatisticRoutes = ['/', '/product-statistics'];
        const ModelRoutes = ['/big-categories', '/categories', '/models', '/product'];
        const PriceListRoutes = ['/price-lists'];
        const ReferenceRoutes = ['/collections', '/sizes', '/colors', '/order-status'];
        const OrdersRoutes = ['/orders'];
        const UsersRoutes = ['/users', '/employees', '/departments', '/employee-statuses'];
        const WarehouseRoutes = ['/warehouse'];

        const BaseRoutes = ['/'];
        if (!to || !from) {
          return;
        }

        const currentRoute = to.path; // Текущий URL
        this.currentPath = currentRoute
        const previousRoute = from.path;

        if (currentRoute == '/products') {

        }

        console.log("previousRoute")
        console.log(previousRoute)
        console.log("previousRoute")

        console.log("currentRoute1")
        console.log(currentRoute)
        console.log("currentRoute1")

        if ((StatisticRoutes.includes(currentRoute) && BaseRoutes.includes(previousRoute))) {
          this.toggleStatisticCollapse()
        }
        
        if ((ModelRoutes.some(route => currentRoute.startsWith(route)) && BaseRoutes.includes(previousRoute))) {
          this.toggleModelCollapse()
        }

        if ((PriceListRoutes.some(route => currentRoute.startsWith(route)) && BaseRoutes.includes(previousRoute))) {
          this.togglePriceListCollapse()
        }

        if ((ReferenceRoutes.some(route => currentRoute.startsWith(route)) && BaseRoutes.includes(previousRoute))) {
          this.toggleReferenceCollapse()
        }

        if ((OrdersRoutes.some(route => currentRoute.startsWith(route)) && BaseRoutes.includes(previousRoute))) {
          this.toggleOrderCollapse()
        }

        if ((UsersRoutes.some(route => currentRoute.startsWith(route)) && BaseRoutes.includes(previousRoute))) {
          this.toggleUserCollapse()
        }
        
        if ((WarehouseRoutes.some(route => currentRoute.startsWith(route)) && BaseRoutes.includes(previousRoute))) {
          this.toggleWarehouseCollapse()
        }
      },
    },
    mounted() {
      // Получаем сохраненное состояние из localStorage при загрузке компонента
      this.checkCurrentRoute();
    },
    watch: {
      // Следим за изменением URL
      $route(to, from) {
        this.checkCurrentRoute(to, from);
      },
    },
    beforeDestroy() {
      // При уничтожении компонента отменяем состояние collapse
      const multiCollapseReference = new bootstrap.Collapse(document.getElementById('multiCollapseReference'));
      multiCollapseReference.dispose();
    },
    destroyed() {
      // При уничтожении компонента удаляем обработчики событий, если они были созданы
      const multiCollapseReference = new bootstrap.Collapse(document.getElementById('multiCollapseReference'));
      multiCollapseReference.dispose();
    },

}
</script>

<style lang="scss">
@import "./custom.scss";
#app {
    font-family: "Public Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
    font-weight: 400;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    
}

.custom-dropdown-toggle {
    cursor: pointer;
    text-decoration: none; /* Если нужно убрать подчеркивание */
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

</style>
