<template>
    <div class="container">
        <div class="row">
            <div class="col-4">
                <div id="chart-spark1">
                    <VueApexCharts type="area" height="160px" :options="chartOptions" :series="series12" ></VueApexCharts>
                </div>
            </div>
            <div class="col-4">
                <div id="chart-spark2">
                    <VueApexCharts type="area" height="160" :options="chartOptionsSpark2" :series="seriesSpark2"></VueApexCharts>
                </div>
            </div>
            <div class="col-4">

            </div>
        </div>
        <div class="row">
            <div class="col-6">
                <VueApexCharts 
                    width="100%" type="bar" 
                    :options="options" :series="series">
                </VueApexCharts>  
            </div>
            <div class="col-6">
                <VueApexCharts 
                    width="100%" type="bar" 
                    :options="options2" :series="series2">
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
    name: 'AdminHome',
    components: {VueApexCharts},
    data: () => ({

    seriesSpark2: [{
        name: 'series-2',
        data: [20, 20, 20, 20, 20, 20, 101, 75, 94, 120, 117, 139]
          }],

    chartOptionsSpark2: {
    chart: {
        type: 'area',
        height: 160,
        sparkline: {
        enabled: true
        },
    },
    stroke: {
        curve: 'straight'
    },
    fill: {
        opacity: 0.3,
    },
    yaxis: {
        min: 0
    },
    colors: ['#DCE6EC'],
    title: {
        text: '$235,312',
        offsetX: 0,
        style: {
        fontSize: '24px',
        }
    },
    subtitle: {
        text: 'Expenses',
        offsetX: 0,
        style: {
        fontSize: '14px',
        }
    }
        },

    chartOptions: {
        chart: {
            type: 'area',
            height: 160,
            sparkline: {
            enabled: true
            },
            colors: ['#DCE6EC'],
            title: {
              text: '$424,652',
              offsetX: 0,
              style: {
                fontSize: '24px',
              }
            },
            subtitle: {
              text: 'Sales',
              offsetX: 0,
              style: {
                fontSize: '14px',
              }
            }
        }
    },
    series12: [{
        name: 'series-2',
        data: [20, 20, 20, 20, 20, 20, 101, 75, 94, 120, 117, 139]
          }],
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
        },
        title: {
            text: 'Fiction Books Sales'
        },
    },
    series: [{
      name: 'series-1',
      data: [55, 62, 89, 66, 98, 72, 101, 75, 94, 120, 117, 139]
    }],
    
    options2: {
        chart: {
            id: 'vuechart-example2'
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
        },
        title: {
            text: 'Books Sales'
        },
    },
    series2: [{
      name: 'series-2',
      data: [20, 20, 20, 20, 20, 20, 101, 75, 94, 120, 117, 139]
    }],

    }),
    mounted() {
        document.title = 'Главная страница'
    },
    methods: {
        
    }
}

</script>

