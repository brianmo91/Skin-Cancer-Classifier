<template>
<div>
    <v-container v-if="oneChart==true">
        
            <VueApexCharts  type=pie width=1000 :options="chartOptions" :series="series"/>
        
    </v-container>
    <v-container v-if="twoCharts==true">
        <VueApexCharts  type=pie width=1000 :options="chartOptions1" :series="series1"/>
        <VueApexCharts  type=pie width=1000 :options="chartOptions3" :series="series3"/>
    </v-container>
</div>
</template>



<script>


import VueApexCharts from 'vue-apexcharts';
import axios from 'axios';
export default {
    name:"ResNet",
    components: {VueApexCharts},
    data() {
        return {
            series: [0.9999974,2.506086e-06,1.4720435e-07],
            chartOptions: {
            labels: ['melanocytic nevi', 'iereiru', 'Actinic keratoses'],
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


                this.resnetarr = data['msg']['0']
                
                
                this.CancerNameRes1 = this.resnetarr['1']['1']
                this.CancerResAcc1 = this.resnetarr['1']['2']

                this.CancerNameRes2 = this.resnetarr['2']['1']
                this.CancerResAcc2 = this.resnetarr['2']['2']

                this.CancerNameRes3 = this.resnetarr['3']['1']
                this.CancerResAcc3 = this.resnetarr['3']['2']

                

                this.chartOptions.labels[0] = this.CancerNameRes1
                this.chartOptions.labels[1] = this.CancerNameRes2
                this.chartOptions.labels[2] = this.CancerNameRes3

                
                var newSeries1 = [this.CancerResAcc1,this.CancerResAcc2,this.CancerResAcc3]
                
                this.series = newSeries1;

       
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
