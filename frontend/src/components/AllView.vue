<template>
  <div>
    <v-text-field
      v-model="newTodo.title"
      label="TODO"
    ></v-text-field>
    <button @click="createTodo">ADD</button>
    <v-data-table
      dense
      :headers="headers"
      :items="doingTodo"
      :single-select="singleSelect"
      hide-default-header
      hide-default-footer
      show-select
      :item-key="id"
      v-model="selected"
    >
      <template v-slot:item.actions="{ item }">
        <v-icon
          small
          class="mr-2"
          @click="updateTodo(item)"
        >mdi-pencil</v-icon>
        <v-icon
          small
          @click="deleteTodo(item)"
        >mdi-delete</v-icon>
      </template>
    </v-data-table>
    <button @click="getDoingTodo">Display doing table</button>
    <button @click="getDoneTodo">Display done table</button>
    <v-data-table
      dense
      :headers="headers"
      :items="doneTodo"
      :single-select="false"
      hide-default-header
      hide-default-footer
      show-select
      :item-key="id"
      v-model="doneTodo"
    ></v-data-table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'AllView',

  data: () => ({
    headers: [
      { text: 'title', value: 'title' },
      { text: 'ID', value: 'id' },
      { text: 'Status', value: 'status' },
      { text: 'Due Date', value: 'due' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    newTodo: {
      title: ''
    },
    singleSelect: true,
    selected: [],
    doneTodo: [],
    doingTodo: []
  }),
  mounted () {
    this.getDoneTodo()
    this.getDoingTodo()
  },
  methods: {
    getDoingTodo () {
      axios.get('/doing')
        .then(response => {
          this.doingTodo = response.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    getDoneTodo () {
      axios.get('/done')
        .then(response => {
          this.doneTodo = response.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    createTodo () {
      /// TODO 日付などを選択できるようにする
      const path = 'http://127.0.0.1:5000/create'
      axios.post(path, this.newTodo)
        .then(response => {
          console.log(response.data)
          this.doingTodo.push(this.newTodo)
        })
    },
    deleteTodo (item) {
      const data = {
        id: item.id
      }
      const path = 'http://127.0.0.1:5000/delete'
      axios.post(path, data)
        .then(response => {
          this.doingTodo = this.doingTodo.filter(function (item, index) {
            if (item.id !== data.id) return true
          })
          console.log(response.data)
        })
    },
    updateTodo (item) {
      const path = 'http://127.0.0.1:5000/update'
      axios.post(path, item)
        .then(response => {
          console.log(response.data)
          return true
        })
    },
    completeTodo (data) {
      const path = 'http://127.0.0.1:5000/complete'
      axios.post(path, data)
        .then(response => {
          console.log(response.data)
          data.status = 1
          return data
        })
    }
  },
  watch: {
    selected: function () {
      if (this.selected.length === 1) {
        const data = {
          id: this.selected[0].id
        }
        this.completeTodo(data)
        this.selected[0].status = 1
        /// remove selected item
        this.doingTodo = this.doingTodo.filter(function (item, _) {
          if (item.id !== data.id) return true
        })
        this.doneTodo.push(this.selected[0])
      }
    },
    doneTodo: function (nowData, oldData) {
      nowData = JSON.stringify(nowData)
      const diff = oldData.filter(item => nowData.indexOf(JSON.stringify(item)) < 0)[0]
      console.log('diff', diff)
      if (diff !== undefined) {
        diff.status = 0
        this.updateTodo(diff)
        this.doingTodo.push(diff)
        this.selected = []
      }
    }
  }
}
</script>
