# serializers.py
from rest_framework import serializers
from .models import QuotationSession, Violation

class QuotationSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationSession  # Указываем модель для сериализации
        fields = [
            'id', 
            'session_id', 
            'status', 
            'name', 
            'start_price', 
            'customer', 
            'location', 
            'regulatory_document', 
            'start_date', 
            'end_date', 
            'integration', 
            'contract_condition'
        ]


# # Сериализатор для проверки URL
# class TenderURLSerializer(serializers.Serializer):
#     url = serializers.URLField()

#     def validate_url(self, value):
#         # Проверка, что URL начинается с нужного префикса
#         if not value.startswith("https://zakupki.mos.ru/auction/"):
#             raise serializers.ValidationError(
#                 "URL должен начинаться с https://zakupki.mos.ru/auction/"
#             )
#         return value


class ViolationSerializer(serializers.Serializer):
    name = serializers.CharField()
    example = serializers.CharField()

class TenderURLSerializer(serializers.Serializer):
    url = serializers.URLField()
    # params = serializers.DictField(child=serializers.CharField(), required=False)
    selected_rules = serializers.ListField(child=ViolationSerializer(), required=False)  # Поле для списка нарушений

    def validate_url(self, value):
        # Проверка, что URL начинается с нужного префикса
        if not value.startswith("https://zakupki.mos.ru/auction/"):
            raise serializers.ValidationError(
                "URL должен начинаться с https://zakupki.mos.ru/auction/"
            )
        return value


class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation  # Указываем модель для сериализации
        fields = "__all__"