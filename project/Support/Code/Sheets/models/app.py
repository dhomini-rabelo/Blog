from .django_class import Base
from .components import *
from .editor import Editor
from pathlib import Path
from .support import *
import io


class DjangoApp(Base, AppAdmin, AppModels, AppSettings, AppViews, AppTests):
    def __init__(self, base_path: str, app: str, project_name: str):
        self.base_path = self.adapt_path(base_path)
        self.app = self.adapt_path(app)
        self.path = f'{self.base_path}/{self.app}'
        assert_folder_existence(self.path)
        self.response = lambda message: response(message, 0.25,app)
        self.spaces = lambda text_list, spaces: list(map(lambda text: f'{sp(spaces)}{text}', text_list))
        self.init = Editor(self.path, '__init__.py')
        self.admin = Editor(self.path, 'admin.py')
        self.models = Editor(self.path, 'models.py')
        self.views = Editor(self.path, 'views.py')
        self.settings = Editor(self.base_path, f'{project_name}/settings.py')
    
    def config_app(self):
        settings = [
            "from django.apps import AppConfig", f"\n\nclass {self.app.title()}Config(AppConfig):",
            *self.spaces([
                "default_auto_field = 'django.db.models.BigAutoField'", f"name = '{self.app}'"
            ], 4),
        ]
        self.init.insert_code(0, settings) # new_reading
        self.response('criada a classe app config')        
            
    def create_py_folder(self, folder_path):
        path = f'{self.base_path}/{folder_path}'
        Path(path).mkdir()
        sleep(0.5)
        with io.open(f'{path}/__init__.py', 'w') as file:
            pass
        
    def create_py_archive(self, archive_path):
        path = f'{self.base_path}/{self.adapt_pyname(archive_path)}'
        with io.open(path, 'w') as file:
            pass
        
    def create_archive(self, archive_path):
        path = f'{self.base_path}/{archive_path}'
        with io.open(path, 'w') as file:
            pass

    def create_templates_folder(self, name_space: str=''):
        try: 
            Path(f'{self.path}/templates').mkdir()
            sleep(0.3)
            Path(f'{self.path}/templates/{name_space}').mkdir()
            self.response(f'pasta templates foi criada')
        except FileExistsError:
            self.response(f'a pasta templates já existe')

    def create_url_archive(self):
        with io.open(f'{self.path}/urls.py', 'w', encoding='utf-8') as arc:
            arc.write('from django.urls import path\nfrom .views import *\n')
            arc.write(f'\nurlpatterns = [\n{sp(4)}path(),\n]\n')
            self.response(f'arquivo urls.py criado')
    
    def create_forms_archive(self):
        with io.open(f'{self.base_path}/Support/code/forms/{self.app}.py', 'w', encoding='utf-8') as arc:
            arc.write('from django.forms import ModelForm, ValidationError\n')
            arc.write(f'from {self.app}.models import *\n')
            self.response('arquivo form criado')

    def add_form(self, model_name: str):
        path = f'{self.base_path}/Support/code/forms'
        editor = Editor(path, f'{self.app}.py')
        form_script = [
            f"class {model_name.title()}Form(ModelForm):\n",
            *self.spaces([
                "class Meta:",
                *self.spaces([
                    "fields = '__all__'",
                    f"model = {model_name}"
                ],8)
            ], 4),
        ]
        editor.add_in_end(form_script)
        self.response(f'criando form para {model_name}')
