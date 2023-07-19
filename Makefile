makemigrate:
	python manage.py makemigrations

migrate:
	python manage.py migrate

run:
	python manage.py runserver

createsuperuser:
	python manage.py createsuperuser

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt