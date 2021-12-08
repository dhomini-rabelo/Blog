from .django_class import Base
from .editor import Editor
from pathlib import Path
from time import sleep
from .support import *
import io


class DjangoProject(Base):
    def __init__(self, base_path: str, project: str):
        self.base_path = self.adapt_path(base_path)
        self.project = self.adapt_path(project)
        self.path = f'{self.base_path}/{self.project}'
        assert_folder_existence(self.path)
            
    def adapt_urls_py(self):
        editor = Editor(self.path, 'urls.py')
        imports = ['from django.conf import settings', 'from django.conf.urls.static import static']
        editor.insert_code('from django.urls', imports)  # new_reading
        url_conf = ['urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)', 'urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)']
        editor.insert_code(']\n', url_conf)
        editor.add_in_line('from django.urls', ', include')
        response('arquivo urls.py criado com sucesso')
    
    def insert_important_comments(self):
        editor = Editor(self.path, 'settings.py')
        inserts = [("DEFAULT_AUTO_FIELD", "\n\n# My configurations"),
                   ("INSTALLED_APPS", f'{sp(4)}# Django apps'),
                   ("    'django.contrib.staticfiles'", f'{sp(4)}# My apps\n{sp(4)}# Others apps'),
        ]
        for current, new in inserts:
            editor.insert_code(current, new)
        response('Inserindo comentários importantes')
        
    def _settings_replaces(self):
        replaces = [
            (f"{sp(8)}'DIRS': [],", f"{sp(8)}'DIRS': [Path(BASE_DIR, 'Support/Layout/Templates')],"),
            ("LANGUAGE_CODE = 'en-us'", "LANGUAGE_CODE = 'pt-br'"),
            ("TIME_ZONE = 'UTC'", "TIME_ZONE = 'America/Sao_Paulo'"),
            (f"{sp(12)}],", f"{sp(12)}],\n{sp(12)}'libraries':"+" {\n"+ f"{sp(12)}'filters': 'Support.code.TemplatesTags.basic',\n{sp(12)}"+"}\n"),
            #("", ""),
        ]
        return replaces
        
    def _settings_inserts(self):
        settings = [
            "\nSTATICFILES_DIRS = [Path(BASE_DIR, 'Support/Layouts/Static')]", 
            "STATIC_ROOT = Path('static')","MEDIA_ROOT = Path(BASE_DIR,'Support/Layout/Media')", 
            "MEDIA_URL = '/media/'", "MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'", "SESSION_COOKIE_AGE = 60*60*24*7", "ACCOUNT_SESSION_REMEMBER = True", "ACCOUNT_UNIQUE_EMAIL = True"
        ]
        inserts = [
            ("# My configurations", settings),
            #("", ""),
        ]
        return inserts
    
    def adapt_settings(self):
        editor = Editor(self.path, 'settings.py')
        replaces = self._settings_replaces()
        inserts = self._settings_inserts()
        
        for current, new in replaces:
            editor.replace_line(current, new)

        for current, new in inserts:
            editor.insert_code(current, new)
            
        response('Colocando configurações básicas e fazendo algumas trocas')
