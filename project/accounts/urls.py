from django.urls import path
from .views import *


# contas/
urlpatterns = [
    path('cadastro/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('minha-conta/', AccountView.as_view(), name='accounts_page'),
]
