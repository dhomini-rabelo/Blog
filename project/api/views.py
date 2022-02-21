from django.shortcuts import render, redirect
from Support.Code.actions._accounts.login_group.login import get_token_for_user
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from accounts.models import User
from rest_framework.response import  Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework import  status
from suggestions.models import CategorySuggestion, SubCategorySuggestion
from .serializers import CategorySuggestionSerializer, SubCategorySuggestionSerializer
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated



class CategorySuggestionView(APIView):
    permission_classes = IsAuthenticated,
    
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
    

@login_required
def get_cookie(request):
    if request.method == 'GET':
        response = redirect(request.GET.get('latest_url'))
        token = get_token_for_user(request)
        response.set_cookie('access_token', token['access'], max_age=60*60*24*3)
        response.set_cookie('refresh_token', token['refresh'], max_age=60*60*24*365)
        response.set_cookie('email', request.session['user_save']['email'], max_age=60*60*24*365)
        return response
    raise Http404



    
def email_view(request):
    send_mail('Sou o assunto', 'Sou a mensagem', 'from_mail', ['to_mail'])
    return HttpResponse('<h2>OI</h2>')