<template>
    <div class="tender-container">
      <header class="tender-header">
        <div class="tender-session">
          <h2>Котировочная сессия {{ sessionId }}</h2>
          <span class="status-badge">АКТИВНАЯ</span>
        </div>
      </header>
  
      <main class="tender-content">
        <div class="tender-main">
          <div class="tender-title">
            <h1>ОБЕСПЕЧЕНИЕ ГРЯЗЕЗАЩИТНЫМИ КОВРИКАМИ</h1>
          </div>
  
          <section class="tender-details">
            <div class="detail-group">
              <h3>Условия исполнения контракта</h3>
              <div class="detail-item">
                <div class="icon-text">
                  <span class="icon">📄</span>
                  Обязательное электронное исполнение с использованием УПД
                </div>
              </div>
            </div>
  
            <div class="detail-group">
              <h3>Обеспечение исполнения контракта</h3>
              <p>Не требуется</p>
            </div>
  
            <div class="detail-group">
              <h3>Заказчик</h3>
              <p>Государственное бюджетное учреждение здравоохранения города Москвы «Детская стоматологическая поликлиника № 46 Департамента здравоохранения города Москвы»</p>
            </div>
  
            <div class="detail-group">
              <h3>Заключение происходит в соответствии с законом</h3>
              <div class="icon-text">
                <span class="icon">📋</span>
                44-ФЗ
              </div>
            </div>
  
            <div class="detail-group">
              <h3>Даты проведения</h3>
              <p>с {{ startDate }} по {{ endDate }}</p>
            </div>
          </section>
  
          <button class="import-pdf-btn" @click="importPDF">Импортировать PDF</button>
        </div>
  
        <aside class="tender-sidebar">
          <div class="sidebar-content">
            <div class="processing-notice">
              <p>Идет обработка ставок. Возможна переторжка.</p>
              <div class="current-time">{{ currentDateTime }}</div>
            </div>
  
            <div class="auth-notice">
              <p>
                Для участия в котировочной сессии
                <br>необходимо авторизоваться
              </p>
            </div>
  
            <div class="price-section">
              <h3>Начальная цена</h3>
              <div class="price">{{ formatPrice(initialPrice) }} ₽</div>
            </div>
          </div>
        </aside>
      </main>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const sessionId = '9867491'
  const startDate = '05.11.2024 20:36:02'
  const endDate = '06.11.2024 20:36:02'
  const initialPrice = 19507.50
  const currentDateTime = ref('06 ноября 2024 20:36:02')
  
  const formatPrice = (price) => {
    return new Intl.NumberFormat('ru-RU').format(price)
  }
  
  const importPDF = () => {
    console.log('Importing PDF...')
    // Add PDF import logic here
  }
  </script>
  
  <style scoped>
  .tender-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Arial', sans-serif;
    color: #333;
    background-color: #f7f7f7;
  }
  
  .tender-header {
    margin-bottom: 30px;
  }
  
  .tender-session {
    display: flex;
    align-items: center;
    gap: 15px;
  }
  
  .tender-session h2 {
    margin: 0;
    font-size: 18px;
    font-weight: 500;
  }
  
  .status-badge {
    background-color: #4CAF50;
    color: white;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 500;
  }
  
  .tender-content {
    display: flex;
    gap: 30px;
  }
  
  .tender-main {
    flex: 1;
    background-color: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .tender-title h1 {
    color: #1a3d88;
    font-size: 24px;
    margin: 0 0 30px 0;
    font-weight: 600;
  }
  
  .detail-group {
    margin-bottom: 25px;
  }
  
  .detail-group h3 {
    color: #666;
    font-size: 16px;
    margin: 0 0 10px 0;
    font-weight: 500;
  }
  
  .icon-text {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  .icon {
    font-size: 20px;
  }
  
  .tender-sidebar {
    width: 300px;
    flex-shrink: 0;
  }
  
  .sidebar-content {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .processing-notice {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .current-time {
    color: #1a3d88;
    font-size: 24px;
    font-weight: bold;
    margin-top: 10px;
  }
  
  .auth-notice {
    background-color: #e9ecef;
    padding: 15px;
    text-align: center;
    border-radius: 6px;
    margin-bottom: 20px;
  }
  
  .price-section {
    text-align: center;
  }
  
  .price-section h3 {
    color: #333;
    margin-bottom: 10px;
    font-weight: 500;
  }
  
  .price {
    color: #1a3d88;
    font-size: 32px;
    font-weight: bold;
  }
  
  .import-pdf-btn {
    background-color: #1a3d88;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s;
    margin-top: 20px;
  }
  
  .import-pdf-btn:hover {
    background-color: #152f66;
  }
  
  @media (max-width: 1024px) {
    .tender-content {
      flex-direction: column;
    }
  
    .tender-sidebar {
      width: 100%;
    }
  }
  
  @media (max-width: 768px) {
    .tender-session {
      flex-direction: column;
      align-items: flex-start;
      gap: 10px;
    }
  
    .tender-title h1 {
      font-size: 20px;
    }
  
    .price {
      font-size: 24px;
    }
  
    .current-time {
      font-size: 20px;
    }
  }
  
  @media (max-width: 480px) {
    .tender-container {
      padding: 10px;
    }
  
    .tender-main, .sidebar-content {
      padding: 15px;
    }
  
    .tender-title h1 {
      font-size: 18px;
    }
  
    .status-badge {
      font-size: 12px;
    }
  
    .detail-group h3 {
      font-size: 14px;
    }
  }
  </style>