from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)
from django.db.models.deletion import CASCADE
from django.db.models.fields import SlugField


class Category(Model):
    name = CharField(max_length=256)
    slug = SlugField(max_length=256)
    img = ImageField(upload_to='categories/%Y/%m/%d', blank=True, null=True)



class SubCategory(Model):
    name = CharField(max_length=256)
    slug = SlugField(max_length=256)
    img = ImageField(upload_to='sub_categories/%Y/%m/%d', blank=True, null=True)
    category = ForeignKey(Category, on_delete=CASCADE)

