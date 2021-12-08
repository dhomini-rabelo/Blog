from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)



class User(AbstractUser):
    name = CharField(max_length=256, null=True, blank=True)
    photo = ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.username

    @mark_safe
    def icon(self):
        return f'<a href="/media/{self.photo}" target="_blank"><img src="/media/{self.photo}" style="width: 35px; height: 25px;"></a>'
