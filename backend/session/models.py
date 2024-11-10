# models.py
from django.db import models

class QuotationSession(models.Model):
    # Идентификатор сессии
    session_id = models.CharField(max_length=100, unique=True)
    # Статус сессии
    status = models.CharField(max_length=50)
    # Название сессии
    name = models.CharField(max_length=200)
    # Начальная цена
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Заказчик
    customer = models.CharField(max_length=200)
    # Местоположение
    location = models.CharField(max_length=200)
    # Регулирующий документ
    regulatory_document = models.CharField(max_length=200)
    # Дата старта
    start_date = models.DateTimeField()
    # Дата окончания
    end_date = models.DateTimeField()
    # Интеграция
    integration = models.CharField(max_length=200)
    # Условие контракта
    contract_condition = models.TextField()

    def __str__(self):
        return self.name  # Возвращает название сессии при выводе объекта


class Violation(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название нарушения")
    example = models.TextField(verbose_name="Пример нарушения")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Нарушение"
        verbose_name_plural = "Нарушения"
