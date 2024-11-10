<template>
  <header class="header">
    <div class="header-container">
      <!-- Logo section -->
      <div class="logo-section">
        <img src="https://zakupki.mos.ru/static/media/pp_logo.80b7ad86dad21f1f5a4d3d170bfb13be.svg" alt="Портал поставщиков" class="logo" />
        <button class="menu-button" @click="toggleMenu">
          <span>Меню</span>
          <MenuIcon class="icon" />
        </button>
      </div>

      <!-- Navigation section -->
      <nav class="nav-section" :class="{ 'nav-active': isMenuOpen }">
        <a href="#" class="nav-link">
          <HeadphonesIcon class="icon" />
          <span>Оставить обращение</span>
        </a>
        <a href="#" class="nav-link">
          <LightbulbIcon class="icon" />
          <span>Центр поддержки</span>
        </a>
        <a href="#" class="nav-link">
          <MapPinIcon class="icon" />
          <span>обл Свердловская</span>
        </a>
      </nav>

      <!-- Actions section -->
      <div class="actions-section">
        <button class="icon-button">
          <SearchIcon class="icon" />
        </button>
        <button class="icon-button">
          <ShoppingCartIcon class="icon" />
        </button>
        <a href="#" class="text-button">Войти</a>
        <a href="#" class="primary-button">Зарегистрироваться</a>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'
import { 
  Menu as MenuIcon,
  Headphones as HeadphonesIcon,
  Lightbulb as LightbulbIcon,
  MapPin as MapPinIcon,
  Search as SearchIcon,
  ShoppingCart as ShoppingCartIcon
} from 'lucide-vue-next'

const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}
</script>

<style scoped>
.header {
  background: #fff;
  border-bottom: 1px solid #e5e7eb;
  padding: 0.75rem 1rem;
  position: sticky;
  top: 0;
  z-index: 50;
}

.header-container {
  max-width: 1440px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.logo {
  height: 40px;
  width: auto;
}

.menu-button {
  display: none;
  align-items: center;
  gap: 0.5rem;
  background: none;
  border: none;
  cursor: pointer;
  color: #374151;
  font-size: 0.875rem;
}

.nav-section {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #374151;
  text-decoration: none;
  font-size: 0.875rem;
  transition: color 0.2s;
}

.nav-link:hover {
  color: #1f2937;
}

.actions-section {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.icon-button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  color: #374151;
  transition: color 0.2s;
}

.icon-button:hover {
  color: #1f2937;
}

.text-button {
  color: #374151;
  text-decoration: none;
  font-size: 0.875rem;
  padding: 0.5rem 1rem;
  transition: color 0.2s;
}

.text-button:hover {
  color: #1f2937;
}

.primary-button {
  background: #dc2626;
  color: white;
  text-decoration: none;
  font-size: 0.875rem;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: background-color 0.2s;
}

.primary-button:hover {
  background: #b91c1c;
}

.icon {
  width: 1.25rem;
  height: 1.25rem;
}

@media (max-width: 1024px) {
  .menu-button {
    display: flex;
  }

  .nav-section {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    padding: 1rem;
    flex-direction: column;
    align-items: flex-start;
    border-bottom: 1px solid #e5e7eb;
  }

  .nav-section.nav-active {
    display: flex;
  }

  .actions-section {
    gap: 0.5rem;
  }

  .text-button {
    display: none;
  }

  .primary-button {
    display: none;
  }
}

@media (max-width: 640px) {
  .header-container {
    gap: 1rem;
  }

  .logo {
    height: 32px;
  }
}
</style>