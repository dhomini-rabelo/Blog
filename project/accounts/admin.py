from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from Support.Code.django.forms.accounts import UserChangeForm, UserCreationForm
from accounts.models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos adicionais", {"fields": ('name', 'slug', "photo", "my_static_pages")}),
    )
    list_display = 'username', 'name', 'email', 'slug'
    list_display_links = 'username',
    search_fields = 'name', 'email'
