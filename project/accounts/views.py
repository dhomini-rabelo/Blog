from Support.Code.actions._accounts.register import get_register_form_class
from django.shortcuts import render
from django.views.generic import View




class RegisterView(View):
    
    def get(self, request):
        context = {}
        form_class = get_register_form_class()
        context['form'] = form_class.get_form()

        return render(request, 'accounts/register.html', context)



 
class LoginView(View):

    def get(self, request):
        return render(request, 'accounts/login.html', {})