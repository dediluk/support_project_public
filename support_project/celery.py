from __future__ import absolute_import
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'support_project.settings')

app = Celery('support_project')
app.conf.enable_utc = False
app.conf.update(timezone='Europe/Moscow')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request}')
