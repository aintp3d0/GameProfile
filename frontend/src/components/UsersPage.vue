<template>
  <div class="users-page">
    <div class="header">
      <h1 class="title">User Activities</h1>
      <p class="subtitle">Recent rhythm game performances and rankings</p>
    </div>
    
    <div class="table-container">
      <table class="users-table">
        <thead>
          <tr>
            <th>Username</th>
            <th>Game</th>
            <th>Song</th>
            <th>Rank</th>
            <th>Score</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id" class="user-row">
            <td class="username">
              <div class="user-info">
                <div class="avatar">{{ user.username.charAt(0).toUpperCase() }}</div>
                <span>{{ user.username }}</span>
              </div>
            </td>
            <td class="game">{{ user.game }}</td>
            <td class="song">{{ user.song }}</td>
            <td class="rank">
              <span class="rank-badge" :class="getRankClass(user.rank)">
                {{ user.rank }}
              </span>
            </td>
            <td class="score">{{ formatScore(user.score) }}</td>
            <td class="date">{{ formatDate(user.date) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const users = ref([
  {
    id: 1,
    username: 'RhythmMaster',
    game: 'Beat Saber',
    song: 'Through The Fire And Flames',
    rank: 'S',
    score: 985432,
    date: '2024-01-15T14:30:00Z'
  },
  {
    id: 2,
    username: 'BeatBreaker',
    game: 'Osu!',
    song: 'Blue Zenith',
    rank: 'A',
    score: 876543,
    date: '2024-01-15T13:45:00Z'
  },
  {
    id: 3,
    username: 'DanceQueen',
    game: 'Dance Dance Revolution',
    song: 'Butterfly',
    rank: 'SS',
    score: 999999,
    date: '2024-01-15T12:20:00Z'
  },
  {
    id: 4,
    username: 'SaberSlayer',
    game: 'Beat Saber',
    song: 'Gangnam Style',
    rank: 'B',
    score: 654321,
    date: '2024-01-15T11:15:00Z'
  },
  {
    id: 5,
    username: 'OsuLegend',
    game: 'Osu!',
    song: 'FREEDOM DiVE',
    rank: 'S',
    score: 912345,
    date: '2024-01-15T10:30:00Z'
  },
  {
    id: 6,
    username: 'DDRKing',
    game: 'Dance Dance Revolution',
    song: 'Sandstorm',
    rank: 'A',
    score: 789012,
    date: '2024-01-15T09:45:00Z'
  }
])

const getRankClass = (rank) => {
  const rankClasses = {
    'SS': 'rank-ss',
    'S': 'rank-s',
    'A': 'rank-a',
    'B': 'rank-b',
    'C': 'rank-c',
    'D': 'rank-d'
  }
  return rankClasses[rank] || 'rank-default'
}

const formatScore = (score) => {
  return score.toLocaleString()
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script>

<style scoped>
.users-page {
  min-height: 100vh;
  padding: 6rem 2rem 2rem 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
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

.table-container {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
  max-width: 1200px;
  width: 100%;
  overflow-x: auto;
}

.users-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95rem;
}

.users-table th {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  border-radius: 8px 8px 0 0;
}

.users-table td {
  padding: 1rem;
  border-bottom: 1px solid #e5e7eb;
  vertical-align: middle;
}

.users-table tr:hover {
  background: rgba(102, 126, 234, 0.05);
}

.user-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.avatar {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.1rem;
}

.username {
  font-weight: 600;
  color: #374151;
}

.game {
  color: #6b7280;
  font-weight: 500;
}

.song {
  color: #374151;
  max-width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.rank-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-weight: bold;
  font-size: 0.9rem;
  text-align: center;
  min-width: 40px;
  display: inline-block;
}

.rank-ss {
  background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
  color: #92400e;
}

.rank-s {
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
}

.rank-a {
  background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);
  color: white;
}

.rank-b {
  background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 100%);
  color: white;
}

.rank-c {
  background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
  color: white;
}

.rank-d {
  background: linear-gradient(135deg, #ef4444 0%, #f87171 100%);
  color: white;
}

.rank-default {
  background: #6b7280;
  color: white;
}

.score {
  font-family: 'Courier New', monospace;
  font-weight: bold;
  color: #059669;
  font-size: 1.1rem;
}

.date {
  color: #6b7280;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .users-page {
    padding: 5rem 1rem 1rem 1rem;
  }
  
  .title {
    font-size: 2rem;
  }
  
  .subtitle {
    font-size: 1rem;
  }
  
  .table-container {
    padding: 1rem;
  }
  
  .users-table th,
  .users-table td {
    padding: 0.75rem 0.5rem;
    font-size: 0.85rem;
  }
  
  .song {
    max-width: 150px;
  }
}
</style> 