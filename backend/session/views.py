# views.py
from rest_framework import generics
from .models import QuotationSession, Violation
from .serializers import QuotationSessionSerializer, TenderURLSerializer, ViolationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .parserAPI import main
# from .parserAPI_asynco import main
from .ollama3_handler import main
from asgiref.sync import async_to_sync
import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start_time = time.perf_counter()  # Время начала обработки
        response = func(self, *args, **kwargs)  # Вызов оригинальной функции
        end_time = time.perf_counter()  # Время окончания обработки
        processing_time = end_time - start_time
        print(f"Время обработки запроса: {processing_time:.2f} секунд.")
        return response  # Возвращаем ответ оригинальной функции
    return wrapper


class QuotationSessionAPIView(generics.ListAPIView):
    queryset = QuotationSession.objects.all()  # Получаем все объекты сессий котирования
    serializer_class = QuotationSessionSerializer  # Указываем сериализатор для обработки данных


class TenderDataView(APIView):
    serializer_class = TenderURLSerializer

    @measure_time
    def post(self, request):
        serializer = TenderURLSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            violations = serializer.validated_data['selected_rules']
            # Переводим async main в синхронный вызов
            try:
                response_data = async_to_sync(main)(url, violations)
                try:
                    # answers_str = response_data.get("answers", "Ошибка обработки данных.")
                    answers_str = {
                        "answers": response_data.get("answers", "Ошибка обработки данных."),
                        "session_info": response_data.get("session_info", "Ошибка обработки данных."),
                        "files": response_data.get("files", "Ошибка обработки данных.")
                    }
                except AttributeError:
                    return Response({"error": "Ошибка обработки данных. Выполните запрос повторно."}, status=status.HTTP_400_BAD_REQUEST)
                return Response(answers_str, status=status.HTTP_200_OK)
            except TypeError as e:
                print("Ошибка обработки данных:", e)
                return Response({"error": "Ошибка обработки данных."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TenderDataView(APIView):
#     serializer_class = TenderURLSerializer

#     @measure_time
#     def post(self, request):
#         serializer = TenderURLSerializer(data=request.data)
#         if serializer.is_valid():
#             url = serializer.validated_data['url']
#             # Переводим async main в синхронный вызов
#             try:
#                 response_data = async_to_sync(main)(url)
#                 try:
#                     # answers_str = response_data.get("answers", "Ошибка обработки данных.")
#                     answers_str = {
#                         "answers": response_data.get("answers", "Ошибка обработки данных."),
#                         "session_info": response_data.get("session_info", "Ошибка обработки данных."),
#                         "files": response_data.get("files", "Ошибка обработки данных.")
#                     }
#                 except AttributeError:
#                     return Response({"error": "Ошибка обработки данных. Выполните запрос повторно."}, status=status.HTTP_400_BAD_REQUEST)
#                 return Response(answers_str, status=status.HTTP_200_OK)
#             except TypeError as e:
#                 print("Ошибка обработки данных:", e)
#                 return Response({"error": "Ошибка обработки данных."}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViolationsAPIView(generics.ListAPIView):
    queryset = Violation.objects.all()  # Получаем все объекты сессий котирования
    serializer_class = ViolationSerializer 
