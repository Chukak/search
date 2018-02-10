# Search
# Introduction
Simple search example with several filters.

## Documentation
[Русский ](https://github.com/Chukak/search/blob/master/readme_ru.md)

## Download
Clone this repos

``` git clone https://github.com/Chukak/search.git ```

## Requirements
In project is used Django 1.11, Mysql 5.7+, Channels 2+. For Channels 2.0 you need python 3.5+.

### Create venv

Create python 3.3+ environment 

#### Ubuntu/Debian

``` sudo apt-get isntall python3-venv ```

``` python3 -m venv venv ```

``` . venv/bin/activate ``` 

Or use other envs.

### Set requirements
Go to project dir and run command

``` pip install -r requirements.txt ```


## Started
### Set migrations django
``` python manage.py makemigrations ```

``` python manage.py migrate ```

### Set data 
If you use Mysql 5.7+, you need mysql.data file. File is in project. In Mysql:

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
