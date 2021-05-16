<template>
  <v-row class="fill-height">
    <v-col>
      <div style="padding: 0 40px 0 40px">
      <v-sheet height="60">
        <v-toolbar
          flat
        >
          <v-btn
            outlined
            class="mr-4"
            color="grey darken-2"
            @click="setToday"
          >
            Today
          </v-btn>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="prev"
          >
            <v-icon small>
              mdi-chevron-left
            </v-icon>
          </v-btn>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="next"
          >
            <v-icon small>
              mdi-chevron-right
            </v-icon>
          </v-btn>
          <v-toolbar-title v-if="$refs.calendar">
            {{ $refs.calendar.title }}
          </v-toolbar-title>
          <v-spacer></v-spacer>
          <v-menu
            bottom
            right
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                outlined
                color="grey darken-2"
                v-bind="attrs"
                v-on="on"
              >
                <span>{{ typeToLabel[type] }}</span>
                <v-icon right>
                  mdi-menu-down
                </v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item @click="type = 'day'">
                <v-list-item-title>Day</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = 'month'">
                <v-list-item-title>Month</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-toolbar>
      </v-sheet>
      <v-card height="700">
        <v-calendar
          ref="calendar"
          v-model="focus"
          color="primary"
          :events="changeKey(todos)"
          :type="type"
          @click:more="viewDay"
          @click:date="viewDay"
        ></v-calendar>
      </v-card>
      </div>
    </v-col>
  </v-row>
</template>

<script>

import store from '../store'
import { mapState } from 'vuex'

export default {
  data: () => ({
    focus: '',
    type: 'month',
    typeToLabel: {
      month: 'Month',
      day: 'Day'
    },
    event: []
  }),
  computed: {
    ...mapState(['todos'])
  },
  async beforeRouteEnter (to, from, next) {
    await store.dispatch('loadAllTodos')
    next()
  },
  methods: {
    changeKey (todos) {
      /// title -> name, due_date => start, end
      return todos.map(todo => {
        if (Number(todo.status) === 0) {
          return { name: todo.title, start: todo.due, end: todo.due, color: 'indigo' }
        } else {
          return { name: todo.title, start: todo.due, end: todo.due, color: 'grey' }
        }
      })
    },
    viewDay ({ date }) {
      this.focus = date
      this.type = 'day'
    },
    getEventColor (event) {
      return event.color
    },
    setToday () {
      this.focus = ''
    },
    prev () {
      this.$refs.calendar.prev()
    },
    next () {
      this.$refs.calendar.next()
    }
  }
}
</script>
