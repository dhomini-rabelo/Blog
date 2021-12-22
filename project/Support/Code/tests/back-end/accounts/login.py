from django.test import TestCase, Client
from Support.Code.actions._accounts.support.login import construct_form
from accounts.models import User



class LoginBackEndTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.get_error = lambda message : f'<div class="error"><span class="error-message"><img src="/static/admin/img/icon-no.svg" alt="error-img">{message}</span></div>'
        self.user = User(
            username='email_for_test@test.com', email='email_for_test@test.com',
            name='test', slug='test'
        )
        self.user.set_password('password123')
        self.user.save()

    #* TESTS FOR GET METHOD
    
    def test_status_code_get_method(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_form_rendering(self):
        response = self.client.get('/login/')
        form_class = construct_form()
        response_html = response.content.decode('utf-8')
        self.assertIn(form_class.form, response_html)

    #* TESTS FOR POST METHOD

    def test_load_fields_value(self):
        data = {'email': 'test_email', 'password': 'test_password'}
        response = self.client.post('/login/', data, follow=True)
        form = response.context['form']
        inputs_with_value = ['test_email', 'test_password']
        for value_attr in inputs_with_value:
            self.assertIn(f'<input value="{value_attr}"', form)

    def test_none_fields_errors(self):
        data = {'email': '', 'password': ''}
        response = self.client.post('/login/', data, follow=True)
        form = response.context['form']
        error_div = self.get_error('Este campo é obrigatório')
        self.assertEqual(form.count(error_div), 2)

    def test_email_not_found_error(self):
        data = {'email': 'test_for_not_found@test.com', 'password': '1'}
        response = self.client.post('/login/', data, follow=True)
        form = response.context['form']
        error = self.get_error('Email não encontrado')
        self.assertIn(error, form)

    def test_incorrect_password_error(self):
        data = {'email': self.user.email, 'password': 'incorrect_password123'}
        response = self.client.post('/login/', data, follow=True)
        form = response.context['form']
        error = self.get_error('Senha incorreta')
        self.assertIn(error, form)

    def test_login(self):
        data = {'email': self.user.email, 'password': 'password123'}
        response = self.client.post('/login/', data, follow=True)
        self.assertEqual(response.request['PATH_INFO'], '/')


