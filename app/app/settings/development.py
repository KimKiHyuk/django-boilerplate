from .base import *

DEBUG=True
HOST = "http://127.0.0.1:8000"
ALLOWED_HOSTS = ["*"]

# DB가 없는 경우(worker 모델) DB 초기화를 안해줌
if not os.getenv('NO_DB'):
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
