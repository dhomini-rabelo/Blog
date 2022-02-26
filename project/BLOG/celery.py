from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from django.core.cache import cache

# print('oi 1')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BLOG.settings")

# print('oi 2')
app = Celery("BLOG.celery")

# print('oi 3')
app.config_from_object("django.conf:settings", namespace="CELERY")

# print('oi 4')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
    
#     sender.add_periodic_task(60.0, test.s(), name='celery every 10')
    

# @app.task(name='Celery beat test')
# def test():
#     cache.set_many({'title': 'Arroz de  Título', 'author': 'Dhomini Rabelo'})
#     return {'process': 'success'}


# if __name__ == '__main__':
#     test.delay()