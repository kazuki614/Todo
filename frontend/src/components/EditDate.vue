<template>
  <v-menu
    v-model="menu"
    :close-on-content-click="false"
    :nudge-right="40"
    transition="scale-transition"
    offset-y
    min-width="auto"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-text-field
        v-model="editTodo.due"
        prepend-inner-icon="mdi-calendar"
        readonly
        v-bind="attrs"
        v-on="on"
        rounded
        hide-details
      ></v-text-field>
    </template>
    <v-date-picker
      v-model="editTodo.due"
      @input="menu = false"
    ></v-date-picker>
  </v-menu>
</template>

<script>
import { mapState } from 'vuex'

export default {
  props: {
    menu: { type: Boolean }
  },
  computed: {
    ...mapState(['editTodo'])
  }
}
</script>
<style>
#date_picker>.v-text-field--rounded>.v-input__control>.v-input__slot {
    padding: 0 !important;
}
</style>
