![django CI](https://github.com/KimKiHyuk/django-boilerplate/workflows/django%20CI/badge.svg?branch=main)
# django-boilerplate
Django backend boilerplate

## Feature
* python 3
* Swagger
* API Sample (health check)
* dev mysql database (docker-compose)

## Development 

```
python3 -m venv venv
docker-compose up -d   
python app/manage.py makemigrations --settings=app.settings.debug
python app/manage.py migrate --settings=app.settings.debug
python manage.py runserver --settings=app.settings.debug
```


## Production (Zappa, AWS)

* fill zappa.settings.json
* run all command using --settings=app.settings.prod
