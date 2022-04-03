from django.apps import AppConfig


class SuggestionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suggestions'
    verbose_name = 'Gerenciamento de Sugestões'

    def ready(self):
        import suggestions.signals