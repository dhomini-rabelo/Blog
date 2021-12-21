from django.test import TestCase, Client
from Support.Code.actions._accounts.support.login import construct_form




class LoginBackEndTest(TestCase):

    def setUp(self):
        self.client = Client()

    #* TESTS FOR GET METHOD
    
    def test_status_code(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_form_rendering(self):
        response = self.client.get('/login')
        self.assertIn(construct_form().form, response.content)

    



