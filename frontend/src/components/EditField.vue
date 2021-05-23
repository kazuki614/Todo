<template>
  <div>
    <v-row>
      <v-col
        cols="12"
        md="1"
      >
        <v-checkbox
          :input-value="Boolean(editTodo.status)"
          @change="changeStatus(editTodo)"
          hide-details
        ></v-checkbox>
      </v-col>
      <v-col
        cols="12"
        md="11"
        id="date_picker"
      >
        <EditDate
          :edit-date="editTodo.due"
          :menu="menu"
        ></EditDate>
      </v-col>
    </v-row>
    <EditTextField/>
    <v-textarea
      rows="20"
      outlined
      flat
      style="padding-top: 15px"
    ></v-textarea>
  </div>
</template>

<script>
import EditDate from './EditDate'
import EditTextField from './EditTextField'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'EditField',
  components: {
    EditDate,
    EditTextField
  },
  computed: {
    ...mapState(['editTodo'])
  },
  methods: {
    ...mapActions(['updateTodo']),
    changeStatus (todo) {
      const status = Boolean(todo.status)
      todo.status = Number(!status)
    }
  }
}
</script>

<style scoped>

</style>
