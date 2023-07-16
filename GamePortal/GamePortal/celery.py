import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GamePortal.settings')

app = Celery('GamePortal')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_email_monday': {
        'task': 'posts.tasks.weekly_notify',
        'schedule': crontab(hour = 8, minute = 0, day_of_week = 'monday'),
    }
}