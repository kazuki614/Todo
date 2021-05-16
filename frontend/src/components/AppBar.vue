<template>
  <v-app-bar
    app
    absolute
    flat
    clipped-left
    dark
    >
    <v-app-bar-nav-icon
      @click.stop="setDrawer(!drawer)"
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
    </v-app-bar-nav-icon>
    <v-toolbar-title
    >TODO
    </v-toolbar-title>
  </v-app-bar>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
export default {
  name: 'AppBar',
  computed: {
    ...mapState(['drawer'])
  },
  methods: {
    ...mapMutations({
      setDrawer: 'setDrawer'
    })
  }
}
</script>
