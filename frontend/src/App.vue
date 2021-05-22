<template>
  <v-app id="inspire">
    <AppBar/>
    <Navigation/>
      <v-main>
        <v-container fluid style="height: 100%">
          <router-view style="padding-top: 40px">
          </router-view>
        </v-container>
      </v-main>
  </v-app>
</template>

<script>
import Navigation from './components/Navigation'
import AppBar from './components/AppBar'

export default {
  name: 'App',
  components: {
    Navigation,
    AppBar
  },
  data: () => ({
    //
  })
}
</script>
