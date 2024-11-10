<template>
  <!-- Header -->
  <Header />
  <div class="procurement-portal">
    <!-- Main Content -->
    <main class="main-content" ref='template_page'>
      <!-- Initial Form State -->
      <div v-if="!hasResponses" class="form-container">
        <div class="form-card">
          <h2 class="form-title">Анализ котировочной сессии</h2>

          <div v-for="(form, index) in forms" :key="index" class="form-group">
            <input v-model="form.url" type="text" placeholder="Введите URL котировочной сессии" class="form-input">
            <div class="checkbox-group">
              <label v-for="(rule, ruleIndex) in processingRules" :key="ruleIndex" class="checkbox-label">
                <input type="checkbox" v-model="form.selected_rules" :value="rule.value" class="checkbox-input">
                {{ rule.label }}
              </label>
            </div>
            <p v-if="!isFormValid" class="error-message">Пожалуйста, выберите хотя бы один чекбокс для каждого URL.</p>
            <button @click="selectAllCheckboxes(index)" class="select-all-button">
              {{ isAllSelected(index) ? 'Отменить все' : 'Выбрать все' }}
            </button>
          </div>
          

          <button @click="sendRequests" :disabled="loading || !isFormValid" class="form-button">
            <span v-if="loading" class="loading-spinner"></span>
            <span v-if="loading">Загрузка...</span>
            <span v-else>Проанализировать</span>
          </button>

          <button @click="addNewForm" class="add-form-button">
            Добавить новое URL
          </button>
        </div>
      </div>

      <!-- Results State -->
      <div v-else-if="hasResponses && !loading" class="results-container">
        <div v-for="(response, index) in responses" :key="index">
          <!-- Session Details -->
          <div class="session-details">
            <!-- Basic Info -->
            <BasicInfo :response="response" v-if="response.session_info" />

            <!-- Specifications -->
            <Specifications :response="response" v-if="response.session_info" />

            <!-- Files -->
            <Files :response="response" v-if="response.files" />
            <Graf :response="response" v-if="response.files" />
            <!-- Analysis Results -->
            <Analys :response="response" v-if="response.answers" />
          </div>
        </div>

        <!-- Actions -->
        <div class="actions">
          <ButtonPDF :block="template_page" />
          <button class="btn-primary red" @click="savePNG">
            Внести изменения в карточку
          </button>
          <button @click="resetForm" class="back-button">
            ← Вернуться к анализу другой сессии
          </button>
        </div>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="error-container">
        <div class="error-card">
          <h3 class="error-title">Произошла ошибка</h3>
          <p class="error-message">{{ error }}</p>
          <button @click="resetForm" class="retry-button">
            Попробовать снова
          </button>
        </div>
      </div>
    </main>
  </div>
  <Footer />
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import Header from './Header.vue'
import Footer from './Footer.vue'
import Files from './Files.vue'
import Analys from './Analys.vue'
import BasicInfo from './BasicInfo.vue'
import Specifications from './Specifications.vue'
import ButtonPDF from './ButtonPDF.vue'
import Graf from './Graf.vue'

const template_page = ref(null)
const forms = ref([{ url: '', selected_rules: [] }])
const responses = ref([])
const loading = ref(false)
const error = ref(null)

const processingRules = ref([])

const isFormValid = computed(() => {
  return forms.value.every(form => form.selected_rules.length > 0)
})

const hasResponses = computed(() => responses.value.length > 0)

const addNewForm = () => {
  forms.value.push({ url: '', selected_rules: [] })
}

const isAllSelected = (formIndex) => {
  const form = forms.value[formIndex]
  return form.selected_rules.length === processingRules.value.length
}

const selectAllCheckboxes = (formIndex) => {
  const form = forms.value[formIndex]
  if (isAllSelected(formIndex)) {
    // If all checkboxes are selected, unselect all
    form.selected_rules = []
  } else {
    // Otherwise, select all checkboxes
    form.selected_rules = processingRules.value.map(rule => rule.value)
  }
}

onMounted(() => {
  getCheckBox();
});

const getCheckBox = async () => {
  try {
    const response = await axios.get('https://zakupkiru.firecalculation.ru/api/api/violations/');
    console.log(response.data)
    // Предполагаем, что response.data - это массив объектов
    response.data.forEach(item => {
      const newRule = {
        label: item.name, // Имя правила
        value: { 'name': item.name, 'example': item.example } // Значение правила
      };

      // Добавляем новое правило в массив processingRules
      processingRules.value.push(newRule);
    });
  } catch (error) {
    console.error('Ошибка при получении данных:', error);
  }
};

const sendRequests = async () => {
  console.log(forms.value)
  if (!isFormValid.value) {
    error.value = 'Пожалуйста, выберите хотя бы один чекбокс для каждого URL.'
    return
  }

  loading.value = true
  error.value = null
  responses.value = []

  try {
    const requests = forms.value.map(form =>
      axios.post('https://zakupkiru.firecalculation.ru/api/api/tender/', {
        url: form.url,
        selected_rules: form.selected_rules
      })
    )

    const results = await Promise.all(requests)
    responses.value = results.map(res => res.data)
    console.log(responses.value)
  } catch (err) {
    error.value = 'Произошла ошибка при обработке одного или нескольких запросов'
  } finally {
    loading.value = false
  }
}

const resetForm = () => {
  forms.value = [{ url: '', selected_rules: [] }]
  responses.value = []
  error.value = null
}

const getTimeLeft = (endDate) => {
  const end = new Date(endDate)
  const now = new Date()
  const diff = end - now

  if (diff <= 0) return { days: '00', hours: '00', minutes: '00', seconds: '00' }

  const days = Math.floor(diff / (1000 * 60 * 60 * 24))
  const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
  const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60))
  const seconds = Math.floor((diff % (1000 * 60)) / 1000)

  return {
    days: String(days).padStart(2, '0'),
    hours: String(hours).padStart(2, '0'),
    minutes: String(minutes).padStart(2, '0'),
    seconds: String(seconds).padStart(2, '0')
  }
}
</script>

<style>
.red{
  background-color: red;
}
.btn-primary {
  width: 100%;
  /* background-color: #3b82f6; */
  color: #ffffff;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
  margin-bottom: 0.5rem;
}

.btn-primary:hover {
  background-color: #2563eb;
}

.procurement-portal {
  background-color: #f4f6f8;
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.logo-container {
  display: flex;
  align-items: center;
}

.logo {
  height: 40px;
  margin-right: 1rem;
}

.portal-title {
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
}

.main-content {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.form-container,
.results-container,
.error-container {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 2rem;
}

.form-title,
.section-title {
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
  margin-bottom: 1.5rem;
  text-align: center;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 4rem;
}

.form-input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
}

.form-button {
  width: 100%;
  background-color: #1976d2;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  padding: 0.75rem;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.form-button:hover {
  background-color: #1565c0;
}

.form-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.loading-spinner {
  display: inline-block;
  width: 1rem;
  height: 1rem;
  border: 2px solid #ffffff;
  border-top: 2px solid transparent;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-right: 0.5rem;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

.session-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
}

.session-title-container {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.session-title {
  font-size: 1.25rem;
  font-weight: bold;
  color: #333;
}

.session-status {
  padding: 0.25rem 0.5rem;
  border-radius: 9999px;
  font-size: 1.2rem;
  font-weight: medium;
  color: #32eb0d;
}

.session-status.active {
  background-color: #4caf50;
  color: #ffffff;
}

.session-name {
  font-size: 1.7rem;
  color: #264b82;
  margin-top: 0.5rem;
}

.timer-container {
  background-color: #e3f2fd;
  padding: 1rem;
  border-radius: 8px;
}

.timer-title {
  font-size: 0.875rem;
  font-weight: medium;
  color: #1976d2;
  margin-bottom: 0.5rem;
}

.timer-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.5rem;
}

.timer-cell {
  background-color: #ffffff;
  padding: 0.5rem;
  border-radius: 4px;
  text-align: center;
}

.timer-value {
  font-size: 1.25rem;
  font-weight: bold;
  color: #1976d2;
}

.timer-label {
  font-size: 0.75rem;
  color: #666;
}


.info-label {
  font-size: 0.875rem;
  color: #666;
  margin-bottom: 0.25rem;
}

.info-value {
  font-size: 1rem;
  color: #333;
  font-weight: medium;
}

.specifications-list {
  display: grid;
  gap: 1rem;
}

.specifications {
  padding-top: 20px;
  background-color: #fff;
  border-radius: 0.5rem;
  box-shadow: 0 1px 30px rgba(0, 0, 0, 0.2);
}

.specification-item {
  display: flex;
  gap: 1rem;
  padding: 1rem;
  background-color: #f9f9f9;
  border-radius: 8px;
}

.specification-image {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 4px;
}

.specification-details {
  flex: 1;
}

.specification-name {
  font-size: 1rem;
  font-weight: medium;
  color: #333;
  margin-bottom: 0.5rem;
}

.specification-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.data-label {
  font-size: 0.75rem;
  color: #666;
  margin-bottom: 0.25rem;
}

.data-value {
  font-size: 0.875rem;
  color: #333;
  font-weight: medium;
}

.files-section {
  margin-top: 2rem;
}

.file-list {
  list-style-type: none;
  padding: 0;
}

.file-item {
  display: flex;
  align-items: center;
  margin-bottom: 0.5rem;
}

.file-icon {
  width: 24px;
  height: 24px;
  margin-right: 0.5rem;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}

.file-link {
  color: #1976d2;
  text-decoration: none;
  transition: color 0.3s;
}

.file-link:hover {
  color: #1565c0;
  text-decoration: underline;
}

.results-list {
  display: grid;
  gap: 1rem;
}

.result-item {
  padding: 1rem;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
}

.result-item.высокая {
  border-color: #f44336;
  background-color: #ffebee;
}

.result-item.средняя {
  border-color: #ff9800;
  background-color: #fff3e0;
}

.result-item.низкая {
  border-color: #4caf50;
  background-color: #e8f5e9;
}

.result-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.result-title {
  font-size: 1rem;
  font-weight: medium;
  color: #333;
}

.result-severity {
  font-size: 0.75rem;
  font-weight: medium;
  padding: 0.25rem 0.5rem;
  border-radius: 9999px;
}

.result-item.высокая .result-severity {
  background-color: #f44336;
  color: #ffffff;
}

.result-item.средняя .result-severity {
  background-color: #ff9800;
  color: #ffffff;
}

.result-item.низкая .result-severity {
  background-color: #4caf50;
  color: #ffffff;
}

.result-description {
  font-size: 0.875rem;
  color: #333;
  margin-bottom: 0.5rem;
}

.recommendations-title {
  font-size: 0.875rem;
  font-weight: medium;
  color: #333;
  margin-bottom: 0.25rem;
}

.recommendations-text {
  font-size: 0.875rem;
  color: #666;
}

.actions {
  margin-top: 2rem;
  text-align: center;
}

.back-button {
  background: none;
  border: none;
  color: #1976d2;
  font-size: 1rem;
  cursor: pointer;
  transition: color 0.3s;
}

.back-button:hover {
  color: #1565c0;
}

.error-card {
  text-align: center;
}

.error-title {
  font-size: 1.25rem;
  font-weight: bold;
  color: #f44336;
  margin-bottom: 1rem;
}

.error-message {
  font-size: 1rem;
  color: #666;
  margin-bottom: 1rem;
}

.retry-button {
  background-color: #f44336;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.retry-button:hover {
  background-color: #d32f2f;
}

.checkbox-group {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.checkbox-label {
  display: flex;
  align-items: center;
  font-size: 0.875rem;
  color: #333;
}

.checkbox-input {
  margin-right: 0.5rem;
}

.add-form-button {
  background-color: #dc2626;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  padding: 0.75rem;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-top: 1rem;
  width: 100%;
}

.add-form-button:hover {
  background-color: #dc2626;
}

.select-all-button {
  width: 100%;
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 10px;
  margin-bottom: 10px;
  cursor: pointer;
  border-radius: 4px;
  font-size: 1rem;
  transition: background-color 0.3s;
}

.select-all-button:hover {
  background-color: #45a049;
}

@media (max-width: 768px) {
  .session-header {
    flex-direction: column;
    gap: 1rem;
  }

  .timer-container {
    width: 100%;
  }

  .specification-item {
    flex-direction: column;
  }

  .specification-image {
    width: 100%;
    height: auto;
    max-height: 200px;
  }

  .specification-grid {
    grid-template-columns: 1fr;
  }

  .checkbox-group {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .form-container,
  .results-container,
  .error-container {
    padding: 1rem;
  }

  .timer-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .basic-info {
    grid-template-columns: 1fr;
  }

  .checkbox-group {
    grid-template-columns: 1fr;
  }
}
</style>