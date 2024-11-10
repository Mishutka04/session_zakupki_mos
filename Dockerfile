FROM python:3.11.9-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Прописываем команду запуска сервера
CMD ["python", "./backend/manage.py", "runserver"]
