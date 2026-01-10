# Лекція 9: Розгортання Django на сервер

## Вступ до Deployment

Deployment — це процес переміщення додатку з локального комп'ютера на production сервер, щоб він був доступний в інтернеті.

Основні кроки:
1. Підготовка коду
2. Вибір хостингу
3. Налаштування сервера
4. Розгортання додатку
5. Моніторинг та обслуговування

## 1. Підготовка Django додатку до production

### 1.1 環境 змінні

```bash
# requirements.txt - список залежностей
pip freeze > requirements.txt
```

```
Django==4.2.0
djangorestframework==3.14.0
drf-spectacular==0.27.0
django-cors-headers==4.0.0
djangorestframework-simplejwt==5.2.0
gunicorn==20.1.0
psycopg2-binary==2.9.0
python-decouple==3.8
```

### 1.2 Settings для production

```python
# autocheck_api/settings.py

from decouple import config, Csv

# Development або Production
DEBUG = config('DEBUG', default=False, cast=bool)

# Секретний ключ
SECRET_KEY = config('SECRET_KEY')  # Обов'язково змінити!

# Дозволені хості
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
# ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# HTTPS налаштування
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# БД
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default=5432, cast=int),
    }
}

# Static файли
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/car_service/staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Media файли
MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/car_service/media'

# Логування
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
```

### 1.3 .gitignore для git

```
# .gitignore
.env
.venv/
*.pyc
__pycache__/
*.sqlite3
db.sqlite3
/staticfiles/
/media/
.DS_Store
*.log
.idea/
*.swp
*.swo
node_modules/
```

### 1.4 Тестування локально

```bash
# Налаштуйте .env для production
DEBUG=False
SECRET_KEY=your-secure-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=car_service_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

# Запустіть локально з production налаштуванням
python manage.py collectstatic
python manage.py check --deploy
```

## 2. Вибір хостингу

### Популярні варіанти:

#### 2.1 Heroku (простий, платний)
```bash
# Встановити Heroku CLI
curl https://cli.heroku.com/install.sh | sh

# Залогінитися
heroku login

# Створити додаток
heroku create car-service-api

# Додати змінні
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key

# Додати PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Develop GitHub
git push heroku main
```

#### 2.2 DigitalOcean (середньо-розмір, $5+/місяць)
```bash
# Найпростіше - App Platform
# Просто пов'язати GitHub репо і задати переменные
```

#### 2.3 AWS (потужний, можна безплатно 1 рік)
```bash
# Використати Elastic Beanstalk або EC2
eb create car-service-env
```

#### 2.4 Linode / Vultr (невеликі віртуальні машини)
```bash
# Найбільше контролю, але потрібні навички Linux
```

## 3. Розгортання на виділеному сервері (Linux/Ubuntu)

### 3.1 Підготовка сервера

```bash
# Оновити систему
sudo apt update && sudo apt upgrade -y

# Встановити Python та зависимости
sudo apt install python3.10 python3.10-venv python3.10-dev
sudo apt install postgresql postgresql-contrib
sudo apt install nginx
sudo apt install supervisor
sudo apt install git

# Перевірити версії
python3 --version
postgresql --version
nginx -v
```

### 3.2 Налаштування PostgreSQL

```bash
# Запустити PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Створити базу даних
sudo -u postgres psql

# У PostgreSQL консолі
CREATE DATABASE car_service_db;
CREATE USER car_user WITH PASSWORD 'secure_password_here';
ALTER ROLE car_user SET client_encoding TO 'utf8';
ALTER ROLE car_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE car_user SET default_transaction_deferrable TO on;
ALTER ROLE car_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE car_service_db TO car_user;
\q
```

### 3.3 Встановлення Django додатку

```bash
# Створити папку для додатку
sudo mkdir -p /var/www/car_service
cd /var/www/car_service

# Клонувати репозиторій
sudo git clone https://github.com/your-username/car_service_api_and_ui.git .

# Змінити власника
sudo chown -R ubuntu:ubuntu /var/www/car_service

# Створити віртуальне середовище
python3 -m venv venv
source venv/bin/activate

# Встановити залежності
pip install -r requirements.txt
pip install gunicorn

# Налаштувати .env
cat > .env << EOF
DEBUG=False
SECRET_KEY=your-secure-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_NAME=car_service_db
DB_USER=car_user
DB_PASSWORD=secure_password_here
DB_HOST=localhost
DB_PORT=5432
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EOF

# Збрати static файли
python manage.py collectstatic --noinput

# Запустити migrations
python manage.py migrate

# Створити суперкористувача
python manage.py createsuperuser
```

### 3.4 Налаштування Gunicorn

Gunicorn — це WSGI сервер для запуску Django.

```bash
# Створити systemd сервіс
sudo vim /etc/systemd/system/gunicorn.service
```

Вміст файлу:

```ini
[Unit]
Description=gunicorn daemon for car_service
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/var/www/car_service
Environment="PATH=/var/www/car_service/venv/bin"
ExecStart=/var/www/car_service/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/var/www/car_service/gunicorn.sock \
          autocheck_api.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
# Активувати сервіс
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

# Перевірити статус
sudo systemctl status gunicorn
```

### 3.5 Налаштування Nginx

Nginx — це reverse proxy перед Gunicorn.

```bash
# Створити конфіг
sudo vim /etc/nginx/sites-available/car_service
```

Вміст файлу:

```nginx
upstream gunicorn_app {
    server unix:/var/www/car_service/gunicorn.sock fail_timeout=0;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    # Редирект на HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    # SSL сертифікат (Let's Encrypt)
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    client_max_body_size 20M;

    location /static/ {
        alias /var/www/car_service/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /media/ {
        alias /var/www/car_service/media/;
    }

    location / {
        proxy_pass http://gunicorn_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }
}
```

```bash
# Активувати сайт
sudo ln -s /etc/nginx/sites-available/car_service /etc/nginx/sites-enabled/

# Перевірити конфіг
sudo nginx -t

# Перезавантажити Nginx
sudo systemctl restart nginx
```

### 3.6 SSL сертифікат (Let's Encrypt)

```bash
# Встановити Certbot
sudo apt install certbot python3-certbot-nginx

# Отримати сертифікат
sudo certbot certonly --nginx -d yourdomain.com -d www.yourdomain.com

# Автоматичне поновлення
sudo systemctl enable certbot.timer
sudo systemctl start certbot.timer
```

### 3.7 Supervisor для контролю процесів

Supervisor забезпечує, що Gunicorn завжди запущений.

```bash
# Встановити
sudo apt install supervisor

# Створити конфіг
sudo vim /etc/supervisor/conf.d/car_service.conf
```

Вміст:

```ini
[program:car_service]
directory=/var/www/car_service
command=/var/www/car_service/venv/bin/gunicorn \
         --workers 3 \
         --bind unix:/var/www/car_service/gunicorn.sock \
         autocheck_api.wsgi:application
autostart=true
autorestart=true
user=ubuntu
stopasgroup=true
stopwaitsecs=10
stdout_logfile=/var/log/supervisor/car_service.log
stderr_logfile=/var/log/supervisor/car_service.log
```

```bash
# Активувати
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start car_service

# Перевірити
sudo supervisorctl status
```

## 4. Розгортання через Docker (сучасний спосіб)

### 4.1 Dockerfile

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Встановити залежності
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Копіювати requirements
COPY requirements.txt .

# Встановити Python залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіювати код
COPY . .

# Зібрати static файли
RUN python manage.py collectstatic --noinput

# Expose порт
EXPOSE 8000

# Команда запуску
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "autocheck_api.wsgi:application"]
```

### 4.2 Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: car_service_db
      POSTGRES_USER: car_user
      POSTGRES_PASSWORD: secure_password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web:
    build: .
    command: >
      sh -c "python manage.py migrate &&
             gunicorn --bind 0.0.0.0:8000 autocheck_api.wsgi:application"
    environment:
      DEBUG: "False"
      SECRET_KEY: your-secret-key
      DB_NAME: car_service_db
      DB_USER: car_user
      DB_PASSWORD: secure_password
      DB_HOST: db
      DB_PORT: 5432
    ports:
      - "8000:8000"
    depends_on:
      - db
    volumes:
      - static_volume:/app/staticfiles
      - media_volume:/app/media

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
  media_volume:
```

### 4.3 Запуск Docker

```bash
# Побудувати образи
docker-compose build

# Запустити контейнери
docker-compose up -d

# Переглянути логи
docker-compose logs -f web

# Зупинити
docker-compose down
```

## 5. CI/CD Pipeline з GitHub Actions

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Deploy to server
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.HOST }}
        username: ${{ secrets.USERNAME }}
        key: ${{ secrets.SSH_KEY }}
        script: |
          cd /var/www/car_service
          git pull origin main
          source venv/bin/activate
          pip install -r requirements.txt
          python manage.py migrate
          python manage.py collectstatic --noinput
          sudo systemctl restart gunicorn
```

## 6. Моніторинг та обслуговування

### 6.1 Логування

```bash
# Переглянути логи Nginx
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# Переглянути логи Gunicorn
sudo journalctl -u gunicorn -f

# Переглянути логи Django
tail -f /var/log/django/debug.log
```

### 6.2 Резервне копіювання БД

```bash
# Резервна копія PostgreSQL
sudo -u postgres pg_dump car_service_db > backup.sql

# Відновлення з резервної копії
sudo -u postgres psql car_service_db < backup.sql

# Автоматичне резервне копіювання (cron)
# Додати до crontab:
0 2 * * * /usr/bin/pg_dump -U car_user car_service_db > /backups/car_service_$(date +\%Y\%m\%d).sql
```

### 6.3 Моніторинг серверу

```bash
# Встановити監視інструменти
sudo apt install htop glances

# Перевірити вільне місце
df -h

# Перевірити пам'ять
free -h

# Перевірити навантаження CPU
top
```

## 7. Чек-лист для production deployment

- [ ] SECRET_KEY змінено
- [ ] DEBUG = False
- [ ] ALLOWED_HOSTS налаштовано
- [ ] HTTPS включено (SSL сертифікат)
- [ ] БД налаштована (PostgreSQL)
- [ ] Static файли зібрані
- [ ] Migrations застосовано
- [ ] Суперкористувач створено
- [ ] Gunicorn/Nginx налаштовано
- [ ] Supervisor налаштовано
- [ ] Email налаштовано
- [ ] Логування налаштовано
- [ ] Резервне копіювання налаштовано
- [ ] Моніторинг налаштовано
- [ ] Firewall налаштовано
- [ ] SSH ключі налаштовано

## Домашнє завдання

1. Підготуйте `.env` для production
2. Розгортайте на Heroku або DigitalOcean
3. Налаштуйте SSL сертифікат
4. Налаштуйте моніторинг та логування
5. Автоматизуйте розгортання через Git

## Посилання

- [Django Deployment](https://docs.djangoproject.com/en/stable/howto/deployment/)
- [Gunicorn](https://gunicorn.org/)
- [Nginx](https://nginx.org/)
- [Docker](https://www.docker.com/)
- [Let's Encrypt](https://letsencrypt.org/)
- [DigitalOcean Tutorials](https://www.digitalocean.com/community/tutorials)
