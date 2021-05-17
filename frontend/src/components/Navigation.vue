<template>
  <div id="nav">
    <v-navigation-drawer
      id="navigation-drawer"
      app
      dark
      clipped
      v-model="drawer"
      width="10%"
      height="100%"
    >
      <v-list dense nav>
         <v-list-item
           v-for="(item) in items"
           :to="item.link"
           :key="item.id"
         >
          <v-list-item-action>
            <v-icon>{{item.icon}}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{item.title}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  name: 'Navigation',
  data () {
    return {
      value: true,
      items: [
        { link: '/', icon: 'mdi-format-list-checks', title: 'All', id: 1 },
        { link: '/today', icon: 'mdi-calendar-today', title: 'Today', id: 2 },
        { link: '/week', icon: 'mdi-calendar-week', title: 'Next 7 Days', id: 3 },
        { link: '/calendar', icon: 'mdi-calendar', title: 'Calendar', id: 4 }
      ]
    }
  },
  computed: {
    drawer: {
      get () {
        return this.$store.state.drawer
      },
      set (val) {
        this.$store.commit('setDrawer', val)
      }
    }
  }
}
</script>
