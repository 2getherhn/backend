runserver:
	docker-compose up

build:
	docker-compose build

rsa_key:
	docker-compose exec together python manage.py creatersakey

migrate:
	docker-compose exec together python manage.py migrate

shell:
	docker-compose exec together python manage.py shell

down:
	docker-compose down