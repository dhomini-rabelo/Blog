from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from celery_beat.SPGT._core import create_static_pages, update_static_pages
from celery_beat.api import create_search_api_data, updated_search_api_data
from celery_beat.base import create_cache_initial_data


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BLOG.settings")

app = Celery("BLOG.celery")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute='*/15'),
        celery_update_project_data.s(),
    )
    

@app.task(name='Create base for project')
def create_base():
    create_cache_initial_data()
    create_search_api_data()
    create_static_pages()
    return {'status': 'success'}


@app.task(name='Update data for project')
def celery_update_project_data():
    updated_search_api_data()
    update_static_pages()
    return {'status': 'success'}


if __name__ == '__main__':
    create_base.delay()