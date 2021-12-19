from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, CASCADE,PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)
from django.db.models.fields import SlugField


class Category(Model):
    name = CharField(max_length=256, verbose_name='Nome')
    slug = SlugField(max_length=256, verbose_name='Url')
    img = ImageField(upload_to='categories/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'    


class SubCategory(Model):
    name = CharField(max_length=256, verbose_name='Nome')
    slug = SlugField(max_length=256, verbose_name='Url')
    img = ImageField(upload_to='sub_categories/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    category = ForeignKey(Category, on_delete=CASCADE, related_name='sub_categories', verbose_name='Categoria')

    class Meta:
        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategorias'

