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
        
        search_api_data: dict = cache.get('search_api')
        
        if search in search_api_data['searches'].keys():
            return Response(search_api_data['searches'][search])
        
        posts, categories, authors = gets(search_api_data, 'posts', 'categories', 'authors')
        
        filter(lambda item: search in item.title, posts)
        filter(lambda item: search in item.name, categories)
        filter(lambda item: search in item.name, authors)
        
        response = { 
                
            'posts': posts, 
            'categories': categories,
            'authors': authors,
            
        }
        
        cache.set('search_api', {
            
            **search_api_data, 
            
            'searches': {
                **search_api_data['searches'], 
                request.data['search']: response
            }
            
        })
        
        return Response(response)
