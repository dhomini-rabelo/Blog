from .search import create_search_api_data, update_search_api_data
from .post import create_post_api_data
from .author import create_author_api_data
from .subcategory import create_subcategory_api_data


def create_api_data(context):
    create_search_api_data(context)
    create_post_api_data(context)
    create_author_api_data(context)
    create_subcategory_api_data(context)


def update_api_data(context, update_obj):
    update_search_api_data(context, update_obj)
    for key in update_obj.keys():
        update_api(key, context)

    

def update_api(key, context):
    match key:
        case 'posts':
            create_post_api_data(context)
        case 'authors':
            create_author_api_data(context)
        case 'subcategories':
            create_subcategory_api_data(context)