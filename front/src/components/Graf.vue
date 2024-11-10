<template>
    <div class="delivery-page">
        <div class="header">
            <div class="tab"><b>График</b></div>
        </div>

        <div class="delivery-stage">
            <div class="stage-number">
                <span>1</span>
            </div>
            <div class="stage-title">Этап поставки</div>
            <div class="stage-price">{{ response.session_info.startCost }} ₽</div>
        </div>

        <div class="delivery-address">
            <div class="address-icon">📍</div>
            <div class="address-text">
                {{ response.session_info.deliveries.deliveryPlace }}
            </div>
            <div class="delivery-time">
                <span class="time-icon">🕒</span>
                <div
                    v-if="response.session_info.deliveries.periodDaysFrom && response.session_info.deliveries.periodDaysTo">
                    {{ response.session_info.deliveries.periodDaysFrom }} - {{
                        response.session_info.deliveries.periodDaysTo }} дней </div>
                <div v-else>{{ response.session_info.deliveries.periodDateFrom }} - {{response.session_info.deliveries.periodDateTo }}</div>

            </div>
        </div>

        <div class="specification-section">
            <div class="specification-header" @click="toggleSpecification">
                <span>Спецификация</span>
                <span class="arrow" :class="{ 'arrow-down': isSpecificationOpen }">▼</span>
            </div>

            <div class="specification-table" v-if="isSpecificationOpen">
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
                        <tr v-for="(item, index) in response.session_info.deliveries.items" :key="index">
                            <td>{{ response.session_info.customer }}</td>
                            <td>{{ item.name }}</td>
                            <td>{{ item.costPerUnit }} ₽</td>
                            <td>{{ item.quantity }}</td>
                            <td>{{ item.sum }} ₽</td>
                        </tr>
                    </tbody>
                </table>
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
    },
})
const isSpecificationOpen = ref(true)

const toggleSpecification = () => {
    isSpecificationOpen.value = !isSpecificationOpen.value
}
</script>
<style scoped>
.delivery-page {

    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    margin-top: 2rem;
    background-color: #fff;
    border-radius: 0.5rem;
    box-shadow: 0 1px 30px rgba(0, 0, 0, 0.2);
}

.header {
    text-align: center;
    /* border-bottom: 1px solid #e0e0e0; */
    margin-bottom: 20px;
    overflow-x: auto;
    color: black;
}

.tab {
    padding: 10px 20px;
    color: black;
    font-size: 1.5rem;
    font-weight: bold;
}

.tab.active {
    color: #1a4f8b;
    border-bottom: 2px solid #1a4f8b;
}

.delivery-stage {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    gap: 15px;
    flex-wrap: wrap;
}

.stage-number {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    border: 2px solid #1a4f8b;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #1a4f8b;
    font-weight: bold;
}

.stage-title {
    font-size: 18px;
    font-weight: bold;
    flex-grow: 1;
}

.stage-price {
    font-size: 18px;
    font-weight: bold;
    color: #1a4f8b;
}

.delivery-address {
    display: flex;
    align-items: flex-start;
    background-color: #fff;
    padding: 15px;
    border-radius: 4px;
    margin-bottom: 20px;
    gap: 10px;
    flex-wrap: wrap;
}

.address-icon,
.time-icon {
    font-size: 20px;
}

.address-text {
    flex-grow: 1;
    color: #333;
    min-width: 200px;
}

.delivery-time {
    color: #666;
    display: flex;
    align-items: center;
    gap: 5px;
}

.specification-section {
    background-color: #fff;
    border-radius: 4px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.specification-header {
    padding: 15px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    font-weight: bold;
    border-bottom: 1px solid #e0e0e0;
    background-color: rgb(231, 238, 247);
}

.arrow {
    font-size: 12px;
    transition: transform 0.3s ease;
}

.arrow-down {
    transform: rotate(180deg);
}

.specification-table {
    padding: 0;
    overflow-x: auto;
}

table {
    width: 100%;
    border-collapse: collapse;
    background-color: white;
}

th,
td {
    padding: 12px 15px;
    text-align: left;
    border: none;
    font-size: 14px;
}

th {
    background-color: #f8f9fa;
    font-weight: normal;
    color: #666;
}

td {
    color: #333;
}

tbody tr {
    border-bottom: 1px solid #e0e0e0;
}

tbody tr:last-child {
    border-bottom: none;
}

th:first-child,
td:first-child {
    padding-left: 20px;
}

th:last-child,
td:last-child {
    padding-right: 20px;
}

@media (max-width: 768px) {
    .delivery-stage {
        flex-direction: column;
        align-items: flex-start;
    }

    .delivery-address {
        flex-direction: column;
    }

    .address-text,
    .delivery-time {
        width: 100%;
    }

    th,
    td {
        padding: 10px;
    }

    th:first-child,
    td:first-child,
    th:last-child,
    td:last-child {
        padding-left: 10px;
        padding-right: 10px;
    }
}

@media (max-width: 480px) {
    .delivery-page {
        padding: 10px;
    }

    .header {
        gap: 10px;
    }

    .tab {
        padding: 10px;
    }

    .stage-title,
    .stage-price {
        font-size: 16px;
    }

    th,
    td {
        font-size: 12px;
    }
}
</style>