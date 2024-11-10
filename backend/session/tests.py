from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class TenderAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url_template = "https://zakupki.mos.ru/auction/{}"

    def test_post_tender_urls(self):
        # Перебираем диапазон от 9867400 до 9867482
        for tender_id in range(9867400, 9867483):  # Включаем 9867482
            url = self.url_template.format(tender_id)
            response = self.client.post(reverse('tender-list'), {'url': url})  # Предполагается, что 'tender-list' - это имя вашего URL

            # Проверяем, что запрос выполнен успешно (статус 201 или 200 в зависимости от вашей логики)
            self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_200_OK])
            # Дополнительные проверки можно добавить здесь, например, проверка содержимого ответа


# Create your tests here.
