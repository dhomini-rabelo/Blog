from abc import ABC

class AppAdmin(ABC):

    def register_admin(self, model_name: str):
        # use admin.site.empty_value_display = '(None)'
        model = model_name.title()
        admin_class = [
            f"\n\n@admin.register({model})\nclass {model}Admin(admin.ModelAdmin):",
            *self.spaces([
                "list_display = '',", "list_display_links = '',", "list_filter = '',",
                "list_per_page = 50", "list_select_related = False # use tuple, default is False",
                "ordering = '',", "actions = None", "prepopulated_fields = {'slug': 'title',}", 
                "search_fields = '', # ^ -> startswith, = -> iexact, @ ->	search, None -> icontains",
            ], 4)
        ]
        self.admin.add_in_end(admin_class)
        self.response(f'class admin para {model_name} criada com sucesso')
            