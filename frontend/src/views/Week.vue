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
      return store.getters.doingTodos.filter((todo) => {
        for (let i = 1; i <= this.addDate; i++) {
          if (todo.due === this.getDate(i)) {
            return todo
          }
        }
      })
    },
    doneTodos () {
      return store.getters.doneTodos.filter((todo) => {
        for (let i = 1; i <= this.addDate; i++) {
          if (todo.due === this.getDate(i)) {
            return todo
          }
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
    view: false,
    addDate: 7
  }),
  methods: {
    getDate (day) {
      const date = new Date()
      date.setDate(date.getDate() + day)
      const year = date.getFullYear()
      const month = ('00' + (date.getMonth() + 1)).slice(-2)
      day = ('00' + date.getDate()).slice(-2)
      return year + '-' + month + '-' + day
    }
  }
}
</script>
