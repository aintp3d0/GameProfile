import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import GameSelection from '../components/GameSelection.vue'
import UsersPage from '../components/UsersPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/games',
    name: 'GameSelection',
    component: GameSelection
  },
  {
    path: '/users',
    name: 'UsersPage',
    component: UsersPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 