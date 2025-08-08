<template>
  <div class="game-card" @mouseenter="isHovered = true" @mouseleave="isHovered = false">
    <div class="card-image">
      <img :src="game.image" :alt="game.name" />
      <div class="overlay" :class="{ 'show': isHovered }">
        <div class="game-info">
          <h3 class="game-name">{{ game.name }}</h3>
          <div class="game-stats">
            <div class="stat">
              <span class="stat-label">Songs</span>
              <span class="stat-value">{{ game.songsCount }}</span>
            </div>
            <div class="stat">
              <span class="stat-label">Difficulty</span>
              <span class="stat-value">{{ game.difficulty }}</span>
            </div>
            <div class="stat">
              <span class="stat-label">Players</span>
              <span class="stat-value">{{ game.playersCount }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  game: {
    type: Object,
    required: true
  }
})

const isHovered = ref(false)
</script>

<style scoped>
.game-card {
  position: relative;
  width: 300px;
  height: 200px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
}

.game-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.card-image {
  position: relative;
  width: 100%;
  height: 100%;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.8) 0%, rgba(0, 0, 0, 0.6) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.overlay.show {
  opacity: 1;
}

.game-info {
  text-align: center;
  color: white;
  padding: 20px;
}

.game-name {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 15px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.game-stats {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.stat {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 4px 0;
}

.stat-label {
  font-size: 0.9rem;
  opacity: 0.9;
}

.stat-value {
  font-size: 1rem;
  font-weight: bold;
  color: #ffd700;
}
</style> 