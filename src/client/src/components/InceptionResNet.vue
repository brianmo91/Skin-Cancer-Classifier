<template>
<div>
    <v-container>
        
            <VueApexCharts  type=pie width=1000 :options="chartOptions" :series="series"/>
        
    </v-container>
    
</div>
</template>



<script>


import VueApexCharts from 'vue-apexcharts';
import axios from 'axios';
export default {
    name:"InceptionResNet",
    components: {VueApexCharts},
    data() {
        return {
            series: [1.0,2.9319884e-13,8.238153e-15],
            chartOptions: {
            labels: ['tesydfyg', 'melanoma', 'benign keratosis-like lesions'],
            responsive: [{
            breakpoint: 580,
            options: {
              chart: {
                width: 400
              },
              legend: {
                position: 'bottom',
                show: true
              }
            }
          }],
          
        },
        
        resnetarr: null,
        inceptionresnetv2: null,
        inceptionv3: null,
        CancerNameRes1: null,
        CancerResAcc1: null,
        CancerNameRes2: null,
        CancerResAcc2: null,
        CancerNameRes3: null,
        CancerResAcc3: null,
        CancerNameInceptionRes1: null,
        CancerInceptionResAcc1: null,
        CancerNameInceptionRes2: null,
        CancerInceptionResAcc2: null,
        CancerNameInceptionRes3: null,
        CancerInceptionResAcc3: null,
        CancerNameInceptionv1: null,
        CancerNameInceptionAcc1: null,
        CancerNameInceptionv2: null,
        CancerNameInceptionAcc2: null,
        CancerNameInceptionv3: null,
        CancerNameInceptionAcc3: null,
        results: null,
        oneChart: true,
        twoCharts: false

        }
    },
    methods: {
        getRes(){
            const url = 'http://localhost:5000/results'

            return axios.get(url)
        },

        getResult(){
            this.getRes().then(response => {
                this.results =  response.data;
                var data = this.results
               
                this.inceptionresnetv2 = data['msg']['2']

                this.CancerNameInceptionRes1 = this.inceptionresnetv2['1']['1']
                this.CancerInceptionResAcc1 = this.inceptionresnetv2['1']['2']

                this.CancerNameInceptionRes2 = this.inceptionresnetv2['2']['1']
                this.CancerInceptionResAcc2 = this.inceptionresnetv2['2']['2']

                this.CancerNameInceptionRes3 = this.inceptionresnetv2['3']['1']
                this.CancerInceptionResAcc3 = this.inceptionresnetv2['3']['2']

                var newSeries = [this.CancerInceptionResAcc1, this.CancerInceptionResAcc2, this.CancerInceptionResAcc3]

                this.series = newSeries

                this.chartOptions.labels[0] = this.CancerNameInceptionRes1
                this.chartOptions.labels[1] = this.CancerNameInceptionRes2
                this.chartOptions.labels[2] = this.CancerNameInceptionRes3
                
            })
            .catch(err => {
                console.log(err)
            })
        }
    },
    
   created() {
        this.getResult()
}
}
</script>
