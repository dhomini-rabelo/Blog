from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, CASCADE,PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)
from django.db.models.fields import SlugField


class Category(Model):
    name = CharField(max_length=256, unique=True,verbose_name='Nome')
    slug = SlugField(max_length=256, unique=True, verbose_name='Url')
    img = ImageField(upload_to='categories/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')

    def get_path(self):
        return f'/categorias/{self.slug}/subcategorias/'

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'    


class SubCategory(Model):
    name = CharField(max_length=256, unique=True, verbose_name='Nome')
    slug = SlugField(max_length=256, unique=True, verbose_name='Url')
    img = ImageField(upload_to='sub_categories/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    category = ForeignKey(Category, on_delete=CASCADE, related_name='sub_categories', verbose_name='Categoria')

    def get_path(self):
        return f'/categorias/subcategorias/{self.slug}'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategorias'

