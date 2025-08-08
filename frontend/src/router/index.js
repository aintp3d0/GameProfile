import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import GameSelection from '../components/GameSelection.vue'

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
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 