<template>
  <div class="quotation-session">
    <header class="header">
      <h1>Портал поставщиков</h1>
      <button class="register-btn">Зарегистрироваться</button>
    </header>

    <main class="main-content">
      <a href="#" class="back-link">
        <span class="icon">←</span> Вернуться в реестр котировочных сессий
      </a>

      <div class="session-info">
        <div>
          <h2>Котировочная сессия 9862557</h2>
          <span class="status">Нет ошибок</span>
        </div>
        <div class="price-info">
          <p>Начальная цена</p>
          <p class="price">23 005,39 ₽</p>
        </div>
      </div>

      <h3>ИЗДЕЛИЯ КАНЦЕЛЯРСКИЕ, БУМАГА И БУМАЖНЫЕ ИЗДЕЛИЯ</h3>

      <div class="section">
        <h4>Условия исполнения контракта</h4>
        <p>Обязательное электронное исполнение с использованием УПД</p>
        <div class="error-section">
          <div class="error">
            <span class="icon">⚠️</span> Ошибка в составлении документа
          </div>
          <button @click="toggleErrorComment('contract')" class="comment-btn">
            {{ showErrorComments.contract ? 'Скрыть комментарий' : 'Показать комментарий' }}
          </button>
          <div class="correct">
            <span class="icon">✅</span> Правильно
          </div>
        </div>
        <div v-if="showErrorComments.contract" class="error-comment">
          Комментарий по ошибке: Необходимо уточнить детали использования УПД.
        </div>
      </div>

      <div class="section">
        <h4>Документы</h4>
        <ul>
          <li v-for="(doc, index) in documents" :key="index">
            <div class="document-item">
              <a :href="doc.url" class="document-link">
                <span class="icon">📄</span> {{ doc.name }}
              </a>
              <div class="error-section">
                <div class="error">
                  <span class="icon">⚠️</span> Ошибка в документе
                </div>
                <button @click="toggleErrorComment(`doc-${index}`)" class="comment-btn">
                  {{ showErrorComments[`doc-${index}`] ? 'Скрыть комментарий' : 'Показать комментарий' }}
                </button>
                <div class="correct">
                  <span class="icon">✅</span> Правильно
                </div>
              </div>
            </div>
            <div v-if="showErrorComments[`doc-${index}`]" class="error-comment">
              {{ doc.errorComment }}
            </div>
          </li>
        </ul>
      </div>

      <div class="section">
        <h4>Спецификации</h4>
        <ul>
          <li v-for="(item, index) in specifications" :key="index" class="specification-item">
            <div @click="toggleSpecification(index)" class="specification-header">
              <div>
                <h5>{{ item.name }}</h5>
                <p>Количество: {{ item.quantity }}</p>
              </div>
              <span class="icon">{{ item.showDetails ? '▲' : '▼' }}</span>
            </div>
            <div v-if="item.showDetails" class="specification-details">
              <p>{{ item.description }}</p>
              <div class="error-section">
                <div v-for="(error, errorIndex) in item.errors" :key="errorIndex" class="error">
                  <span class="icon">⚠️</span> {{ error.message }}
                </div>
                <button @click="toggleErrorComment(`spec-${index}`)" class="comment-btn">
                  {{ showErrorComments[`spec-${index}`] ? 'Скрыть комментарии' : 'Показать комментарии' }}
                </button>
                <div class="correct">
                  <span class="icon">✅</span> Правильно
                </div>
              </div>
              <div v-if="showErrorComments[`spec-${index}`]" class="error-comment">
                <p v-for="(error, errorIndex) in item.errors" :key="errorIndex">
                  {{ error.comment }}
                </p>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </main>

    <footer class="footer">
      <div class="footer-links">
        <a href="#">О портале</a>
        <a href="#">Контакты</a>
        <a href="#">Новости</a>
        <a href="#">Центр поддержки</a>
        <a href="#">Карта сайта</a>
      </div>
      <p>© 2017-2024 v.20241003</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const showErrorComments = reactive({
  contract: false,
})

const documents = [
  { 
    name: 'Канцелярия бумага.docx', 
    url: '#', 
    errorComment: 'Неверный формат документа. Требуется PDF.' 
  },
  { 
    name: 'Проект контракта.pdf', 
    url: '#', 
    errorComment: 'Отсутствует подпись ответственного лица.' 
  },
]

const specifications = ref([
  {
    name: 'Бумага для офисной техники "CARTBLANK" А4, 500 л, 100 микрон',
    quantity: '60 шт',
    description: 'Высококачественная бумага для офисной техники.',
    showDetails: false,
    errors: [
      { message: 'Несоответствие заявленной плотности', comment: 'Фактическая плотность 80 г/м², а не 100 микрон.' },
      { message: 'Ошибка в количестве', comment: 'Требуется 80 шт, а не 60 шт.' }
    ]
  },
  {
    name: 'Файл-вкладыш Attache А4 60 мкм прозрачный рифленый 100 штук в упаковке',
    quantity: '1 упак',
    description: 'Прозрачные файлы-вкладыши для хранения документов.',
    showDetails: false,
    errors: [
      { message: 'Ошибка в спецификации', comment: 'Требуется гладкая поверхность, а не рифленая.' }
    ]
  },
  {
    name: 'Папка-уголок 180 мкм А4 прозрачный',
    quantity: '10 шт',
    description: 'Прочные папки-уголки для хранения документов.',
    showDetails: false,
    errors: [
      { message: 'Ошибка в толщине материала', comment: 'Требуется 200 мкм, а не 180 мкм.' }
    ]
  },
])

const toggleErrorComment = (key) => {
  showErrorComments[key] = !showErrorComments[key]
}

const toggleSpecification = (index) => {
  specifications.value[index].showDetails = !specifications.value[index].showDetails
}
</script>

<style scoped>
ul { list-style-type: none; }
.quotation-session {
  font-family: Arial, sans-serif;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.register-btn {
  background-color: #ff4d4f;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
}

.main-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.back-link {
  display: inline-flex;
  align-items: center;
  color: #1890ff;
  text-decoration: none;
  margin-bottom: 20px;
}

.session-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.status {
  background-color: #52c41a;
  color: white;
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 12px;
}

.price-info {
  text-align: right;
}

.price {
  font-size: 24px;
  font-weight: bold;
}

.section {
  margin-bottom: 20px;
}

.error-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}

.error, .correct {
  display: flex;
  align-items: center;
}

.error {
  color: #ff4d4f;
}

.correct {
  color: #52c41a;
}

.comment-btn {
  background: none;
  border: none;
  color: #1890ff;
  cursor: pointer;
}

.error-comment {
  background-color: #fff1f0;
  border: 1px solid #ffccc7;
  padding: 10px;
  margin-top: 10px;
  border-radius: 4px;
}

.document-item, .specification-item {
  border: 1px solid #d9d9d9;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 4px;
}

.document-link {
  color: #1890ff;
  text-decoration: none;
}

.specification-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
}

.specification-details {
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px solid #d9d9d9;
}

.footer {
  margin-top: 40px;
  text-align: center;
}

.footer-links {
  margin-bottom: 10px;
}

.footer-links a {
  color: #8c8c8c;
  text-decoration: none;
  margin: 0 10px;
}

.icon {
  margin-right: 5px;
}
</style>