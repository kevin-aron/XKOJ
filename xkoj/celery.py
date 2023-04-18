from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xkoj.settings')

backend = 'redis://8.130.110.219:6379/1'
broker = 'redis://8.130.110.219:6379/2'

app = Celery('xkoj', backend=backend, broker=broker)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)