<template>
    <div style="
    display: inline-block;
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: 1000px;
    height: 400px;
    margin: auto;
    border: 3px solid #1976D2;
    border-radius: 10px">

    <v-container style="margin-left: 80px">
        <v-card-title style="margin-left:70px; margin-bottom:50px;font-size: 25px">Please select one or more algorithms to process your image</v-card-title>
        <v-switch style="font-size: 250px" v-model="alg1" class="colorFont" label="ResNet152V2" >sfasdas</v-switch>
        <v-switch v-model="alg2" class="xl-2" label="InceptionV3"></v-switch>
      <v-switch v-model="alg3" class="xl-2" label="InceptionResNetV2"></v-switch>
    </v-container>
    
      <v-btn  :loading="loading"  min-width="300" min-height="50" style="margin-left: 340px; margin-top:0px" class="primary" type="submit" v-on:click="testS(), loader ='loading'"> Submit </v-btn> 
    </div>
</template>

<script>
import axios from 'axios'
import { EventBus } from "../event-bus.js";

export default {
    name: 'AlgoSelector',
    data() {
      return {
          files:[],
          alg1: false,
          alg2: false,
          alg3: false,
          choices: null,
          result: "shdiaueguggg",
          loading:false,
          loader:null
      }
    },
    methods: {
        testS() {
            this.buildArray()
            
            setTimeout(this.loadPieCharts, 70000)
            
        },
        loadPieCharts() {
           
            EventBus.$emit('LOAD_PIE_CHARTS')
        },
        sendData() {
            EventBus.$emit('senddata', this.result)
        },
        //this method takes the values of the switch buttons in the form of booleans
        buildArray() {
            
            var data = {
                resnet: this.alg1,
                inceptionres: this.alg2,
                inceptionv3: this.alg3
            }
            EventBus.$emit("pieload",data)
            const url = 'http://localhost:5000/algos'
            //this is where the post request is called to send the data
            return axios.post(url,data);
        },
        getRes(){
            const url = 'http://localhost:5000/results'

            return axios.get(url)
        },

        getResult(){
            this.getRes().then(response => {
                this.result =  response.data['msg'];
                

                console.log('RES in algo',this.result)
    })
    .catch(err => {
        console.log(err)
    })
        }
    },
    watch: {
      loader () {
        const l = this.loader
        this[l] = !this[l]

        setTimeout(() => (this[l] = false), 3000)

        this.loader = null
      }
    }
}
</script>
