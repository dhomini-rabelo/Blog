from django.contrib import admin

from Support.Code.Fast.utils.main import update_cache_keys
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'name', 'slug'
    ordering = 'name',
    search_fields = 'name',

    def save_model(self, request, obj, form, change):
        update_cache_keys('categories')
        return super().save_model(request, obj, form, change)


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

    def save_model(self, request, obj, form, change):
        update_cache_keys('subcategories')
        return super().save_model(request, obj, form, change)