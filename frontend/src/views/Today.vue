<template>
  <div style="padding: 30px">
    <v-row>
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
      <v-col
        cols="12"
        md="4"
      ></v-col>
    </v-row>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import store from '../store/index'
import TodoInput from '../components/TodoInput'
import List from '../components/List'

export default {
  components: {
    TodoInput,
    List
  },
  computed: {
    ...mapState(['todos']),
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
