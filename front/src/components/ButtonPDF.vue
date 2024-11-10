<template>
    <button class="btn-primary" @click="savePNG">
        Скачать PDF
    </button>
</template>
<script setup>
import { defineProps } from 'vue'
import html2pdf from 'html2pdf.js';
function savePNG() {
    setTimeout(() => {
        const element = props.block
        if (!element) {
            console.error("Элемент не найден!");
            return;
        }

        const options = {
            margin: 1,
            filename: 'generated-pdf.pdf',
            image: { type: 'jpeg', quality: 0.98 },
            html2canvas: { scale: 2 },
            jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
        };

        html2pdf()
            .from(element)
            .set(options)
            .save(); // Сохранение файла
    }, 1000); // Ожидание загрузки ресурсов
}
const props = defineProps({
    block: {
        type: Object,
        required: true
    },
});
</script>
<style>
.btn-primary {
    width: 100%;
    background-color: #3b82f6;
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
</style>