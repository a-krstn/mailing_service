from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += ['rest_framework.renderers.BrowsableAPIRenderer']

# redis settings
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

# celery settings
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + str(REDIS_PORT) + '/0'
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + str(REDIS_PORT) + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_ACCEPT_BACKEND = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'