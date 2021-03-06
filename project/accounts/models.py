from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, SlugField, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, JSONField)



class User(AbstractUser):
    name = CharField(max_length=256, blank=True, null=True, verbose_name='Nome')
    slug = SlugField(max_length=256, blank=True, null=True, verbose_name='Slug')
    photo = ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True, verbose_name='Foto')
    my_static_pages = JSONField(blank=True, null=True)

    def __str__(self):
        return self.username

    @mark_safe
    def icon(self):
        return f'<a href="/media/{self.photo}" target="_blank"><img src="/media/{self.photo}" style="width: 35px; height: 25px;"></a>'

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
