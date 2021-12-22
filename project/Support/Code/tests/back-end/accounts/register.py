from django.test import TestCase, Client
from Support.Code.actions._accounts.support.register import construct_form
from Support.Code.actions.Support.messages import success_message
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
        response = self.client.get('/cadastro/')
        self.assertEqual(response.status_code, 200)

    def test_form_rendering(self):
        response = self.client.get('/cadastro/')
        form_class = construct_form()
        response_html = response.content.decode('utf-8')
        self.assertIn(form_class.form, response_html)

    #* TESTS FOR POST METHOD

    def test_javascript_use(self):
        data = {
            'name': 'test_name', 'email': 'a', 'password': 'password123',
            'confirm_password': 'pass'
        }
        response = self.client.post('/cadastro/', data, follow=True)
        self.assertEqual(response.client.session['not_use_javascript'], True)
        data['javascript'] = 'on'
        new_response = self.client.post('/cadastro/', data, follow=True)
        self.assertEqual(new_response.client.session['not_use_javascript'], False)

    def test_load_fields_value(self):
        data = {'name': 'test_name', 'email': 'a', 'password': 'password123', 'confirm_password': 'pass'}
        response = self.client.post('/cadastro/', data, follow=False)
        self.assertEqual(response.client.session['register_fields'], data)

    def test_none_fields_errors(self):
        data = {'name': '', 'email': '', 'password': '', 'confirm_password': ''}
        response = self.client.post('/cadastro/', data, follow=True)
        form = response.context['form']
        error_div = self.get_error('Este campo é obrigatório')
        self.assertEqual(form.count(error_div), 4)

    def test_max_length_error(self):
        data = {'name': 'x'*257, 'email': 'x'*129, 'password': 'x'*257, 'confirm_password': 'x'*257}
        response = self.client.post('/cadastro/', data, follow=True)
        form = response.context['form']
        error_256 = self.get_error('Este campo deve ter no máximo 256 dígitos')
        error_128 = self.get_error('Este campo deve ter no máximo 128 dígitos')
        self.assertEqual(form.count(error_256), 3)
        self.assertEqual(form.count(error_128), 1)

    def test_only_str_and_invalid_email_and_min_length_and_different_passwords_errors(self):
        data = {'name': 'Árroz@#', 'email': 'admin@test', 'password': 'x'*7, 'confirm_password': 'x'*6}
        response = self.client.post('/cadastro/', data, follow=True)
        form = response.context['form']
        error_only_str = self.get_error('Este campo aceita apenas letras')
        error_email = self.get_error('Email inválido')
        error_min_length = self.get_error('Este campo deve ter no mínimo 8 dígitos')
        error_different_passwords = self.get_error('As senhas são diferentes')
        self.assertIn(error_only_str, form)
        self.assertIn(error_email, form)
        self.assertIn(error_min_length, form)
        self.assertIn(error_different_passwords, form)

    def test_email_not_unique_error(self):
        data = {
            'name': 'Test', 'email': 'email_for_test@test.com',
            'password': 'password', 'confirm_password': 'pass'
        }
        response = self.client.post('/cadastro/', data, follow=True)
        form = response.context['form']
        error_email_not_unique = self.get_error('Email já está em uso')
        self.assertIn(error_email_not_unique, form)

    def test_register(self):
        data = {
            'name': 'Test Name', 'email': 'email@test.com',
            'password': 'password123', 'confirm_password': 'password123'
        }
        response = self.client.post('/cadastro/', data, follow=True)
        self.assertEqual(response.request['PATH_INFO'], '/login/')

        # test success message
        self.assertIn(success_message('Usuário criado com sucesso'), response.context['messages'])

    