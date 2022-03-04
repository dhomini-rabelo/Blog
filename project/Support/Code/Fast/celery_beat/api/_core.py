from .search import create_search_api_data
from .post import create_post_api_data
from .author import create_author_api_data
from .subcategory import create_subcategory_api_data


def create_api_data(context):
    create_search_api_data(context)
    create_post_api_data(context)
    create_author_api_data(context)
    create_subcategory_api_data(context)