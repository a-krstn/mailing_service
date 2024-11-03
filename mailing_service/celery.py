import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailing_service.settings.local')

app = Celery('mailing')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'Europe/Moscow'
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-mailings-every-minute': {
        'task': 'mailing.tasks.check_and_start_mailings',
        'schedule': crontab(),
    },
}