<template>
  <div class="procurement-portal">
    <!-- Header section remains the same -->

    <main class="main-content">
      <div class="container">
        <div class="session-header">
          <a href="#" class="back-link">← Вернуться в реестр котировочных сессий</a>
          <div class="session-info">
            <h1>Котировочная сессия {{ sessionId }}</h1>
            <span class="status-badge active">АКТИВНАЯ</span>
          </div>
        </div>

        <div class="procurement-title">
          <h2>{{ title }}</h2>
        </div>

        <div class="main-grid">
          <!-- Left Content -->
          <div class="content-section">
            <!-- Contract Details Card -->
            <div class="card">
              <div class="card-section">
                <h3>Условия исполнения контракта</h3>
                <div class="contract-requirement">
                  <i class="icon-document"></i>
                  <span>{{ contractTerms }}</span>
                </div>
              </div>

              <div class="card-section">
                <h3>Обеспечение исполнения контракта</h3>
                <p>{{ securityRequirement }}</p>
              </div>

              <div class="card-section">
                <h3>Заказчик</h3>
                <p>{{ customer }}</p>
              </div>

              <div class="card-section">
                <h3>Заключение происходит в соответствии с законом</h3>
                <p class="law-reference">{{ lawReference }}</p>
              </div>

              <div class="card-section">
                <h3>Даты проведения</h3>
                <div class="date-range">
                  <div class="date-item">
                    <span class="date-label">с</span>
                    <span class="date-value">{{ startDate }}</span>
                  </div>
                  <div class="date-item">
                    <span class="date-label">по</span>
                    <span class="date-value">{{ endDate }}</span>
                  </div>
                </div>
              </div>

              <div class="card-section">
                <h3>Документы</h3>
                <div class="documents-list">
                  <button class="download-all-btn" @click="downloadAll">
                    <i class="icon-download"></i>
                    Скачать все
                  </button>
                  <div class="document-item" v-for="doc in documents" :key="doc.id">
                    <i :class="getDocumentIcon(doc.type)"></i>
                    <span class="document-name">{{ doc.name }}</span>
                    <button class="download-btn" @click="downloadDocument(doc)">
                      <i class="icon-download-single"></i>
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- Tabs Section -->
            <ProductDetail />
          </div>

          <!-- Right Sidebar -->
          <div class="sidebar-section">
            <div class="card timer-card">
              <h3>До окончания сессии осталось:</h3>
              <div class="timer-grid">
                <div v-for="(value, unit) in timeRemaining" :key="unit" class="timer-item">
                  <span class="timer-value">{{ value }}</span>
                  <span class="timer-unit">{{ unit }}</span>
                </div>
              </div>
              <div class="price-section">
                <span class="price-label">Начальная цена</span>
                <span class="price-value">{{ formatPrice(initialPrice) }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import ProductDetail from './ProductDetail.vue';
const sessionId = '9867491'
const title = 'ОБЕСПЕЧЕНИЕ ГРЯЗЕЗАЩИТНЫМИ КОВРИКАМИ'
const contractTerms = 'Обязательное электронное исполнение с использованием УПД'
const securityRequirement = 'Не требуется'
const customer = 'Государственное бюджетное учреждение здравоохранения города Москвы «Детская стоматологическая поликлиника № 46 Департамента здравоохранения города Москвы»'
const lawReference = '44-ФЗ'
const startDate = '05.11.2024 20:36:02'
const endDate = '06.11.2024 20:36:02'
const initialPrice = 19507.50
const activeTab = ref('specifications')
const expandedErrors = ref([])

const documents = [
  {
    id: 1,
    name: 'Проект контракта.pdf',
    type: 'pdf'
  },
  {
    id: 2,
    name: 'ТЗ_грязевые коврики.docx',
    type: 'word'
  }
]

const specifications = [
  {
    id: 1,
    name: 'Услуга по обеспечению грязезащитными ковриками',
    quantity: 51,
    unitPrice: 382.5,
    total: 19507.5,
    errors: [
      {
        id: 'spec1-error1',
        severity: 'high',
        title: 'Несоответствие размеров',
        description: 'Указанные размеры ковриков не соответствуют требованиям технического задания'
      },
      {
        id: 'spec1-error2',
        severity: 'medium',
        title: 'Отсутствует сертификат',
        description: 'Необходимо предоставить сертификат соответствия на материалы'
      }
    ]
  }
]

const deliverySchedule = [
  {
    id: 1,
    stage: 'Этап поставки',
    address: 'г.г Москва, 111399, г. Москва, ул. Новогиреевская, д.17',
    date: '11.11.2024 - 31.12.2024',
    errors: [
      {
        id: 'schedule1-error1',
        severity: 'low',
        title: 'Уточнение времени доставки',
        description: 'Необходимо согласовать точное время доставки в указанный период'
      }
    ]
  }
]

const timeRemaining = ref({
  'Дней': '00',
  'Часов': '14',
  'Минут': '07',
  'Секунд': '08'
})

const tabs = [
  {
    id: 'specifications',
    name: 'СПЕЦИФИКАЦИИ',
    items: specifications
  },
  {
    id: 'schedule',
    name: 'ГРАФИК ПОСТАВКИ',
    items: deliverySchedule
  }
]

// Methods
const setActiveTab = (tabId) => {
  activeTab.value = tabId
}

const toggleError = (errorId) => {
  const index = expandedErrors.value.indexOf(errorId)
  if (index === -1) {
    expandedErrors.value.push(errorId)
  } else {
    expandedErrors.value.splice(index, 1)
  }
}

const getDocumentIcon = (type) => {
  const icons = {
    pdf: 'icon-pdf',
    word: 'icon-word'
  }
  return icons[type] || 'icon-file'
}

const downloadDocument = (doc) => {
  console.log('Downloading document:', doc.name)
}

const downloadAll = () => {
  console.log('Downloading all documents')
}

const formatPrice = (price) => {
  return new Intl.NumberFormat('ru-RU', {
    style: 'currency',
    currency: 'RUB',
    minimumFractionDigits: 2
  }).format(price)
}
</script>

<style>
/* Reset and Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  background-color: #f5f7fa;
  color: #333;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Session Header Styles */
.session-header {
  margin-bottom: 2rem;
}

.back-link {
  color: #666;
  text-decoration: none;
  display: inline-block;
  margin-bottom: 1rem;
}

.session-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.status-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
  font-weight: 500;
}

.status-badge.active {
  background-color: #e6f4ea;
  color: #1e7e34;
}

/* Main Grid Layout */
.main-grid {
  display: grid;
  grid-template-columns: 3fr 1fr;
  gap: 2rem;
}

/* Card Styles */
.card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  margin-bottom: 1.5rem;
}

.card-section {
  padding: 1.5rem;
  border-bottom: 1px solid #eee;
}

.card-section:last-child {
  border-bottom: none;
}

.card-section h3 {
  font-size: 1rem;
  color: #666;
  margin-bottom: 0.75rem;
}

/* Documents List Styles */
.documents-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.download-all-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #0066cc;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  font-weight: 500;
}

.document-item {
  display: flex;
  align-items: center;
  padding: 0.75rem;
  background: #f8f9fa;
  border-radius: 4px;
}

.document-name {
  flex: 1;
  margin: 0 0.75rem;
}

/* Tabs Styles */
.tabs-section {
  background: white;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.tabs-header {
  display: flex;
  border-bottom: 1px solid #eee;
}

.tab-btn {
  padding: 1rem 1.5rem;
  border: none;
  background: none;
  font-weight: 500;
  color: #666;
  cursor: pointer;
  position: relative;
}

.tab-btn.active {
  color: #0066cc;
}

.tab-btn.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 2px;
  background: #0066cc;
}

.tab-counter {
  margin-left: 0.5rem;
  padding: 0.125rem 0.5rem;
  background: #f0f0f0;
  border-radius: 1rem;
  font-size: 0.875rem;
}

/* Error Styles */
.error-section {
  margin-top: 1rem;
}

.error-item {
  margin-bottom: 0.5rem;
}

.error-header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  text-align: left;
}

.error-header.high {
  background-color: #fff5f5;
  color: #c53030;
}

.error-header.medium {
  background-color: #fffff0;
  color: #975a16;
}

.error-header.low {
  background-color: #fffaf0;
  color: #9c4221;
}

.error-content {
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 0 0 4px 4px;
  margin-top: 1px;
}

.icon-chevron {
  transition: transform 0.2s;
}

.icon-chevron.rotated {
  transform: rotate(180deg);
}

/* Timer Card Styles */
.timer-card {
  padding: 1.5rem;
}

.timer-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.5rem;
  margin: 1rem 0;
}

.timer-item {
  background: #f8f9fa;
  padding: 0.75rem;
  border-radius: 4px;
  text-align: center;
}

.timer-value {
  display: block;
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
}

.timer-unit {
  display: block;
  font-size: 0.75rem;
  color: #666;
  margin-top: 0.25rem;
}

.price-section {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid #eee;
}

.price-label {
  display: block;
  color: #666;
  margin-bottom: 0.5rem;
}

.price-value {
  display: block;
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
}

/* Responsive Styles */
@media (max-width: 1024px) {
  .main-grid {
    grid-template-columns: 1fr;
  }

  .timer-card {
    position: sticky;
    top: 1rem;
  }
}

@media (max-width: 768px) {
  .session-info {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }

  .timer-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .tabs-header {
    overflow-x: auto;
    white-space: nowrap;
  }
}

/* Icons */
[class^="icon-"] {
  display: inline-block;
  width: 24px;
  height: 24px;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}

.icon-document {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='currentColor'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z' /%3E%3C/svg%3E");
}

.icon-download {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='currentColor'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4' /%3E%3C/svg%3E");
}

.icon-chevron {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='currentColor'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M19 9l-7 7-7-7' /%3E%3C/svg%3E");
}

.icon-location {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='currentColor'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z' /%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M15 11a3 3 0 11-6 0 3 3 0 016 0z' /%3E%3C/svg%3E");
}

.icon-calendar {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='currentColor'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z' /%3E%3C/svg%3E");
}
</style>