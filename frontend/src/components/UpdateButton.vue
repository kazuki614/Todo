<template>
  <v-btn
   fab
   dark
   small
   @click="updateTodo({item: editTodo})"
  >
    <v-icon dark>
      mdi-send-outline
    </v-icon>
  </v-btn>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'UpdateButton',
  methods: {
    ...mapActions(['updateTodo'])
  },
  computed: {
    ...mapState(['editTodo'])
  }
}
</script>
