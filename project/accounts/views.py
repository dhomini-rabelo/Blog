from django.db.models import fields
from Support.Code.actions._accounts.register import get_register_form, validate_register_form, save_register_form_errors, create_user, save_register_form_fields_values, delete_register_form_fields_values
from Support.Code.actions._accounts.login import get_login_form
from django.shortcuts import render, redirect
from django.views.generic import View




class RegisterView(View):
    
    def get(self, request):
        context = {}
        context['form'] = get_register_form(request)
        return render(request, 'accounts/register.html', context)

    def post(self, request):
        validation = validate_register_form(request)
        if validation['status'] == 'valid':
            create_user(validation['fields'])
            delete_register_form_fields_values(request)
            return redirect('login')
        else:
            save_register_form_errors(request, validation['errors'])
            save_register_form_fields_values(request, validation['fields'])
            return redirect('register')




class LoginView(View):

    def get(self, request):
        context = {}
        context['form'] = get_login_form(request)
        return render(request, 'accounts/login.html', context)