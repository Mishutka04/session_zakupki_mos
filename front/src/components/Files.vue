<template>
  <div v-if="response.files && response.files.length > 0" class="file-list">
    <h4 class="file-list__title">Документы</h4>
    <div class="file-list__container">
      <ul class="file-list__items">
        <li v-for="file in response.files" :key="file[0]" class="file-item">
          <div class="file-item__content">
            <span :class="getFileIconClass(file[0])" class="file-item__icon"></span>
            <span class="file-item__name">{{ file[1] }}</span>
          </div>
          <button @click="downloadFile(file[0])" class="file-item__download">
            Скачать
          </button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  response: {
    type: Object,
    required: true
  }
})

const getFileIconClass = (fileName) => {
  const extension = fileName.split('.').pop().toLowerCase()
  switch (extension) {
    case 'pdf':
      return 'file-item__icon--pdf'
    case 'doc':
    case 'docx':
      return 'file-item__icon--word'
    case 'xls':
    case 'xlsx':
      return 'file-item__icon--excel'
    case 'jpg':
    case 'jpeg':
    case 'png':
      return 'file-item__icon--image'
    default:
      return 'file-item__icon--default'
  }
}

const downloadFile = (fileUrl) => {
  window.open(fileUrl, '_blank')
}
</script>

<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

.file-list {
  margin-top: 2rem;
  padding: 1.5rem;
  background-color: #fff;
  border-radius: 0.5rem;
  box-shadow: 0 1px 30px rgba(0, 0, 0, 0.2);
}

.file-list__title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 1rem;
  text-align: center;
  padding-top: 1.5rem;
  
}

.file-list__container {

  padding: 1.5rem;
}

.file-list__items {
  list-style-type: none;
  display: flex;
  flex-direction: column;
  padding: 0;
  margin: 0;
}

.file-item {
  display: inline-block;
  align-items: center;
  justify-content: space-between;
  background-color: #f8f9fa;
  border-radius: 6px;
  padding: 1rem;
  margin-bottom: 1rem;
  transition: background-color 0.3s ease;
}

.file-item:hover {
  background-color: #e9ecef;
}

.file-item__content {
  display: flex;
  align-items: center;
  flex-grow: 1;
}

.file-item__icon {
  font-size: 1.5rem;
  margin-right: 1rem;
}

.file-item__icon--pdf::before {
  content: '\f1c1';
  font-family: 'Font Awesome 6 Free';
  color: #dc3545;
}

.file-item__icon--word::before {
  content: '\f1c2';
  font-family: 'Font Awesome 6 Free';
  color: #007bff;
}

.file-item__icon--excel::before {
  content: '\f1c3';
  font-family: 'Font Awesome 6 Free';
  color: #28a745;
}

.file-item__icon--image::before {
  content: '\f1c5';
  font-family: 'Font Awesome 6 Free';
  color: #6f42c1;
}

.file-item__icon--default::before {
  content: '\f15b';
  font-family: 'Font Awesome 6 Free';
  color: #6c757d;
}

.file-item__name {
  font-size: 1rem;
  color: #333;
}

.file-item__download {
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 0.875rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-left: 1rem;
}

.file-item__download:hover {
  background-color: #0056b3;
}

@media (max-width: 768px) {
  .file-item {
    flex-direction: column;
    align-items: flex-start;
  }

  .file-item__download {
    margin-left: 0;
    margin-top: 1rem;
    align-self: stretch;
  }
}
</style>