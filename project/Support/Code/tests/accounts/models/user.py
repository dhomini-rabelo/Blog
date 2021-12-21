from .size_user import UserStringSizeTest
from .unique_user import UserUniqueFieldsTest
from django.test import TestCase
from accounts.models import User
from posts.models import Post
from Support.Code.actions.Support.for_fields import set_slug
from unittest import expectedFailure



class UserTest(TestCase, UserUniqueFieldsTest):

    def setUp(self):
        self.user = User(
            username='test@test.com', name='name_test',
            email='test@test.com', slug=set_slug('name_test')
        )
        self.user.set_password('12345678')
        self.user.save()

    def test_default_fields(self):
        self.assertEqual(self.user.username, 'test@test.com')
        self.assertEqual(self.user.email, 'test@test.com')
        self.assertEqual(self.user.name, 'name_test')
        self.assertEqual(self.user.slug, 'name-test')

    def test_changes(self):
        self.user.username = 'new_test@test.com'
        self.user.email = 'new_test@test.com'
        self.user.name = 'new_name_test'
        self.user.slug = 'new-name-test'
        self.user.save()
        self.assertEqual(self.user.username, 'new_test@test.com')
        self.assertEqual(self.user.email, 'new_test@test.com')
        self.assertEqual(self.user.name, 'new_name_test')
        self.assertEqual(self.user.slug, 'new-name-test')

    def test_verbose_name(self):
        model = self.user._meta
        self.assertEqual(model.get_field('username').verbose_name, 'usuário')
        self.assertEqual(model.get_field('email').verbose_name, 'endereço de email')
        self.assertEqual(model.get_field('name').verbose_name, 'Nome')
        self.assertEqual(model.get_field('slug').verbose_name, 'Slug')
       
    def test_str_method(self):
        self.assertEqual(str(self.user), self.user.username)

    def tearDown(self):
        self.assertTrue(isinstance(self.user.username, str))
        self.assertTrue(isinstance(self.user.email, str))
        self.assertTrue(isinstance(self.user.name, str))
        self.assertTrue(isinstance(self.user.slug, str))

