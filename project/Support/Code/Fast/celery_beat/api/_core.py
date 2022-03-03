from .search import create_search_api_data
from .post import create_post_api_data


def create_api_data(context):
    create_search_api_data(context)
    create_post_api_data(context)