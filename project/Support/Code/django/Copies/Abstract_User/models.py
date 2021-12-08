from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
from django.utils import timezone
from decimal import Decimal

class User(AbstractUser):
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        
    photo = ImageField('Foto de perfil', upload_to='images/%Y/%m/%d/%M/%f', null=True, blank=True, default='images/default.jpg')
    
    def __str__(self):
        return self.username

    @mark_safe
    def icon(self):
        return f'<a href="/media/{self.photo}" target="_blank"><img src="/media/{self.photo}" style="width: 35px; height: 25px;"></a>'
    
    def __dict__(self):
        fields_value = {'username': self.username, 'first_name': self.first_name,
                        'last_name': self.last_name, 'email': self.email}
    
