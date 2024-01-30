<template>
    <div class="container">
        <div class="row">
            <div class="col-6">
                <VueApexCharts 
                    width="500" type="bar" 
                    :options="options" :series="series">
                </VueApexCharts>  
            </div>
            <div class="col-6">
                <VueApexCharts 
                    width="500" type="bar" 
                    :options="options" :series="series">
                </VueApexCharts> 
            </div>
        </div>
        <div class="row">
            <div class="col-6">
                <VueApexCharts 
                    width="500" type="bar" 
                    :options="options" :series="series">
                </VueApexCharts>  
            </div>
            <div class="col-6">
                <VueApexCharts 
                    width="500" type="bar" 
                    :options="options" :series="series">
                </VueApexCharts> 
            </div>
        </div>
    </div>
    <div>
    </div>
</template>

<script>
import VueApexCharts from "vue3-apexcharts";

export default {
    name: 'ProductStatistics',
    components: {VueApexCharts},
    data: () => ({
    options: {
      chart: {
        id: 'vuechart-example'
      },
      xaxis: {
        categories: [
         "Jan",
         "Feb",
         "Mar",
         "Apr",
         "May",
         "Jun",
         "Jul",
         "Aug",
         "Sep",
         "Oct",
         "Nov",
         "Dec"
        ]
      }
    },
    series: [{
      name: 'series-1',
      data: [55, 62, 89, 66, 98, 72, 101, 75, 94, 120, 117, 139]
    }]}),
    mounted() {
        document.title = 'Главная страница'
    },
    methods: {
        
    }
}

</script>

