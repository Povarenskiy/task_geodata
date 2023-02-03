# Отображение границ участка на карте по кадастровому номеру

Разработан на Python 3.10.

Зависимости:
* Django==4.1.6
* folium==0.14.0
* rosreestr2coord==4.1.6

Пример работы сайта:
![Image alt](https://github.com/Povarenskiy/task_geodata/blob/main/result.png)

# Установка и запуск

1. Клонировать репозиторий с Github.com:
````
git clone https://github.com/Povarenskiy/task_geodata.git
````
2. В директории проекта создать виртуальное окружение (venv/ — название виртуального окружения)
````
python -m venv venv
````
3. Активировать виртуальное окружение 
````
venv\Scripts\activate.bat - для Windows
source venv/bin/activate - для Linux и MacOS
````
4. Установка зависимостей
````
pip install -r requirements.txt
````
5. Запустить сервер
````
python manage.py runserver
````
6. В браузере перейти на 
````
http://127.0.0.1:8000/
````


