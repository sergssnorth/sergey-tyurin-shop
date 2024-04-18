<template>
    <div class="container-fluid">
        <div class="row my-3">
            <div class="col-4">
                <div class="card p-2"  style="border-radius: 1.5rem;">
                    <div id="chart-spark1">
                        <VueApexCharts type="area" height="160" :options="chartOptionsSpark1" :series="seriesSpark1">
                        </VueApexCharts>
                    </div>
                </div>
            </div>

            <div class="col-4">
                <div class="card p-2"  style="border-radius: 1.5rem;">
                    <div id="chart-spark2">
                        <VueApexCharts type="area" height="160" :options="chartOptionsSpark2" :series="seriesSpark2">
                        </VueApexCharts>
                    </div>
                </div>
            </div>

            <div class="col-4">
                <div class="card p-2"  style="border-radius: 1.5rem;">
                    <div id="chart-spark3">
                        <VueApexCharts type="area" height="160" :options="chartOptionsSpark3" :series="seriesSpark3">
                        </VueApexCharts>
                    </div>
                </div>
            </div>
        </div>
        <div class="row mt-3">
            <div class="col-8">
                <div class="card p-2"  style="border-radius: 1.5rem;">
                    <div id="chart-bar1">
                        <VueApexCharts width="100%" type="bar" :options="chartOptionsBar1" :series="seriesBar1">
                        </VueApexCharts>
                    </div>
                </div>
            </div>
            <div class="col-4">
                <div class="card p-2"  style="border-radius: 1.5rem;">
                    <div id="chart-donut1">
                        <VueApexCharts width="100%" type="donut" :options="chartOptionsDonut1" :series="seriesDonut1">
                        </VueApexCharts>
                    </div>
                </div>
            </div>
        </div>

    </div>
    <div>
    </div>
</template>

<script>
import VueApexCharts from "vue3-apexcharts";

export default {
    name: 'Home',
    components: { VueApexCharts },
    data: () => ({
        seriesSpark1: [{
            name: 'Выручка',
            data: [37,54,77,58,75,96,92,73,99,99,14,41,23,30,78,75,33,45,44,22,69,30,13,97,81,67,52,74,24,63]
        }],

        chartOptionsSpark1: {
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
            colors: ['#03c3ec'],
            title: {
                text: '₽ 235 312',
                offsetX: 0,
                style: {
                    fontSize:  '20px',
                    fontWeight:  '400',
                }
            },
            subtitle: {
                text: 'Выручка',
                offsetX: 0,
                style: {
                    fontSize: '15px',
                    fontWeight:  '400',
                }
            }
        },

        seriesSpark2: [{
            name: 'Продаж',
            data: [61,34,56,45,71,85,79,17,56,29,45,53,55,49,46,14,69,87,65,45,57,25,90,18,22,77,41,30,58,53]
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
            colors: ['#03c3ec'],
            title: {
                text: '54',
                offsetX: 0,
                style: {
                    fontSize:  '20px',
                    fontWeight:  '400',
                }
            },
            subtitle: {
                text: 'Кол-во продаж',
                offsetX: 0,
                style: {
                    fontSize: '15px',
                    fontWeight:  '400',
                }
            }
        },

        seriesSpark3: [{
            name: 'Пользователей',
            data: [86,68,12,47,81,76,26,22,12,34,90,18,41,36,41,78,17,17,55,30,57,61,47,95,18,52,14,20,31,65]
        }],

        chartOptionsSpark3: {
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
            colors: ['#03c3ec'],
            title: {
                text: '1 253',
                offsetX: 0,
                style: {
                    fontSize:  '20px',
                    fontWeight:  '400'
                }
            },
            subtitle: {
                text: 'Кол-во пользователей',
                offsetX: 0,
                style: {
                    fontSize: '15px',
                    fontWeight:  '400',
                }
            }
        },


        seriesBar1: [{
            name: 'Футболки',
            data: [44, 55, 41, 67, 22, 43, 44, 55, 41, 67, 22, 43, 44, 55, 41, 67, 22, 43, 44, 55, 41, 67, 22, 43, 55, 41, 67, 22, 43, 0]
          }, {
            name: 'Толстовки',
            data: [13, 23, 20, 8, 13, 27, 13, 23, 20, 8, 13, 27, 13, 23, 20, 8, 13, 27, 13, 23, 20, 8, 13, 27, 23, 20, 8, 13, 27, 0]
          }, {
            name: 'Аксессуары',
            data: [11, 17, 15, 15, 21, 14, 13, 23, 20, 8, 13, 27, 11, 17, 15, 15, 21, 14, 13, 23, 20, 8, 13, 27, 23, 20, 8, 13, 27, 0]
          }],
        chartOptionsBar1: {
            chart: {
              type: 'bar',
              height: 350,
              stacked: true,
              toolbar: {
                show: true
              },
              zoom: {
                enabled: false
              }
            },
            responsive: [{
              breakpoint: 480,
              options: {
                legend: {
                  position: 'bottom',
                  offsetX: -10,
                  offsetY: 0
                }
              }
            }],
            plotOptions: {
              bar: {
                horizontal: false,
                borderRadius: 10,
                dataLabels: {
                  total: {
                    enabled: true,
                    style: {
                      fontSize: '13px',
                      fontWeight: 900
                    }
                  }
                }
              },
            },
            xaxis: {
              type: 'datetime',
              categories: ['01/01/2011 GMT', '01/02/2011 GMT', '01/03/2011 GMT', '01/04/2011 GMT',
                '01/05/2011 GMT', '01/06/2011 GMT','01/07/2011 GMT', '01/08/2011 GMT', '01/09/2011 GMT', '01/10/2011 GMT',
                '01/11/2011 GMT', '01/12/2011 GMT', '01/13/2011 GMT', '01/14/2011 GMT', '01/15/2011 GMT', '01/16/2011 GMT',
                '01/17/2011 GMT', '01/18/2011 GMT','01/19/2011 GMT', '01/20/2011 GMT', '01/21/2011 GMT', '01/22/2011 GMT',
                '01/23/2011 GMT', '01/24/2011 GMT', '01/25/2011 GMT', '01/26/2011 GMT', '01/27/2011 GMT',
                '01/28/2011 GMT', '01/29/2011 GMT','01/30/2011 GMT'
              ],
            },
            legend: {
              position: 'right',
              offsetY: 42
            },
            fill: {
              opacity: 1
            },
            title: {
                text: 'Продажи по категориям',
                offsetX: 0,
                margin: 20,
                align: 'center',
                style: {
                    fontSize:  '20px',
                    fontWeight:  '400'
                }
            },
        },


        seriesDonut1: [44, 55, 13, 33],
        chartOptionsDonut1: {
            chart: {
              width: 380,
              type: 'donut',
            },
            labels: ["T-shirt PL", "T-shirt New Era", "T-shirt Colors", "Zip-Hoodie Russia"],
            dataLabels: {
              enabled: false
            },
            responsive: [{
              breakpoint: 480,
              options: {
                chart: {
                  width: 200
                },
                legend: {
                  show: false
                }
              }
            }],
            legend: {
              position: 'right',
              offsetY: 100,
              height: 230,
            },
            title: {
                text: 'Продажи моделей',
                offsetX: 0,
                margin: 20,
                align: 'center',
                style: {
                    fontSize:  '20px',
                    fontWeight:  '400'
                }
            },
          },
        
    }),
    mounted() {
        document.title = 'Главная страница'
    },
    methods: {

    }
}

</script>
