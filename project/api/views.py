from django.shortcuts import render
from rest_framework.response import  Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework import  status
from suggestions.models import CategorySuggestion, SubCategorySuggestion
from .serializers import CategorySuggestionSerializer, SubCategorySuggestionSerializer



class CategorySuggestionView(APIView):
    
    def get(self, request, user_id):
        suggestions = CategorySuggestion.objects.filter(user__id=user_id)
        serializer = CategorySuggestionSerializer(suggestions, many=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        serializer = CategorySuggestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SubCategorySuggestionView(APIView):
    
    def get(self, request, user_id):
        suggestions = SubCategorySuggestion.objects.filter(user__id=user_id)
        serializer = SubCategorySuggestionSerializer(suggestions, many=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        serializer = SubCategorySuggestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)