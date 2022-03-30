from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = 'code', 'author','title'
    list_display_links = 'code', 'author',
    list_filter = 'published',
    list_per_page = 50
    ordering = 'created',
    search_fields = 'author', 'title', 
    summernote_fields = 'text',


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = 'id', 'get_user_name', 'get_post_code'
    list_display_links = 'id',
    list_filter = 'published',
    list_select_related = 'user',
    list_per_page = 50
    ordering = 'date',
    search_fields = 'text', 

    @admin.display(description='Usuário')
    def get_user_name(self, comment):
        return comment.user.name

    @admin.display(description='Post Code')
    def get_post_code(self, comment):
        return comment.post.code
