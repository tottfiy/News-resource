FROM python:3.11-alpine

# 2. Робоча директорія
WORKDIR /news

# 3. Встановлення залежностей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Копіюємо весь код проєкту
COPY . .

# 5. Проганяємо міграції під час побудови образу
RUN python manage.py makemigrations
RUN python manage.py migrate

# 6. Запускаємо сервер на 0.0.0.0:8008
CMD ["python", "manage.py", "runserver", "0.0.0.0:8008"]
