from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'name', 'slug'
    ordering = 'name',
    search_fields = 'name',


@admin.register(SubCategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 'slug', 'get_category'
    list_display_links = 'name',
    list_per_page = 50
    list_select_related = 'category',
    ordering = 'name',
    search_fields = 'name',

    @admin.display(description='Categoria')
    def get_category(self, sub_category):
        return sub_category.category.name