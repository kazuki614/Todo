<template>
  <div>
    <v-row>
      <v-col
        cols="12"
        md="11"
      >
        <v-text-field
          v-model="titleName"
          label="TODO"
          hide-details
          append-icon="mdi-calendar"
          @keydown.enter="createTodo({ item: {title: titleName, due: dueDate} })"
          @click:append="viewCalendar"
          rounded
          solo
        ></v-text-field>
        <v-dialog
          v-if="view"
          ref="dialog"
          v-model="view"
          :return-value.sync="dueDate"
          persistent
          width="290px"
        >
          <v-date-picker
            v-model="dueDate"
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
              @click="$refs.dialog.save(dueDate)"
            >
              OK
            </v-btn>
          </v-date-picker>
        </v-dialog>
      </v-col>
      <v-col
        cols="12"
        md="1"
      >
       <v-btn
         fab
         dark
         color="indigo"
         @click="createTodo({ item: {title: titleName, due: dueDate} })"
        >
          <v-icon dark>
            mdi-plus
          </v-icon>
        </v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoInput',
  props: {
    titleName: { type: String },
    dueDate: { type: Date },
    view: { type: Boolean, default: false }
  },
  methods: {
    ...mapActions(['createTodo']),
    viewCalendar () {
      this.view = !this.view
    }
  }
}
</script>
