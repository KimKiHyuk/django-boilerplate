from .base import *

DEBUG=True
HOST = "http://127.0.0.1:8000"
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'), # dbname
        'USER': os.getenv('MYSQL_ID'), # master username
        'PASSWORD': os.getenv('MYSQL_PW'), # master password
        'HOST': os.getenv('MYSQL_IP'), # Endpoint
        'PORT': os.getenv('MYSQL_PORT'),
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}
