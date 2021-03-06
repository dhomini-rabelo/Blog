from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework import  status
from django.core.cache import cache
from Support.Code.actions.Support.utils.main import gets
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class SearchApiView(APIView):
    
    @method_decorator(cache_page(60 * 5))
    def get(self, request):
        search_api_data: dict = cache.get('search_api')
        return Response(search_api_data)
    
    def post(self, request):
        if 'search' not in request.data.keys(): 
            return Response({'error': 'invalid body'}, status=status.HTTP_400_BAD_REQUEST)
        
        search: str = request.data['search']
        
        searches: dict = cache.get('searches')
        
        if search.lower() in searches.keys():
            return Response(searches[search])
        
        search_api_data: dict = cache.get('search_api')
        
        posts, categories, authors, subcategories = gets(search_api_data, 'posts', 'categories', 'authors', 'subcategories', obj_filter='none')
        
        do_search = lambda item: search.lower() in item['title'].lower()
        
        
        response = { 
                
            'posts': list(filter(do_search, posts[:])), 
            'categories': list(filter(do_search, categories[:])),
            'subcategories': list(filter(do_search, subcategories[:])),
            'authors': list(filter(do_search, authors[:])),
            
        }
        
        cache.set('searches', {**searches, search.lower(): response}, None)
        
        return Response(response)
