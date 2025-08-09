<template>
  <div class="game-selection">
    <div class="header">
      <h1 class="title">Choose Your Rhythm Game</h1>
      <p class="subtitle">Select a game to start your musical journey</p>
    </div>
    
    <div class="games-grid">
      <GameCard 
        v-for="game in games" 
        :key="game.id" 
        :game="game"
        @click="selectGame(game)"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import GameCard from './GameCard.vue'

const games = ref([
  {
    id: 1,
    name: 'Beat Saber',
    image: 'https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=400&h=300&fit=crop',
    songsCount: 150,
    difficulty: 'Medium',
    playersCount: 1250
  },
  {
    id: 2,
    name: 'Osu!',
    image: 'https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=400&h=300&fit=crop',
    songsCount: 500,
    difficulty: 'Hard',
    playersCount: 2100
  },
  {
    id: 3,
    name: 'Dance Dance Revolution',
    image: 'https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=400&h=300&fit=crop',
    songsCount: 200,
    difficulty: 'Easy',
    playersCount: 890
  }
])

const selectGame = (game) => {
  console.log('Selected game:', game.name)
  // Here you can add navigation logic to the specific game page
}
</script>

<style scoped>
.game-selection {
  min-height: 100vh;
  padding: 6rem 2rem 2rem 2rem; /* Added top padding for navigation */
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.header {
  text-align: center;
  margin-bottom: 3rem;
  color: white;
}

.title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.subtitle {
  font-size: 1.2rem;
  opacity: 0.9;
  margin: 0;
}

.games-grid {
  display: grid;
  grid-template-columns: repeat(3, 300px);
  gap: 2rem;
  max-width: 1200px;
  width: 100%;
  justify-content: center;
}

@media (max-width: 1024px) {
  .games-grid {
    grid-template-columns: repeat(2, 300px);
  }
}

@media (max-width: 768px) {
  .game-selection {
    padding: 5rem 1rem 1rem 1rem;
  }
  
  .title {
    font-size: 2rem;
  }
  
  .subtitle {
    font-size: 1rem;
  }
  
  .games-grid {
    grid-template-columns: 300px;
    gap: 1rem;
  }
}
</style> 