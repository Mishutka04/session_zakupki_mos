<template>
  <div class="basic-info-container">
    <div class="basic-info">
      <!-- Session Header -->
      <div class="session-header">
        <div class="session-header-content">
          <div class="session-title-container">
            <h2 class="session-title">
              Котировочная сессия {{ response.session_info.id }}
            </h2>
            <span
              :class="{ 'active-of-card': response.session_info.state === 'Активная', 'take-of-card': response.session_info.state === 'СНЯТА С ПУБЛИКАЦИИ', 'finished': response.session_info.state === 'ПРОВЕДЕНО' }">
              <b>{{ response.session_info.state }}</b>
            </span>
          </div>
          <h3 class="session-name">{{ response.session_info.name }}</h3>
        </div>
      </div>
      <div class="info-item">
        <h4 class="info-label">Заказчик</h4>
        <p class="info-value"><b>{{ response.session_info.customer }}</b></p>
      </div>
      <div class="info-item">
        <h4 class="info-label">Начальная цена</h4>
        <p class="info-value"><b>{{ response.session_info.startCost }} ₽</b></p>
      </div>
      <div class="info-item">
        <h4 class="info-label">Условия исполнения контракта</h4>
        <p class="info-value"><b>{{ response.session_info.termsContract }}</b></p>
      </div>
      <div class="info-item">
        <h4 class="info-label">Обеспечение исполнения контракта</h4>
        <p class="info-value" v-if="response.session_info.contractGuaranteeAmount == 0"><b>Не требуется</b></p>
        <p v-else><b>{{ response.session_info.contractGuaranteeAmount }}</b></p>
      </div>
      <div class="info-item">
        <h4 class="info-label">Заключение происходит в соответствии с законом</h4>
        <p><b>{{ response.session_info.federalLawName }}</b></p>
      </div>
      <div class="info-item">
        <h4 class="info-label">Даты проведения</h4>
        <p class="info-value"><b>С {{ response.session_info.startDate }} по {{ response.session_info.endDate }}</b></p>
      </div>
      <div class="info-item">
        <h4 class="info-label">Наличие лицензии</h4>
        <p class="info-value"><b>{{ response.session_info.uploadLicenseDocumentsComment }}</b></p>
      </div>
    </div>

    <div class="violations-block">
      <div class="violations-header">
        <h2>Краткий отчет по карточке</h2>
      </div>

      <div class="violations-summary">
        <h4>Нарушения по КС</h4>
        <ul class="violations-list" v-for="(answer, index) in response.answers" :key="index">
          <h5>Файл № {{ index + 1 }}</h5>
          <li v-for="(answer_data, dataIndex) in answer" :key="dataIndex">
            {{ answer_data.violation_type }}
            <span :class="['violation-level', violationLevelClass(answer_data.severity)]">
              {{ answer_data.severity }}
            </span>
          </li>
        </ul>
      </div>

      <div class="price-info">
        <h4>Рекомендации</h4>
        <div class="status-card" v-if="recommendationType === 'attention'">
          <div class="icon-wrapper">
            <div class="icon attention">
              <Camera class="icon-svg" />
            </div>
          </div>
          <h2 class="title">Обратить внимание на нарушения</h2>
          <p class="message">
            Выявлены незначительные нарушения в котировочной сессии
          </p>
        </div>
        <div class="status-card" v-else-if="recommendationType === 'remove'">
          <div class="icon-wrapper">
            <div class="icon remove">
              <BanIcon class="icon-svg" />
            </div>
          </div>
          <h2 class="title">Снять с площадки</h2>
          <p class="message">
            Обнаружены серьезные нарушения в котировочной сессии
          </p>
        </div>
        <div class="status-card" v-else>
          <div class="icon-wrapper">
            <div class="icon no-violations">
              <CheckCircleIcon class="icon-svg" />
            </div>
          </div>
          <h2 class="title">Нарушений нет</h2>
          <p class="message">
            Котировочная сессия соответствует всем требованиям
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { Camera, BanIcon, CheckCircleIcon } from 'lucide-vue-next'

const props = defineProps({
  response: {
    type: Object,
    required: true
  },
})

const currentDate = computed(() => {
  const now = new Date()
  return now.toLocaleString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  })
})

const violationLevelClass = (level) => {
  switch (level) {
    case 'Высокая': return 'severity-badge critical'
    case 'Средняя': return 'severity-badge high'
    case 'Низкая': return 'severity-badge low'
    default: return ''
  }
}

const recommendationType = computed(() => {
  const violations = []
  props.response.answers.forEach(answer => {
    answer.forEach(answer_data => {
      violations.push(answer_data.severity)
    })
  })

  if (violations.includes('Высокая')) {
    return 'remove'
  } else if (violations.includes('Средняя')) {
    return 'attention'
  } else if (violations.includes('Низкая')) {
    return 'attention'
  } else {
    return 'no-violations'
  }
})
</script>

<style>
.severity-badge {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
}
.critical {
  background-color: #e74c3c;
  color: #fff;
}
.high {
  background-color: #e67e22;
  color: #fff;
}

.medium {
  background-color: #f1c40f;
  color: #333;
}

.low {
  background-color: #2ecc71;
  color: #fff;
}

.basic-info-container {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
}

.basic-info {
  flex: 1;
  min-width: 300px;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  padding: 1.5rem;
  background-color: #fff;
  border-radius: 0.5rem;
  box-shadow: 0 1px 30px rgba(0, 0, 0, 0.2);
  margin-bottom: 2rem;
}

.session-header {
  margin-bottom: 1rem;
}

.session-title-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.session-title {
  font-size: 1.5rem;
  margin: 0;
}

.session-name {
  font-size: 1.25rem;
  margin: 0.5rem 0 0 0;
}

.take-of-card {
  color: #db2b21;
}

.finished {
  color: #7f8792;
}

.active-of-card {
  color: #0d9b68;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.info-label {
  color: #6B7280;
  font-size: 0.875rem;
  font-weight: 500;
  margin: 0;
}

.info-value {
  color: #111827;
  font-size: 1rem;
  font-weight: 400;
  margin: 0;
  line-height: 1.5;
}

.violations-block {
  width: 100%;
  max-width: 400px;
  background-color: #fff;
  border-radius: 0.5rem;
  box-shadow: 0 1px 30px rgba(0, 0, 0, 0.2);
  padding: 1.5rem;
  display: inline-block;
  height: fit-content;
  max-height: 80vh;
  overflow-y: auto;
}

.violations-header {
  margin-bottom: 1.5rem;
  text-align: center;
}

.violations-header h2 {
  color: #333;
  font-size: 1.25rem;
  margin: 0;
}
h5 {
  color: #333;
  font-size: 1rem;
  margin: 0;
  margin-top: 2rem;
  text-align: center;
}

.violations-summary {
  margin-bottom: 2rem;
}

.violations-summary h4 {
  font-size: 1rem;
  margin: 0 0 1rem 0;
  color: #333;
  text-align: center;
}

.violations-list {
  list-style: none;
  padding: 0;
  margin: 0;
  
}

.violations-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
  font-size: 0.9rem;
}
.violations-list li span{
  margin-left: 10px;
}
.violation-level {
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.8rem;
  font-weight: 500;
}

.level-high {
  border: 2px solid #DC2626;
  color: #DC2626;
}

.level-medium {
  border: 2px solid #D97706;
  color: #D97706;
}

.level-low {
  border: 2px solid #059669;
  color: #059669;
}

.price-info {
  border-top: 1px solid #eee;
  padding-top: 1.5rem;
}

.price-info h4 {
  font-size: 1rem;
  margin: 0 0 1rem 0;
  color: #333;
  text-align: center;
}

.status-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  margin-bottom: 1rem;
  text-align: center;
}

.icon-wrapper {
  margin-bottom: 1rem;
}

.icon {
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-svg {
  width: 32px;
  height: 32px;
}

.attention {
  background-color: #FEF3C7;
}

.attention .icon-svg {
  color: #D97706;
  margin: 20px;
}

.remove {
  background-color: #FEE2E2;
}

.remove .icon-svg {
  color: #DC2626;
}

.no-violations {
  background-color: #D1FAE5;
}

.no-violations .icon-svg {
  color: #059669;
  margin: 10px;
}

.title {
  font-size: 1.25rem;
  color: #1A1D1F;
  margin: 0 0 0.5rem 0;
  font-weight: 600;
}

.message {
  color: #6F767E;
  font-size: 0.875rem;
  margin: 0;
  line-height: 1.5;
}

.price-label {
  color: #6F767E;
  font-size: 0.875rem;
  margin: 0 0 0.25rem 0;
}

.price-value {
  color: #1A1D1F;
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0;
}

@media (max-width: 768px) {
  .basic-info-container {
    flex-direction: column;
  }

  .violations-block {
    max-width: 100%;
    margin-bottom: 20px;
  }
}
</style>