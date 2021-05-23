<template>
  <div>
    <v-list dense expand>
      <v-list-group
        :value="true"
        v-for="(all, index) in allTodos"
        :key="all"
      >
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title>{{Object.keys(allTodos)[index]}}</v-list-item-title>
          </v-list-item-content>
        </template>
          <v-list-item-group :v-model="allTodos">
          <v-list-item
            v-for="todo in all"
            :key="todo.id"
            @click="onEditTodo(todo)"
            sub-group
          >
          <v-list-item-content>
            <v-checkbox
              v-model="selected"
              :label=todo.title
              :value=todo
              @change="changeStatus(todo)"
              v-if="Object.keys(allTodos)[index]==='DOING'"
            ></v-checkbox>
            <v-checkbox
              :v-model="todo"
              :label=todo.title
              :value=todo
              @change="changeStatus(todo)"
              v-else
            ></v-checkbox>
          </v-list-item-content>
          <v-list-item-action>
            <v-list-item-action-text v-text="todo.due"></v-list-item-action-text>
          </v-list-item-action>
          <v-list-item-action>
            <v-btn
              icon
              @click="deleteTodo({ item: todo })"
            >
              <v-icon color="grey">mdi-delete</v-icon>
            </v-btn>
          </v-list-item-action>
          </v-list-item>
          </v-list-item-group>
      </v-list-group>
    </v-list>
  </div>
</template>

<script>
import { mapActions, mapMutations, mapState } from 'vuex'

export default {
  props: {
    allTodos: JSON,
    selected: Array,
    statusName: String
  },
  methods: {
    ...mapActions(['deleteTodo', 'toComplete', 'toIncomplete']),
    ...mapMutations(['setEditTodo']),
    changeStatus (todo) {
      if (todo.status === 0) {
        this.toComplete({ item: todo })
      } else {
        this.toIncomplete({ item: todo })
      }
    },
    onEditTodo (todo) {
      this.$store.commit('setEditTodo', { todo: todo })
    }
  },
  computed: {
    ...mapState(['editTodo'])
  }
}
</script>
