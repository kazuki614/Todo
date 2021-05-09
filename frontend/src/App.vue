<template>
  <v-app id="inspire">
    <AppBar/>
    <Navigation/>
    <v-main>
      <router-view style="padding-top: 55px">
        <AllView/>
      </router-view>
    </v-main>
  </v-app>
</template>

<script>
import AllView from './components/AllView'
import Navigation from './components/Navigation'
import AppBar from './components/AppBar'

export default {
  name: 'App',
  components: {
    AllView,
    Navigation,
    AppBar
  },
  data: () => ({
    //
  })
}
</script>
