from accounts.models import User
from unittest import expectedFailure


class UserUniqueFieldsTest:

    @expectedFailure
    def test_username_unique(self):
        user_for_test_1 = User.objects.create(username='test_unique')
        user_for_test_2 = User.objects.create(username='test_unique')