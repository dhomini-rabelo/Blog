from django.urls import path
from .views import *


# contas/
urlpatterns = [
    path('cadastro/', RegisterView.as_view(), 'register'),
    path('login/', LoginView.as_view(), 'login'),
]
