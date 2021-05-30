<template>
  <div style="padding: 20px; height: 100%">
    <v-row
      style="height: 100%"
    >
      <v-col
        cols="12"
        md="8"
      >
        <TodoInput
          :title="title"
          :due="date"
          :view="view"
        ></TodoInput>
        <List
          :selected="selected"
          :doing-todos="doingTodos"
          :done-todos="doneTodos"
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
      const now = new Date()
      return store.getters.doingTodos.filter((todo) => {
        if (todo.due === this.formatDate(now)) {
          return todo
        }
      })
    },
    doneTodos () {
      const now = new Date()
      return store.getters.doneTodos.filter((todo) => {
        if (todo.due === this.formatDate(now)) {
          return todo
        }
      })
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
  }),
  methods: {
    formatDate (dt) {
      const year = dt.getFullYear()
      const month = ('00' + (dt.getMonth() + 1)).slice(-2)
      const day = ('00' + dt.getDate()).slice(-2)
      return (year + '-' + month + '-' + day)
    }
  }
}
</script>
