<template>
  <div
    style="padding: 20px; height: 100%">
    <v-row
      style="height: 100%">
      <v-col
        cols="12"
        sm="8">
        <TodoInput
          :title-name="title"
          :due-date="date"
          :view="view"
        ></TodoInput>
        <List
          :selected="selected"
          :todos="doingTodos"
          status-name="DOING"
        ></List>
        <v-divider></v-divider>
        <List
          :selected="doneTodos"
          :todos="doneTodos"
          status-name="DONE"
        ></List>
      </v-col>
      <v-divider vertical></v-divider>
      <!-- EditView -->
      <v-col
        cols="12"
        md="4"
      >
        <EditForm
          v-if="Boolean(Object.keys(editTodo).length)"
        ></EditForm>
        <NotSelect
          v-else
        ></NotSelect>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import store from '../store/index'
import TodoInput from '../components/TodoInput'
import List from '../components/List'
import EditForm from '../components/EditForm'
import NotSelect from '../components/NotSelect'

export default {
  components: {
    TodoInput,
    List,
    EditForm,
    NotSelect
  },
  computed: {
    ...mapState(['todos', 'editTodo']),
    doingTodos () {
      return store.getters.doingTodos
    },
    doneTodos () {
      return store.getters.doneTodos
    }
  },
  async beforeRouteEnter (to, from, next) {
    await store.dispatch('loadAllTodos')
    next()
  },
  data: () => ({
    selected: [],
    title: '',
    date: '',
    view: false
  })
}
</script>
