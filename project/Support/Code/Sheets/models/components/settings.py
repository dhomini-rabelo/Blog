from abc import ABC

class AppSettings(ABC):
            
    def register_app(self):
        self.settings.insert_code('    # My apps', f"    '{self.app}.{self.app.title()}Config',")
        self.response('app foi registrado')


    def register_abstract_user(self):
        self.settings.add_in_end(f"\nAUTH_USER_MODEL = 'accounts.User'")
        self.response('Registrado modelo padrão de usuário')
            
                    