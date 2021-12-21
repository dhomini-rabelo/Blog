from unittest import expectedFailure


class UserStringSizeTest:

    @expectedFailure
    def test_username_size(self):
        # error because "max_length" was outdated
        self.user.username = 'x' * 160
        self.user.save()

    @expectedFailure
    def test_name_size(self):
        self.user.name = 'x' * 260
        self.user.save()

    @expectedFailure
    def test_slug_size(self):
        self.user.slug = 'x' * 260
        self.user.save()
