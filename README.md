## Курсовая 6. Основы веб-разработки на Django

### 1. Для запуска приложения необходимо настроить виртуальное окружение и установить все необходимые зависимости с помощью команд:
    Команда для Windows:
        - python -m venv venv
        - venv\Scripts\activate
        - pip install -r requirement.txt

    Команда для Unix:
        - python3 -m venv venv
        - source venv/bin/activate 
        - pip install -r requirement.txt

### 2. Для запуска celery:
        - celery -A config beat --loglevel=info celery -A config worker --loglevel=info

### 3. Для запуска redis:
    Redis официально не поддерживается в Windows: 
        - Установите WSL2, Ubuntu. Подробности смотрите тут https://redis.io/docs/getting-started/installation/install-redis-on-windows/
        - sudo apt-get update (обновление)
        - sudo service redis-server start
        - redis-cli
        - Проверка работает ли сервер Redis: введите Ping, ответ от сервера: Pong

    Команда для Unix:
        - redis-cli

### 4. Для заполнения моделей данными необходимо выполнить следующую команду: 
    Команда для Windows:
        - python manage.py fill

    Команда для Unix:
        - python3 manage.py fill

### 5. Для работы с переменными окружениями необходимо заполнить файл
    - env.examples

### 6. Для создания администратора (createsuperuser)
    - заполните поля email, PASSWORD. users/management/commands/csu.py
    - python manage.py csu (Windows)
    - python3 manage.py csu (Unix)

### 7. Для запуска приложения: 
    Команда для Windows:
    - python manage.py runserver

    Команда для Unix:
    - python3 manage.py runserver

### 8. Для отправки рассылки из командной строки: 
    Команда для Windows:
    - python manage.py sendmessage N, где N - это pk рассылки

    Команда для Unix:    
    - python3 manage.py sendmessage N, где N - это pk рассылки