<template>
  <v-app id="inspire">
    <AppBar/>
    <Navigation/>
    <v-main>
      <router-view style="padding-top: 55px">
        <AllView/>
        <AllView2/>
        <Calendar/>
      </router-view>
    </v-main>
  </v-app>
</template>

<script>
import AllView from './views/AllView'
import Navigation from './components/Navigation'
import AppBar from './components/AppBar'
import Calendar from './views/Calendar'
import AllView2 from './views/AllView2'

export default {
  name: 'App',
  components: {
    AllView,
    Navigation,
    AppBar,
    Calendar,
    AllView2
  },
  data: () => ({
    //
  })
}
</script>
