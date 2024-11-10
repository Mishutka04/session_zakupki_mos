<template>
  <div class="analysis-results">
    <h2 class="section-title">Результаты анализа</h2>
    <div v-for="(answerItem, fileIndex) in response.answers" :key="fileIndex" class="file-group">
      <h3 class="file-title">Отчет по файлу № {{ fileIndex + 1 }}</h3>
      <div class="results-table">
        <div class="table-header">
          <div class="header-cell">Тип нарушения</div>
          <div class="header-cell">Серьезность</div>
          <div class="header-cell">Описание</div>
          <div class="header-cell">Рекомендации</div>
        </div>
        <div v-for="(answer, index) in answerItem" :key="index" class="table-row"
          :class="answer.severity.toLowerCase()">
          <div class="cell">{{ answer.violation_type }}</div>
          <div class="cell">
            <span :class="{ 'severity-badge critical': answer.severity === 'Высокая', 'severity-badge high': answer.severity === 'Средняя', 'severity-badge low': answer.severity === 'Низкая' }">{{ answer.severity }}</span>
          </div>
          <div class="cell">{{ answer.description }}</div>
          <div class="cell">
            <button @click="toggleRecommendations(fileIndex, index)" class="toggle-btn">
              {{ showRecommendations[`${fileIndex}-${index}`] ? 'Скрыть' : 'Показать' }}
            </button>
            <div v-if="showRecommendations[`${fileIndex}-${index}`]" class="recommendations">
              {{ answer.suggestions }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, ref } from 'vue'

const props = defineProps({
  response: {
    type: Object,
    required: true
  }
})

const showRecommendations = ref({})

const toggleRecommendations = (fileIndex, index) => {
  const key = `${fileIndex}-${index}`
  showRecommendations.value[key] = !showRecommendations.value[key]
}
</script>

<style scoped>
.analysis-results {
  font-family: 'Roboto', sans-serif;
  margin: 0 auto;
  margin-top: 2rem;
  padding: 20px;
  background-color: #fff;
  border-radius: 0.5rem;
  box-shadow: 0 1px 30px rgba(0, 0, 0, 0.2);
}

.section-title {
  font-size: 28px;
  color: #2c3e50;
  margin-bottom: 20px;
}

.file-title {
  font-size: 20px;
  color: #34495e;
  margin-bottom: 15px;
  text-align: center;
  margin-top: 3rem;
}

.results-table {
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  overflow: hidden;
}

.table-header {
  display: flex;
  background-color: #f5f5f5;
  font-weight: bold;
}

.header-cell {
  flex: 1;
  padding: 12px;
  text-align: left;
  color: #2c3e50;
}

.table-row {
  display: flex;
  border-top: 1px solid #e0e0e0;
}

.table-row:nth-child(even) {
  background-color: #f9f9f9;
}

.cell {
  flex: 1;
  padding: 12px;
  text-align: left;
}

.severity-badge {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
  text-transform: uppercase;
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

.toggle-btn {
  background-color: #3498db;
  color: #fff;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.2s ease-in-out;
}

.toggle-btn:hover {
  background-color: #2980b9;
}

.recommendations {
  margin-top: 10px;
  padding: 10px;
  background-color: #ecf0f1;
  border-radius: 4px;
  font-size: 14px;
  color: #34495e;
}
</style>