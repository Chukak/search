# Search
# Introduction
A simple search with some filters.

## Documentation
[Русский ](https://github.com/Chukak/search/blob/master/readme_ru.md)

## Download
Clone this repository.

``` git clone https://github.com/Chukak/search.git ```

## Getting started
In project is used Django 1.11, Mysql 5.7+, Channels 2+. For Channels 2.0 you need python 3.5+.

### Create virtual environment

Create python 3.3+ environment 

#### Ubuntu/Debian

``` sudo apt-get isntall python3-venv ```

``` python3 -m venv venv ```

``` . venv/bin/activate ``` 

Or use other envs.

### Requirements
Run the command:

``` pip install -r requirements.txt ```


## Started
### Database
If you use Mysql 5.7+, create a database. In Mysql:

``` CREATE DATABASE search; ```

Create the `mysql.cnf` file. In `mysql.cnf`:

``` 
[client]
database = search
user = your username
password = your password
default-character-set = utf8
```

In your django configuration file:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'mysql.cnf'),
        }
    }
}
```

### Set migrations django
``` python manage.py makemigrations ```

``` python manage.py migrate ```

### Set data 
If you use Mysql 5.7+, you need the `mysql.data` file. The file is in the project. In Mysql:

``` 
LOAD DATA LOCAL INFILE 'your/path/to/project/mysql.data'
FIELDS TERMINATED BY '~~' LINES TERMINATED BY '\n' 
(title, author, text, rating, date_created);
```
### Run server
Run django server:

``` python manage.py runserver ```

and go to <strong>localhost:8000</strong>.


## Authors 
[Chukak](https://github.com/Chukak)
