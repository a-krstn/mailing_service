from .base import *

DEBUG = False
ADMINS = [
    ('Admin', os.getenv('EMAIL_HOST_USER')),
]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': 5432,
    }
}

# redis settings
REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 0

# celery settings
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + str(REDIS_PORT) + '/0'
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + str(REDIS_PORT) + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_ACCEPT_BACKEND = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'