from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework import  status
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator





class PostApi(APIView):
    
    @method_decorator(cache_page(60 * 10))
    def get(self, request, code):
        data = cache.get('posts_api')
        post = data.get(str(code))
        if post is None: return Response({'error': 'invalid body'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(post, status=status.HTTP_200_OK)
    



class PostsListBySubcategoryApi(APIView):
    
    @method_decorator(cache_page(60 * 10))
    def get(self, request, subcategory_slug):
        data = cache.get('cache_page__subcategories')
        posts = data.get(str(subcategory_slug))
        if posts is None: return Response({'error': 'invalid body'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(posts, status=status.HTTP_200_OK)




class PostsListByAuthorApi(APIView):
    
    @method_decorator(cache_page(60 * 10))
    def get(self, request, author_slug):
        data = cache.get('cache_page__authors')
        posts = data.get(str(author_slug))
        if posts is None: return Response({'error': 'invalid body'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(posts, status=status.HTTP_200_OK)