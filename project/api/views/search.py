from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework import  status
from django.core.cache import cache
from Support.Code.actions.Support.utils.main import gets



class SearchApiView(APIView):
    
    def get(self, request):
        search_api_data: dict = cache.get('search_api')
        return Response(search_api_data)
    
    def post(self, request):
        if 'search' not in request.data.keys(): 
            return Response({'error': 'invalid body'}, status=status.HTTP_400_BAD_REQUEST)
        
        search = request.data['search']
        
        check_cache = cache.get(f'search_{search}')
        
        if check_cache is not None:
            return Response(check_cache)
        
        search_api_data: dict = cache.get('search_api')
        
        posts, categories, authors, subcategories = gets(search_api_data, 'posts', 'categories', 'authors', 'subcategories')
        
        do_search = lambda item: search.lower() in item.lower()
        
        
        response = { 
                
            'posts': list(filter(do_search, posts[:])), 
            'categories': list(filter(do_search, categories[:])),
            'subcategories': list(filter(do_search, subcategories[:])),
            'authors': list(filter(do_search, authors[:])),
            
        }
        
        cache.set(f'search_{search}', response, 60*10)
        
        return Response(response)
