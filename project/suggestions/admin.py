from django.contrib import admin
from .models import *


@admin.register(CategorySuggestion)
class CategorySuggestionAdmin(admin.ModelAdmin):
    list_display = 'name', 'state'
    list_display_links = 'name',
    ordering = 'name',
    search_fields = 'name',
    
    
@admin.register(SubCategorySuggestion)    
class SubCategorySuggestionAdmin(admin.ModelAdmin):
    list_display = 'name', 'state'
    list_display_links = 'name',
    ordering = 'name',
    search_fields = 'name',
    