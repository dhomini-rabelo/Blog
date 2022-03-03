from Support.Code.Fast.celery_beat.SPGT._core import create_static_pages, update_static_pages
from Support.Code.Fast.celery_beat.api import create_search_api_data, updated_search_api_data
from Support.Code.Fast.celery_beat.base import create_cache_initial_data, create_process_context
from celery.signals import celeryd_init
from celery import shared_task


@celeryd_init.connect
def create_base(sender, conf, **kwargs):
    context = create_process_context()
    create_cache_initial_data()
    create_search_api_data(context)
    create_static_pages(context)
    return {
        'actions': [
            'create initial cache',
            'create data for search api',
            'create data for static pages',
        ]
    }


@shared_task(name='Update data for project')
def celery_update_project_data():
    api_process = updated_search_api_data()
    static_pages_process = update_static_pages()
    
    return {
        'api': api_process,
        'static_pages': static_pages_process,
    }