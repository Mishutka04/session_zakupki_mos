<template>
    <div class="specifications">
        <h4 class="section-title">Спецификации</h4>
        <div class="specifications-list">
            <div v-for="item in response.session_info.items" :key="item.name" class="specification-item">
                <img :src="item.image_url" :alt="item.name" class="specification-image">
                <div class="specification-details">
                    <h5 class="specification-name">{{ item.name }}</h5>
                    <div class="specification-grid">
                        <div class="specification-data">
                            <p class="data-label">Количество</p>
                            <p class="data-value">{{ item.currentValue }} {{ item.okeiName }}</p>
                        </div>
                        <div class="specification-data">
                            <p class="data-label">Цена за единицу</p>
                            <p class="data-value">{{ item.costPerUnit }} ₽</p>
                        </div>
                        <div class="specification-data">
                            <p class="data-label">Общая стоимость</p>
                            <p class="data-value">{{ item.currentValue * item.costPerUnit }} ₽</p>
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


</script>

<style scoped></style>