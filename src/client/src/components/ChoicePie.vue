<template>
<div>
    
<v-container v-if="inceptionres==1 && inceptionv3==1 && resnet==1 && results!=null">
    <v-card-title> ResNet</v-card-title>
    <ResNet/>
    <v-card-title> InceptionResNet</v-card-title>
    <InceptionResNet/>
    <v-card-title>Inceptionv3</v-card-title>
    <InceptionV3/>

</v-container>

<v-container v-else-if="inceptionres==1 && inceptionv3==1 && results!=null">
    <InceptionResNet/>
    <InceptionV3/>
</v-container>

<v-container v-else-if="inceptionres==1 && resnet==1 && results!=null">
    <v-card-title> ResNet</v-card-title>
    <ResNet/>
    <InceptionResNet/>
</v-container>

<v-container v-else-if="resnet==1 && inceptionv3==1 && results!=null">
    <v-card-title> ResNet</v-card-title>
    <ResNet/>
    <InceptionV3/>
</v-container>

<v-container v-else-if="inceptionres==1 && results!=null">
    <v-card-title> InceptionResNet</v-card-title>
    <InceptionResNet/>
</v-container>

<v-container v-else-if="inceptionv3==1 && results!=null">
    <v-card-title>Inceptionv3</v-card-title>
    <InceptionV3/>
</v-container>

<v-container v-else-if="resnet==1 && results!=null">
    <v-card-title> ResNet</v-card-title>
    <ResNet/>
</v-container>

</div>
</template>

<script>
import ResNet from "./ResNet"
import InceptionResNet from "./InceptionResNet"
import InceptionV3 from "./InceptionV3"
import axios from 'axios'

export default {
    name:"ChoicePie",
    components: {ResNet, InceptionResNet, InceptionV3},
    data() {
        return {
            inceptionv3: false,
            resnet: false,
            inceptionres: false,
            data: {
                alg1: null,
                alg2: null,
                alg3: null
            },
            temp: null,
            loading: false,
            results: null,
            resu: null
        }
    },

     created() {
        this.getOptions()
        this.getResult()
      
    },
    
    methods: {
        getRes(){
            const url = 'http://localhost:5000/results'

            return axios.get(url)
        },
        getResult(){
            this.getRes().then(response => {
                this.resu =  response.data;
                
                this.results = this.resu['msg']
               
            })
        },
        getOptionsReq() {
            const url = 'http://localhost:5000/array'

            return axios.get(url)

        },

        getOptions() {
            this.getOptionsReq().then(response => {
                this.loading = true
                this.temp = response;
                this.resnet = this.temp['data']['optionarray']['0']
                this.inceptionres = this.temp['data']['optionarray']['2']
                this.inceptionv3 = this.temp['data']['optionarray']['1']
            })
        }
    }
}
</script>
