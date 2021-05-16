<template>
  <div style="padding: 30px">
    <v-row>
      <v-col
        cols="12"
        md="8"
      >
<!--        <v-text-field-->
<!--          v-model="title"-->
<!--          label="TODO"-->
<!--          hide-details-->
<!--          outlined-->
<!--          append-icon="mdi-calendar"-->
<!--          @keydown.enter="createTodo({ item: {title: title, due: date} })"-->
<!--          @click:append="viewCalendar"-->
<!--          rounded-->
<!--        ></v-text-field>-->
<!--        <v-dialog-->
<!--          v-if="view"-->
<!--          ref="dialog"-->
<!--          v-model="view"-->
<!--          :return-value.sync="date"-->
<!--          persistent-->
<!--          width="290px"-->
<!--        >-->
<!--          <v-date-picker-->
<!--            v-model="date"-->
<!--            scrollable-->
<!--          >-->
<!--            <v-spacer></v-spacer>-->
<!--            <v-btn-->
<!--              text-->
<!--              color="primary"-->
<!--              @click="view = false"-->
<!--            >-->
<!--              Cancel-->
<!--            </v-btn>-->
<!--            <v-btn-->
<!--              text-->
<!--              color="primary"-->
<!--              @click="$refs.dialog.save(date)"-->
<!--            >-->
<!--              OK-->
<!--            </v-btn>-->
<!--          </v-date-picker>-->
<!--        </v-dialog>-->
<!--        <v-list dense>-->
<!--          <v-list-group-->
<!--            :value="true"-->
<!--            no-action-->
<!--            sub-group-->
<!--            v-if="doingTodos.length"-->
<!--          >-->
<!--            <template v-slot:activator>-->
<!--              <v-list-item-content>-->
<!--                <v-list-item-title>DOING</v-list-item-title>-->
<!--              </v-list-item-content>-->
<!--            </template>-->
<!--            <v-list-item-->
<!--              :key="todo.id"-->
<!--              style="height: 45px"-->
<!--              v-for="todo in doingTodos"-->
<!--            >-->
<!--              <v-list-item-content>-->
<!--                <v-checkbox-->
<!--                  v-model="selected"-->
<!--                  :label=todo.title-->
<!--                  :value=todo-->
<!--                  @change="toComplete(todo)"-->
<!--                ></v-checkbox>-->
<!--              </v-list-item-content>-->
<!--              <v-list-item-action>-->
<!--                <v-list-item-action-text v-text="todo.due"></v-list-item-action-text>-->
<!--              </v-list-item-action>-->
<!--              <v-list-item-action>-->
<!--                <v-btn-->
<!--                  icon-->
<!--                  @click="deleteTodo({ item: todo })"-->
<!--                >-->
<!--                  <v-icon color="grey">mdi-delete</v-icon>-->
<!--                </v-btn>-->
<!--              </v-list-item-action>-->
<!--              <v-list-item-action>-->
<!--                <v-btn icon>-->
<!--                  <v-icon color="grey">mdi-pencil</v-icon>-->
<!--                </v-btn>-->
<!--              </v-list-item-action>-->
<!--            </v-list-item>-->
<!--          </v-list-group>-->
<!--        </v-list>-->
<!--        <v-list dense>-->
<!--          <v-list-group-->
<!--            :value="true"-->
<!--            no-action-->
<!--            sub-group-->
<!--            color="grey"-->
<!--            v-if="doneTodos.length"-->
<!--          >-->
<!--            <template v-slot:activator>-->
<!--              <v-list-item-content>-->
<!--                <v-list-item-title>DONE</v-list-item-title>-->
<!--              </v-list-item-content>-->
<!--            </template>-->
<!--            <v-list-item-->
<!--              v-for="todo in doneTodos"-->
<!--              :key="todo.id"-->
<!--              style="height: 45px"-->
<!--            >-->
<!--              <v-list-item-content>-->
<!--                <v-checkbox-->
<!--                  v-model="doneTodos"-->
<!--                  :label=todo.title-->
<!--                  :value=todo-->
<!--                  @change="toIncomplete(todo)"-->
<!--                ></v-checkbox>-->
<!--              </v-list-item-content>-->
<!--              <v-list-item-action>-->
<!--                <v-list-item-action-text v-text="todo.due"></v-list-item-action-text>-->
<!--              </v-list-item-action>-->
<!--              <v-list-item-action>-->
<!--                <v-btn-->
<!--                  icon-->
<!--                  @click="deleteTodo({ item: todo })"-->
<!--                >-->
<!--                  <v-icon color="grey">mdi-delete</v-icon>-->
<!--                </v-btn>-->
<!--              </v-list-item-action>-->
<!--              <v-list-item-action>-->
<!--                <v-btn icon>-->
<!--                  <v-icon color="grey">mdi-pencil</v-icon>-->
<!--                </v-btn>-->
<!--              </v-list-item-action>-->
<!--            </v-list-item>-->
<!--          </v-list-group>-->
<!--        </v-list>-->
        <v-text-field
          v-model="newTodo.title"
          label="TODO"
          hide-details
          outlined
          append-icon="mdi-calendar"
          @keydown.enter="createTodo"
          @click:append="viewCalendar"
          rounded
        ></v-text-field>
        <v-dialog
          v-if="view"
          ref="dialog"
          v-model="view"
          :return-value.sync="date"
          persistent
          width="290px"
        >
          <v-date-picker
            v-model="date"
            scrollable
          >
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              @click="view = false"
            >
              Cancel
            </v-btn>
            <v-btn
              text
              color="primary"
              @click="$refs.dialog.save(date)"
            >
              OK
            </v-btn>
          </v-date-picker>
        </v-dialog>
        <v-list dense>
          <v-list-group
            :value="true"
            no-action
            sub-group
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
            >
              <v-list-item-content>
                <v-checkbox
                  v-model="selected"
                  :label=todo.title
                  :value=todo
                  @change="toComplete(todo)"
                ></v-checkbox>
              </v-list-item-content>
              <v-list-item-action>
                <v-list-item-action-text v-text="todo.due"></v-list-item-action-text>
              </v-list-item-action>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="grey">mdi-delete</v-icon>
                </v-btn>
              </v-list-item-action>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="grey">mdi-pencil</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-group>
        </v-list>
        <v-divider></v-divider>
        <v-list dense>
          <v-list-group
            :value="true"
            no-action
            sub-group
            color="grey"
          >
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title>DOING</v-list-item-title>
              </v-list-item-content>
            </template>
            <v-list-item
              v-for="todo in doneTodos"
              :key="todo.id"
              style="height: 45px"
            >
              <v-list-item-content>
                <v-checkbox
                  v-model="doneTodos"
                  :label=todo.title
                  :value=todo
                  @change="toIncomplete(todo)"
                ></v-checkbox>
              </v-list-item-content>
              <v-list-item-action>
                <v-list-item-action-text v-text="todo.due"></v-list-item-action-text>
              </v-list-item-action>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="grey">mdi-delete</v-icon>
                </v-btn>
              </v-list-item-action>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="grey">mdi-pencil</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-group>
        </v-list>
        <div>TESTTESTTESTTEST</div>
        <List
          status="DOING"
          :selected="selected"
          :todos="doingTodos"
          @change="toComplete"
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
import axios from 'axios'
import List from '@/components/List'

export default {
  components: {
    List
  },
  data: () => ({
    todos: [],
    selected: [],
    doingTodos: [],
    doneTodos: [],
    newTodo: [{
      title: ''
    }],
    date: '',
    view: ''
  }),
  mounted () {
    this.getAllTodos()
  },
  methods: {
    getDoingTodo () {
      this.doingTodos = this.todos.filter((todo) => todo.status === 0)
    },
    getDoneTodo () {
      this.doneTodos = this.todos.filter((todo) => todo.status === 1)
    },
    getAllTodos () {
      axios.get('/api')
        .then(response => {
          this.todos = response.data
          this.getDoneTodo()
          this.getDoingTodo()
        })
    },
    toComplete (item) {
      const status = Boolean(item.status)
      item.status = Number(!status)
      this.doingTodos = this.doingTodos.filter((todo, _) => {
        if (todo.id !== item.id) return true
      })
      this.selected = []
      this.doneTodos.push(item)
    },
    toIncomplete (item) {
      const status = Boolean(item.status)
      item.status = Number(!status)
      this.doneTodos = this.doneTodos.filter((todo, _) => {
        if (todo.id !== item.id) return true
      })
      this.selected = []
      this.doingTodos.push(item)
    },
    createTodo () {},
    viewCalendar () {
      this.view = !this.view
    }
  }
}
</script>
