from abc import ABC

class AppModels(ABC):

    def import_for_model(self):
        current_import = 'from django.db import models'
        new_import = 'from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)'
        self.models.replace_line(current_import, new_import) # new_reading
        self.response(f'import do model foi editado')
        
    
    
    def create_abstract_user_model(self):
        imports =  [
            "from django.contrib.auth.models import AbstractUser", "from django.utils.safestring import mark_safe",
            "from django.utils import timezone"
        ]
        abstract_user_class = [
            '\n\nclass User(AbstractUser):', 
            *self.spaces([
                "photo = ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True, default='images/user.jpg')",
                "def __str__(self):",
                *self.spaces([
                    "return self.username\n",         
                ], 8),
                "@mark_safe",
                "def icon(self):",
                *self.spaces([
                    """return f'<a href="/media/{self.photo}" target="_blank"><img src="/media/{self.photo}" style="width: 35px; height: 25px;"></a>""",         
                ], 8),                
            ], 4),
        ]
        self.models.add_in_start(imports)
        self.models.add_in_end(abstract_user_class)
        self.response('Criado modelo padrão de usuário')

                