<template>
  <nav class="navigation">
    <div class="nav-container">
      <router-link to="/" class="nav-link" active-class="active">
        Home
      </router-link>
      <router-link to="/games" class="nav-link" active-class="active">
        Games
      </router-link>
      <router-link to="/users" class="nav-link" active-class="active">
        Users
      </router-link>
    </div>
  </nav>
</template>

<style scoped>
.navigation {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(10px);
  z-index: 1000;
  padding: 1rem 0;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  gap: 2rem;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  transition: all 0.3s ease;
}

.nav-link:hover {
  background: rgba(255, 255, 255, 0.1);
}

.nav-link.active {
  background: rgba(255, 255, 255, 0.2);
  color: #ffd700;
}
</style> 