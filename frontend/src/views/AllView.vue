<template>
  <div
    style="padding: 20px; height: 100%"
  >
    <v-row
      style="height: 100%"
    >
      <v-col
        cols="12"
        md="8"
      >
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
        v-if="Boolean(Object.keys(editTodo).length)"
        style="padding: 20px"
      >
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
        <v-row>
          <v-col
            cols="12"
            md="10"
          >
            <EditTextField/>
          </v-col>
          <v-col
            cols="12"
            md="1"
          >
            <UpdateButton/>
          </v-col>
        </v-row>
      </v-col>
      <!-- Non select case -->
      <v-col
        cols="12"
        md="4"
        v-else
      >
        <v-row
          justify="center"
          align-content="center"
        >
          <v-col
            cols="3"
          >
            <h1>Hello, World</h1>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import store from '../store/index'
import TodoInput from '../components/TodoInput'
import List from '../components/List'
import EditTextField from '../components/EditTextField'
import EditDate from '../components/EditDate'
import UpdateButton from '../components/UpdateButton'

export default {
  components: {
    TodoInput,
    List,
    EditDate,
    EditTextField,
    UpdateButton
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
    view: false,
    menu: false
  }),
  methods: {
    ...mapActions(['updateTodo']),
    changeStatus (todo) {
      const status = Boolean(todo.status)
      todo.status = Number(!status)
    }
  }
}
</script>
