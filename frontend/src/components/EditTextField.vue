<template>
  <v-text-field
    v-model="editTodo.title"
    hide-details
    @keydown.enter="updateTodo({item: editTodo})"
  ></v-text-field>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  methods: {
    ...mapActions(['updateTodo'])
  },
  computed: {
    ...mapState(['editTodo'])
  }
}
</script>
