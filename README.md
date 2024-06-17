# Парсер отзывов Yelp

Это предварительный проект парсера отзывов с сайта `yelp.com`. Проект реальзован с помощью библиотеки scrapy.

## Инструкция к запуску парсера

## 1. Установка зависимосте проекта

Создайте виртуально окружение с помощью команды:

```commandline
python -m venv .venv
```

Активируйте виртуальное окружение с помощью команд:

- Для операционной системы Windows

```commandline
venv/Scripts/activate.bat
```

- Для операционной системы Linux

```commandline
source venv/bin/activate
```

Для установки зависимостей проекта выполните следующую команду:

```commandline
pip install -r requirements.txt
```

## 2. Настройка переменных окружения

Для работы с перменными необходимо будет создать файл `.env` с вашими данными для использования БД. Данные для
определения указаны в файле `example.env`.

## 3. Экспорт данных в JSON или CSV

Scrapy имеет встроенные форматы экспорта, такие как JSON и CSV. Для извлечения данных в формат JSON необходимо ввести
команду

```commandline
scrapy crawl scraper -O filename.json
```

и

```commandline
scrapy crawl scraper -O filename.csv
```

Для импорта данных в CSV файл. filename в данном случае - название вашего файла.