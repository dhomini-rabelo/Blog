from models.eraser import delete_comments_by_folder
from for_project import project_name, bp
from models.app import DjangoApp
from time import sleep


app_name = 'authors'
app = DjangoApp(bp, app_name, project_name)


#* MAIS USADOS
# app.add_form('Pessoa')
# app.register_admin('SubCategory')
# app.create_view('form', logged=False)

#* APÓS CRIAÇÃO
# sleep(1)
# delete_comments_by_folder(bp, app_name)
# sleep(1)
# app.create_url_archive()
# sleep(1)
# app.import_for_model()
# sleep(1)
# app.register_app()
# sleep(1)
# app.config_app()





#* CRIAR TESTES
# app.create_py_folder(f'Support/code/tests/{app_name}')
# tests = ['models', 'views', 'forms']
# for test in tests:
#     app.create_test_archive(f'{app_name}/{test}')