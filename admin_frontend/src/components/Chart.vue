<template>
    <ccv-simple-bar-chart :data='data' :options='options'></ccv-simple-bar-chart>
</template>

<script>
import "@carbon/styles/css/styles.css";

import "@carbon/charts/styles.css";
import chartsVue from "@carbon/charts-vue";
export default {
    name: "Chart",
	components: {},
	data() {
		return {
			data: [
                {
                        "group": "Qty",
                        "value": 65000
                },
                {
                        "group": "More",
                        "value": 29123
                },
                {
                        "group": "Sold",
                        "value": 35213
                },
                {
                        "group": "Restocking",
                        "value": 51213
                },
                {
                        "group": "Misc",
                        "value": 16932
                }
            ],
		    options: {
                "title": "Vertical simple bar (discrete)",
                "axes": {
                        "left": {
                                "mapsTo": "value"
                        },
                        "bottom": {
                                "mapsTo": "group",
                                "scaleType": "labels"
                        }
                },
                "height": "400px"
            }
		};
	},
}

</script>

