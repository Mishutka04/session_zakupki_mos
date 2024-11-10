<template>
  <footer class="footer">
    <div class="footer-top">
      <nav class="footer-nav">
        <ul class="nav-list">
          <li><a href="#" class="nav-link">О портале</a></li>
          <li><a href="#" class="nav-link">Контакты</a></li>
          <li><a href="#" class="nav-link">Новости</a></li>
          <li><a href="#" class="nav-link">Центр поддержки</a></li>
          <li><a href="#" class="nav-link">Карта сайта</a></li>
        </ul>
        <a href="#" class="accessibility-link">
          <EyeIcon class="icon" />
          Версия для слабовидящих
        </a>
      </nav>
    </div>

    <div class="footer-content">
      <div class="logos">
        <img src="../assets/msk.png" alt="Департамент города Москвы" class="logo" />
        <img src="../assets/ii.png" alt="Департамент информационных технологий" class="logo" />
      </div>
      
      <div class="footer-bottom">
        <div class="copyright">
          © 2017-2024 v.20241031
        </div>
        <a href="#" class="telegram-link">
          <SendIcon class="icon" />
          Наш телеграм-канал
        </a>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { EyeIcon, SendIcon } from 'lucide-vue-next'
</script>

<style scoped>
.footer {
  padding: 2rem 4rem;
  background-color: #fff;
  font-family: system-ui, -apple-system, sans-serif;
}

.footer-top {
  margin-bottom: 2rem;
  border-bottom: 1px solid #eaeaea;
  padding-bottom: 1rem;
}

.footer-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-list {
  display: flex;
  gap: 2rem;
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-link {
  color: #4B75B9;
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.2s ease;
}

.nav-link:hover {
  color: #2c4b8b;
}

.accessibility-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #4B75B9;
  text-decoration: none;
  font-size: 0.9rem;
}

.accessibility-link:hover {
  color: #2c4b8b;
}

.footer-content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.logos {
  display: flex;
  gap: 4rem;
  align-items: center;
}

.logo {
  height: 40px;
  width: auto;
}

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 1rem;
  border-top: 1px solid #eaeaea;
}

.copyright {
  color: #666;
  font-size: 0.9rem;
}

.telegram-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #4B75B9;
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.2s ease;
}

.telegram-link:hover {
  color: #2c4b8b;
}

.icon {
  width: 1.2rem;
  height: 1.2rem;
}

@media (max-width: 768px) {
  .footer {
    padding: 1.5rem;
  }

  .footer-nav {
    flex-direction: column;
    gap: 1rem;
  }

  .nav-list {
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }

  .logos {
    flex-direction: column;
    align-items: flex-start;
    gap: 2rem;
  }

  .footer-bottom {
    flex-direction: column;
    gap: 1rem;
    align-items: flex-start;
  }
}
</style>