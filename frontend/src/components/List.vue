<template>
  <div>
    <v-list dense>
      <v-list-group
        :value="true"
        v-if="doingTodos.length"
      >
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title>DOING</v-list-item-title>
          </v-list-item-content>
        </template>
        <v-list-item
          :key="todo.id"
          style="height: 45px"
          v-for="todo in doingTodos"
          @click="onEditTodo(todo)"
          v-bind:class="{active: activeItem === todo.id}"
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
    <v-list dense>
      <v-list-group
        :value="true"
        v-if="doneTodos.length"
      >
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title>DONE</v-list-item-title>
          </v-list-item-content>
        </template>
        <v-list-item
          :key="todo.id"
          style="height: 45px"
          v-for="todo in doneTodos"
          @click="onEditTodo(todo)"
          v-bind:class="{active: activeItem === todo.id}"
        >
          <v-list-item-content>
            <v-checkbox
              v-model="doneTodos"
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
    doingTodos: JSON,
    doneTodos: JSON,
    selected: Array
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
      this.isActive = !this.isActive
      this.activeItem = todo.id
      this.$store.commit('setEditTodo', { todo: todo })
    }
  },
  computed: {
    ...mapState(['editTodo'])
  },
  data: () => ({
    activeItem: null
  })
}
</script>
<style>
.active {
  background: #0d47a130;
}
</style>
