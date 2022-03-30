from django.db.models import (Model, CharField, DateTimeField, TextField, SlugField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField
from accounts.models import User
from categories.models import Category, SubCategory




class Post(Model):
    title = CharField(max_length=256, verbose_name='Título')
    description = CharField(max_length=256, verbose_name='Descrição')
    author = ForeignKey(User, on_delete=RESTRICT, related_name='posts', verbose_name='Autor')
    img = ImageField(upload_to='posts/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem de publicação')
    text = TextField(verbose_name='Texto')
    created = DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated = DateTimeField(auto_now=True, verbose_name='Atualizado em')
    sub_categories = ManyToManyField(SubCategory, verbose_name='Subcategorias')
    category = ForeignKey(Category, on_delete=RESTRICT, related_name='posts', verbose_name='Categoria')
    code = PositiveIntegerField(unique=True, verbose_name='Código')
    published = BooleanField(verbose_name='Publicado')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'



class Comment(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='comments', verbose_name='Usuário')
    post = ForeignKey(Post, on_delete=CASCADE, related_name='comments', verbose_name='Post')
    text = TextField(verbose_name='Texto')
    date = DateTimeField(auto_now_add=True, verbose_name='Data')
    published = BooleanField(default=True, verbose_name='Publicado')

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'


