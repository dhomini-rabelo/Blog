import io

try:
    from Support.Code.Fast.celery_beat.SPGT._core import create_static_pages, update_static_pages
    from Support.Code.Fast.celery_beat.api._core import create_api_data, update_api_data
    from Support.Code.Fast.celery_beat.cache_pages._core import create_cache_pages, update_cache_pages
    from Support.Code.Fast.celery_beat.base import create_cache_initial_data, create_process_context, update_process_context
    from celery.signals import celeryd_init
    from celery import shared_task
except ImportError as e:
    with io.open('./error.txt', 'w') as file:
        file.write(str(e))


@celeryd_init.connect
def create_base(sender, conf, **kwargs):
    context = create_process_context()
    create_cache_initial_data()
    create_api_data(context)
    create_static_pages(context)
    create_cache_pages(context)
    return {
        'actions': [
            'create initial cache',
            'create data for api',
            'create data for static pages',
            'create data for cache pages',
        ]
    }


@shared_task(name='Update data for project')
def celery_update_project_data():
    context, update_obj = update_process_context()
    
    if context != {}:
        update_api_data(context, update_obj)
        update_cache_pages(context, update_obj)
        static_pages_process = update_static_pages(context, update_obj)
        create_cache_initial_data()
        return {
            'update': update_obj,
            'static_pages_report': static_pages_process,
        }

    return {
        'proccess': 'update data verify',
        'response': 'no changes'
    }