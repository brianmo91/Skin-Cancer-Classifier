<template>
<div>
    <FileUpload v-if="fileupFlag==true"/>
    <AlgoSelector v-if="algoFlag==true"/>
    <ChoicePie v-if="pieFlag==true"/>
   
</div>
</template>


<script>
import FileUpload from "./FileUpload.vue"
import AlgoSelector from "./AlgoSelector.vue"
import { EventBus } from "../event-bus.js";
import ChoicePie from './ChoicePie.vue';


export default {
    name:"Home",
    components: {FileUpload, AlgoSelector,ChoicePie},
    data() {
      return {
          algoFlag: false,
          fileupFlag: true,
          pieFlag: false
      }
    },
      mounted() {
          EventBus.$on('FILE_UPLOADED', () => {
              this.algoFlag = true;
              this.fileupFlag = false;
          });
          EventBus.$on('LOAD_PIE_CHARTS', () => {
              this.algoFlag = false;
              this.fileupFlag = false;
              this.pieFlag = true;
          }) 
      }
    }

</script>