from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings




os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BLOG.settings")

app = Celery("BLOG.celery")

app.config_from_object("django.conf:settings", namespace="CELERY")

CELERY_TASKS = settings.INSTALLED_APPS + [
    'accounts.tasks.email',
    'Support.Code.Fast.celery_beat._tasks',
]

app.autodiscover_tasks(lambda: CELERY_TASKS)



app.conf.beat_schedule = {

    'update_project_data': {
        'task': 'Update data for project',  
        'schedule': 50.0,
        'args': []
    },

}


    