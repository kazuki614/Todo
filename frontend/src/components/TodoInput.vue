<template>
  <div>
    <v-text-field
      v-model="title"
      label="TODO"
      hide-details
      outlined
      append-icon="mdi-calendar"
      @keydown.enter="createTodo({ item: {title: title, due: due} })"
      @click:append="viewCalendar"
      rounded
    ></v-text-field>
    <v-dialog
      v-if="view"
      ref="dialog"
      v-model="view"
      :return-value.sync="due"
      persistent
      width="290px"
    >
      <v-date-picker
        v-model="due"
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
          @click="$refs.dialog.save(due)"
        >
          OK
        </v-btn>
      </v-date-picker>
    </v-dialog>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoInput',
  props: {
    title: { type: String },
    due: { type: Date },
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
