![django CI](https://github.com/KimKiHyuk/django-boilerplate/workflows/django%20CI/badge.svg?branch=main)
# django-boilerplate
Django backend boilerplate

## Features
* Swagger
* API Sample (health check)
* dev mysql database (docker-compose)

## Development 

```
$ python3 -m venv venv
$ docker-compose up -d   
$app python manage.py makemigrations --settings=app.settings.development
$app python manage.py migrate --settings=app.settings.development
$app python manage.py runserver --settings=app.settings.development
```


## Deployment (Zappa, AWS)
* $app export $(grep -v '^#' .<enviroment>.env | xargs)
* $app envsubst < zappa_settings.json.tpl > zappa_settings.json
```json
{
    "dev": {
        "django_settings": "$SETTINGS",
        "profile_name": "$AWS_PROFILE",
        "project_name": "django-zappa-template",
        "runtime": "python3.6",
        "s3_bucket": "$BUCKET_NAME",
        "aws_region": "$REGION",
    }
}
```
* zappa deploy <stage>