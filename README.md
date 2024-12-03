# Django-vuejs-test

# Django Backend + DRF + Vue Frontend

Этот проект объединяет Django для бэкенда и Vue.js для фронтенда. Все компоненты приложения контейнеризованы с использованием Docker Compose. Ниже представлены инструкции по настройке и запуску проекта.

## Зависимости

Для работы с проектом необходимы следующие зависимости:

- **[Docker](https://www.docker.com/get-started)** для контейнеризации приложения
- **[Docker Compose](https://docs.docker.com/compose/install/)** для управления многоконтейнерными приложениями
- **[GNU Make](https://www.gnu.org/software/make/)** для автоматизации команд 
  (опционально)


Убедитесь, что Docker и Docker Compose установлены на вашем компьютере:

```bash
    docker --version
```
```bash
    docker-compose --version
```

## Установка и запуск

Сначала клонируйте проект с GitHub и перейдите в папку проекта:  
```bash
  git clone https://github.com/novozhilov-ivan/parity-django-vuejs-test.git
```
```bash
  cd parity-django-vuejs-test
```

## Подготовка перед запуском
Перед запуском проекта необходимо настроить файл окружения .env. Для этого выполните следующие шаги:

**Убедитесь, что в корне проекта находится файл .env.example.**

Выполните одно из следующих действий:
Создайте новый файл .env и скопируйте в него содержимое из .env.example. Затем настройте значения переменных, если это необходимо.
Либо просто переименуйте файл .env.example в .env, чтобы использовать значения по умолчанию.
Пример команды для переименования файла в терминале (Linux/MacOS):

```bash
  cat .env.example > .env
```
После этого ваш проект будет использовать переменные окружения из файла .env.


### Запуск с использованием GNU Make (рекомендуется)

1. **Сборка и запуск контейнеров**  
   Выполните следующую команду, чтобы собрать и запустить контейнеры:  
```bash
  make up-all
```
2.  **Применение миграций базы данных**  
```bash
  make migrate
```
3.  **Доступ к приложению**  
Откройте браузер и перейдите по адресу:
http://localhost:8080

### Запуск с использованием только Docker Compose

1. **Сборка контейнеров**  
```bash
  docker compose -f frontend.yml -f app.yml -f postgres.yml build
```
2.  **Запуск контейнеров**  
```bash
  docker compose -f frontend.yml -f app.yml -f postgres.yml up -d
```
3. **Применение миграций базы данных**  
```bash
  docker exec -it images-app python manage.py migrate
```
4. **Доступ к приложению**  
Откройте браузер и перейдите по адресу:
http://localhost:8080
