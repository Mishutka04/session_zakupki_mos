<template>
    <div class="procurement-portal">
      <div class="tabs-container">
        <div class="tabs-header">
          <button 
            v-for="tab in tabs" 
            :key="tab.id"
            @click="activeTab = tab.id"
            :class="['tab-button', { active: activeTab === tab.id }]"
          >
            {{ tab.name }} {{ tab.count }}
          </button>
        </div>
  
        <!-- Specifications Tab -->
        <div v-if="activeTab === 'specifications'" class="tab-content">
          <div class="specification-card">
            <div class="card-image">
              <img src="" alt="" class="placeholder-image" />
            </div>
            <div class="card-content">
              <h3 class="service-name">{{ specification.name }}</h3>
              <div class="service-details">
                <div class="detail-item">
                  <span class="detail-label">Количество</span>
                  <span class="detail-value">{{ specification.quantity }} шт</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Цена за ед.</span>
                  <span class="detail-value">{{ specification.pricePerUnit }} ₽</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Общая стоимость</span>
                  <span class="detail-value total">{{ specification.totalPrice }} ₽</span>
                </div>
              </div>
              <button @click="toggleDetails" class="show-details-btn">
                {{ showDetails ? 'Скрыть' : 'Показать' }} подробную информацию
                <span class="arrow" :class="{ 'arrow-down': showDetails }">▼</span>
              </button>
            </div>
          </div>
          <div v-if="showDetails" class="error-section">
            <div v-for="error in specification.errors" :key="error.id" class="error-item">
              <button 
                @click="toggleError(error.id)"
                class="error-header"
                :class="error.severity"
              >
                <span class="error-title">{{ error.title }}</span>
                <span class="error-severity">{{ getSeverityText(error.severity) }}</span>
                <span class="arrow" :class="{ 'arrow-down': expandedErrors.includes(error.id) }">▼</span>
              </button>
              <div v-if="expandedErrors.includes(error.id)" class="error-description">
                {{ error.description }}
              </div>
            </div>
          </div>
        </div>
  
        <!-- Delivery Schedule Tab -->
        <div v-if="activeTab === 'schedule'" class="tab-content">
          <div class="delivery-stage">
            <div class="stage-header">
              <div class="stage-number">1</div>
              <h3 class="stage-title">Этап поставки</h3>
              <div class="stage-price">{{ specification.totalPrice }} ₽</div>
            </div>
  
            <div class="stage-details">
              <div class="address">
                <i class="icon-location"></i>
                {{ delivery.address }}
              </div>
              <div class="date">
                <i class="icon-calendar"></i>
                {{ delivery.dates }}
              </div>
            </div>
  
            <div class="specification-details">
              <button @click="toggleSpecification" class="specification-toggle">
                Спецификация
                <span class="arrow" :class="{ 'arrow-down': showSpecification }">▼</span>
              </button>
  
              <div v-if="showSpecification" class="specification-table">
                <table>
                  <thead>
                    <tr>
                      <th>Заказчик</th>
                      <th>Наименование</th>
                      <th>Цена за единицу</th>
                      <th>Кол-во</th>
                      <th>Сумма</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>{{ customer }}</td>
                      <td>{{ specification.name }}</td>
                      <td>{{ specification.pricePerUnit }} ₽</td>
                      <td>{{ specification.quantity }}</td>
                      <td>{{ specification.totalPrice }} ₽</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
  
            <div class="error-section">
              <div v-for="error in delivery.errors" :key="error.id" class="error-item">
                <button 
                  @click="toggleError(error.id)"
                  class="error-header"
                  :class="error.severity"
                >
                  <span class="error-title">{{ error.title }}</span>
                  <span class="error-severity">{{ getSeverityText(error.severity) }}</span>
                  <span class="arrow" :class="{ 'arrow-down': expandedErrors.includes(error.id) }">▼</span>
                </button>
                <div v-if="expandedErrors.includes(error.id)" class="error-description">
                  {{ error.description }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const activeTab = ref('specifications')
  const showDetails = ref(false)
  const showSpecification = ref(false)
  const expandedErrors = ref([])
  
  const specification = {
    name: 'Услуга по обеспечению грязезащитными ковриками',
    quantity: 51,
    pricePerUnit: '382,5',
    totalPrice: '19 507,5',
    errors: [
      { id: 1, severity: 'high', title: 'Несоответствие размеров', description: 'Указанные размеры ковриков не соответствуют требованиям заказчика' },
      { id: 2, severity: 'medium', title: 'Отсутствует сертификат', description: 'Необходимо приложить сертификат соответствия на материалы' },
      { id: 3, severity: 'low', title: 'Уточнение цвета', description: 'Требуется уточнение цветовой гаммы ковриков' }
    ]
  }
  
  const customer = 'Государственное бюджетное учреждение здравоохранения города Москвы «Детская стоматологическая поликлиника № 46 Департамента здравоохранения города Москвы»'
  
  const delivery = {
    address: 'г.г Москва, 111399, г. Москва, ул. Новогиреевская, д.17',
    dates: '11.11.2024 - 31.12.2024',
    errors: [
      { id: 4, severity: 'medium', title: 'Уточнение времени доставки', description: 'Необходимо согласовать точное время доставки в указанный период' },
      { id: 5, severity: 'low', title: 'Дополнительная информация', description: 'Требуется указать контактное лицо для приема товара' }
    ]
  }
  
  const tabs = [
    { id: 'specifications', name: 'СПЕЦИФИКАЦИИ', count: '1' },
    { id: 'schedule', name: 'ГРАФИК ПОСТАВКИ', count: '1' }
  ]
  
  const toggleDetails = () => {
    showDetails.value = !showDetails.value
  }
  
  const toggleSpecification = () => {
    showSpecification.value = !showSpecification.value
  }
  
  const toggleError = (errorId) => {
    const index = expandedErrors.value.indexOf(errorId)
    if (index === -1) {
      expandedErrors.value.push(errorId)
    } else {
      expandedErrors.value.splice(index, 1)
    }
  }
  
  const getSeverityText = (severity) => {
    const severityTexts = {
      high: 'Высокая',
      medium: 'Средняя',
      low: 'Низкая'
    }
    return severityTexts[severity] || 'Неизвестно'
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
    color: #333;
    background-color: #f5f5f5;
  }
  
  .procurement-portal {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  /* Tabs Styles */
  .tabs-container {
    background-color: #fff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  }
  
  .tabs-header {
    display: flex;
    background-color: #f8fafc;
    border-bottom: 1px solid #e2e8f0;
  }
  
  .tab-button {
    padding: 1rem 2rem;
    border: none;
    background: none;
    cursor: pointer;
    color: #64748b;
    font-weight: 500;
    position: relative;
  }
  
  .tab-button.active {
    color: #1e40af;
  }
  
  .tab-button.active::after {
    content: '';
    position: absolute;
    bottom: -1px;
    left: 0;
    right: 0;
    height: 2px;
    background-color: #1e40af;
  }
  
  /* Specification Card Styles */
  .specification-card {
    display: flex;
    padding: 1.5rem;
    border-bottom: 1px solid #e2e8f0;
  }
  
  .card-image {
    flex-shrink: 0;
    margin-right: 1.5rem;
  }
  
  .placeholder-image {
    width: 100px;
    height: 100px;
    background-color: #f8fafc;
    border-radius: 4px;
  }
  
  .card-content {
    flex-grow: 1;
  }
  
  .service-name {
    font-size: 1.125rem;
    color: #1e40af;
    margin-bottom: 1rem;
  }
  
  .service-details {
    display: flex;
    gap: 2rem;
    margin-bottom: 1rem;
  }
  
  .detail-item {
    display: flex;
    flex-direction: column;
  }
  
  .detail-label {
    color: #64748b;
    font-size: 0.875rem;
    margin-bottom: 0.25rem;
  }
  
  .detail-value {
    font-weight: 500;
  }
  
  .detail-value.total {
    color: #1e40af;
    font-weight: 600;
  }
  
  .show-details-btn {
    color: #1e40af;
    background: none;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.875rem;
  }
  
  /* Delivery Stage Styles */
  .delivery-stage {
    padding: 1.5rem;
  }
  
  .stage-header {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
  }
  
  .stage-number {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    border: 2px solid #1e40af;
    color: #1e40af;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    margin-right: 1rem;
  }
  
  .stage-title {
    flex-grow: 1;
    font-size: 1.125rem;
    font-weight: 500;
  }
  
  .stage-price {
    font-weight: 600;
    color: #1e40af;
  }
  
  .stage-details {
    display: flex;
    gap: 2rem;
    margin-bottom: 1rem;
  }
  
  .address, .date {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: #64748b;
  }
  
  .icon-location, .icon-calendar {
    width: 20px;
    height: 20px;
    background-size: contain;
  }
  
  .icon-location {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='currentColor'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z'/%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M15 11a3 3 0 11-6 0 3 3 0 016 0z'/%3E%3C/svg%3E");
  }
  
  .icon-calendar {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='currentColor'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z'/%3E%3C/svg%3E");
  }
  
  .specification-toggle {
    width: 100%;
    padding: 0.75rem;
    background-color: #f8fafc;
    border: none;
    border-radius: 4px;
    text-align: left;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }
  
  .arrow {
    font-size: 0.75rem;
    transition: transform 0.2s;
  }
  
  .arrow-down {
    transform: rotate(180deg);
  }
  
  .specification-table {
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    overflow-x: auto;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    padding: 0.75rem;
    text-align: left;
    border-bottom: 1px solid #e2e8f0;
  }
  
  th {
    background-color: #f8fafc;
    font-weight: 500;
    color: #64748b;
  }
  
  td {
    color: #1e293b;
  }
  
  /* Error Styles */
  .error-section {
    margin-top: 1rem;
  }
  
  .error-item {
    margin-bottom: 0.5rem;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    overflow: hidden;
  }
  
  .error-header {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.75rem 1rem;
    background: none;
    border: none;
    cursor: pointer;
    text-align: left;
  }
  
  .error-header.high {
    background-color: #fee2e2;
    color: #991b1b;
  }
  
  .error-header.medium {
    background-color: #fef3c7;
    color: #92400e;
  }
  
  .error-header.low {
    background-color: #e0f2fe;
    color: #0369a1;
  }
  
  .error-title {
    font-weight: 500;
  }
  
  .error-severity {
    font-size: 0.875rem;
    padding: 0.25rem 0.5rem;
    border-radius: 9999px;
    background-color: rgba(255, 255, 255, 0.5);
  }
  
  .error-description {
    padding: 0.75rem 1rem;
    background-color: #fff;
    border-top: 1px solid #e2e8f0;
    font-size: 0.875rem;
    color: #4b5563;
  }
  
  /* Responsive Styles */
  @media (max-width: 768px) {
    .service-details {
      flex-direction: column;
      gap: 1rem;
    }
  
    .stage-details {
      flex-direction: column;
      gap: 1rem;
    }
  
    .specification-table {
      font-size: 0.875rem;
    }
  
    .tabs-header {
      flex-wrap: wrap;
    }
  
    .tab-button {
      flex-grow: 1;
      text-align: center;
    }
  }
  </style>