<template>
  <div>
    <v-checkbox
      v-for="todo in todos"
      :key="todo.id"
      :label="todo.title"
      @change="onChange(todo)"
      hide-details
    ></v-checkbox>
    <button @click="getAll">Display table</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      todos: []
    }
  },
  methods: {
    getAll () {
      const path = 'http://127.0.0.1:5000/all'
      axios.get(path)
        .then(response => {
          this.todos = response.data
        })
    },
    onChange (todo) {
      console.log(todo)
      console.log(todo.status)
      todo.status = Number(todo.status === 0)
      console.log(todo.status)
    }
  }
}
</script>
