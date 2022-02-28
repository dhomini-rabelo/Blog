from accounts.models import User
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework import  status
from suggestions.models import CategorySuggestion, SubCategorySuggestion
from ..serializers import CategorySuggestionSerializer, SubCategorySuggestionSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated



class CategorySuggestionView(APIView):
    permission_classes = IsAuthenticated,
    
    @method_decorator(cache_page(60*5))
    def get(self, request):
        suggestions = CategorySuggestion.objects.all()
        serializer = CategorySuggestionSerializer(suggestions, many=True)
        return Response(serializer.data)

    def post(self, request):
        if 'email' not in request.data.keys() and 'name' not in request.data.keys(): 
            return Response({'error': 'invalid body'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(email=request.data['email']).first()
        if user is None:
            return Response({'error': 'user not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CategorySuggestionSerializer(data={'name': request.data['name'], 'state': 'loading', 'user': user.id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'invalid data'}, status=status.HTTP_400_BAD_REQUEST)



class SubCategorySuggestionView(APIView):
    permission_classes = IsAuthenticated,
    
    @method_decorator(cache_page(60*5))
    def get(self, request):
        suggestions = SubCategorySuggestion.objects.all()
        serializer = SubCategorySuggestionSerializer(suggestions, many=True)
        return Response(serializer.data)

    def post(self, request):
        if 'email' not in request.data.keys() and 'name' not in request.data.keys(): 
            return Response({'error': 'invalid body'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(email=request.data['email']).first()
        if user is None:
            return Response({'error': 'user not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SubCategorySuggestionSerializer(data={'name': request.data['name'], 'state': 'loading', 'user': user.id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    
