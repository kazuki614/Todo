<template>
  <div>
    <v-list dense>
      <v-list-group
        :value="true"
        no-action
        sub-group
        v-if="todos.length"
      >
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title>{{ statusName }}</v-list-item-title>
          </v-list-item-content>
        </template>
        <v-list-item
          :key="todo.id"
          style="height: 45px"
          v-for="todo in todos"
          @click="onEditTodo(todo)"
        >
          <v-list-item-content>
            <v-checkbox
              v-model="selected"
              :label=todo.title
              :value=todo
              @change="changeStatus(todo)"
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
      </v-list-group>
    </v-list>
  </div>
</template>

<script>
import { mapActions, mapMutations, mapState } from 'vuex'

export default {
  props: {
    todos: JSON,
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
