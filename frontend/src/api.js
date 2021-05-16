import axios from 'axios'

export default {
  async getAllTodos () {
    const response = await axios.get('/api')
    return response.data
  },
  async createTodo (item) {
    const response = await axios.post('/api', item)
    return response.data
  },
  async deleteTodo (item) {
    const data = {
      id: item.id
    }
    const response = await axios.delete('/api', { data: data })
    return response.data
  },
  async updateTodo (item) {
    const response = await axios.put('/api', item)
    return response.data
  }
}
