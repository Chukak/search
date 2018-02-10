# Search
# Введение
Простой поиск с несколькими фильтрами

## Загрузка
Клонируйте репозиторий

``` git clone https://github.com/Chukak/search.git ```

## Требования
В проекте используется Django 1.11, Mysql 5.7+, Channels 2+. Для Channels 2+ вам нужен python 3.5+.

### Создайте виртуальное окружение venv

Создайте виртуальное окружение python 3.3+ 

#### Ubuntu/Debian

``` sudo apt-get isntall python3-venv ```

``` python3 -m venv venv ```

``` . venv/bin/activate ``` 

Или используйте другие окружения.

### Установка требований
Перейдите в папку проекта и запустите команду

``` pip install -r requirements.txt ```


## Запуск
### Миграции django
``` python manage.py makemigrations ```

``` python manage.py migrate ```

### Настройка данных 
Если вы используете Mysql 5.7+, вам нужен файл mysql.data. Файл есть в проекте. В Mysql:

``` 
LOAD DATA LOCAL INFILE 'your/path/to/project/mysql.data'
FIELDS TERMINATED BY '~~' LINES TERMINATED BY '\n' 
(title, author, text, rating, date_created);
```
### Запуск сервера
Запустите сервер django:

``` python manage.py runserver ```

и перейдите <strong>localhost:8000</strong>.


## Авторы
[Chukak](https://github.com/Chukak)
