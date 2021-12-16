from Support.Code.actions._accounts.register import get_register_form
from Support.Code.actions._accounts.login import get_login_form
from django.shortcuts import render
from django.views.generic import View




class RegisterView(View):
    
    def get(self, request):
        context = {}
        context['form'] = get_register_form(request)
        return render(request, 'accounts/register.html', context)





class LoginView(View):

    def get(self, request):
        context = {}
        context['form'] = get_login_form(request)
        return render(request, 'accounts/login.html', context)