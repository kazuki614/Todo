import Vue from 'vue'
import VueRouter from 'vue-router'
import AllView from '../views/AllView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'All',
    component: AllView
  },
  {
    path: '/calendar',
    name: 'Calendar',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Calendar.vue')
  },
  {
    path: '/today',
    name: 'today',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Today.vue')
  },
  {
    path: '/week',
    name: 'week',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Week.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
