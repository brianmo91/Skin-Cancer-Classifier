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
    name:"InceptionV3",
    components: {VueApexCharts},
    data() {
        return {
            series: [0.99947935,0.00052071654,1.5936376e-10],
            chartOptions: {
            labels: ['melanocytic nevi', 'benign keratosis-like lesions', 'reeee'],
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
        twoCharts: false,
        temp: null

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
                this.inceptionv3 = data['msg']['1']
               
                this.CancerNameInceptionRes1 = this.inceptionv3['1']['1']
                this.CancerInceptionResAcc1 = this.inceptionv3['1']['2']

                this.CancerNameInceptionRes2 = this.inceptionv3['2']['1']
                this.CancerInceptionResAcc2 = this.inceptionv3['2']['2']

                this.CancerNameInceptionRes3 = this.inceptionv3['3']['1']
                this.CancerInceptionResAcc3 = this.inceptionv3['3']['2']

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
