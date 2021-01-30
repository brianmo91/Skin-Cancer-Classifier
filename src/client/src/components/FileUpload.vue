<template>
  <div>
     
    <v-container fluid grid-list-md style="max-width: 40%; border: 3px solid #1976D2;margin-top: 200px; border-radius: 10px; padding: 30px 40px 30px 80px">
      <v-card-title style="margin-left: 110px; margin-bottom:100px; margin-top:20px;font-size:30px" >Upload your image </v-card-title>
      <v-layout justify-center="" >
        <v-flex xs12>
          <v-file-input v-model="files" name="image_file" type="file"> </v-file-input>
          <v-btn  min-width="200" min-height="50" style="margin-left:160px; margin-bottom: 30px;margin-top: 30px" class="primary" type="submit" v-on:click="uploadImage(),loadAlgoSelector()"> Upload </v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import axios from 'axios'
  import { EventBus } from "../event-bus.js";

  export default {
    name: 'FileUpload',
    data() {
      return {
          files:[]
      }
    },
    methods: {
        loadAlgoSelector() {
            EventBus.$emit('FILE_UPLOADED')
        },
        //This function is activated once upload is selected. 
        uploadImage() {
            const formData = new FormData();
            for(var i = 0; i < this.files.length; i++) {
                let file = this.files[i]
                formData.append('image_file', file);
            }
            //request url
            const url = 'http://localhost:5000/upload'

            //this is the post request to send data to the server ...app.route (/upload)
            return axios.post(url,formData)
        }
    }
  }
</script>