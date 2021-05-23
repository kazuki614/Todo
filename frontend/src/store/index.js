import Vue from 'vue'
import Vuex from 'vuex'

import api from '../api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [],
    editTodo: [],
    drawer: null
  },
  getters: {
    doingTodos: state => {
      return state.todos.filter((todo) => todo.status === 0)
    },
    doneTodos: state => {
      return state.todos.filter((todo) => todo.status === 1)
    },
    allTodos: state => {
      return {
        DOING: state.todos.filter((todo) => todo.status === 0),
        DONE: state.todos.filter((todo) => todo.status === 1)
      }
    }
  },
  mutations: {
    setTodos (state, { todos }) {
      state.todos = todos
    },
    setDoingTodos (state, { todos }) {
      state.doingTodos = todos.filter((todo) => todo.status === 0)
    },
    setDoneTodos (state, { todos }) {
      state.doneTodos = todos.filter((todo) => todo.status === 1)
    },
    removeTodo (state, { item }) {
      state.todos = state.todos.filter((todo, index) => {
        if (todo.id !== item.id) return true
      })
    },
    setTodo (state, { todo }) {
      state.todos.push(todo)
    },
    updateTodo (state, { item }) {
      state.todos.find((todo) => {
        if (todo.id === item.id) {
          todo = item
        }
      })
    },
    setDrawer (state, { payload }) {
      state.drawer = payload
    },
    setEditTodo (state, { todo }) {
      state.editTodo = todo
    }
  },
  actions: {
    async loadAllTodos ({ commit }) {
      const todos = await api.getAllTodos()
      commit('setTodos', { todos })
      commit('setDoingTodos', { todos })
      commit('setDoneTodos', { todos })
    },
    async createTodo ({ commit }, { item }) {
      const todo = await api.createTodo(item)
      commit('setTodo', { todo })
    },
    async deleteTodo ({ commit }, { item }) {
      await api.deleteTodo(item)
      commit('removeTodo', { item })
    },
    async updateTodo ({ commit }, { item }) {
      await api.updateTodo(item)
      commit('updateTodo', { item })
    },
    async toComplete ({ commit }, { item }) {
      item.status = 1
      await api.updateTodo(item)
    },
    async toIncomplete ({ commit }, { item }) {
      item.status = 0
      await api.updateTodo(item)
    }
  },
  modules: {}
})
