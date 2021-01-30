<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
     <h1>Skin Cancer Classifier</h1>

      <v-spacer></v-spacer>

    </v-app-bar>
    <v-container fluid grid-list-md>
      <v-layout justify-center="" >
        <v-flex xs12>
          <v-content>
            
            <Home/>
          </v-content>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
import Home from './components/Home';
export default {
  name: 'App',

  components: {
    Home
  },

  data: () => ({
    //
  }),
};
</script>
