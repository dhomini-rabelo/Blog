from django.db.models import (Model, CharField, DateTimeField, TextField, SlugField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField
from accounts.models import User
from categories.models import Category, SubCategory




class Post(Model):
    title = CharField(max_length=256)
    slug = SlugField(max_length=256)
    description = CharField(max_length=256)
    author = ForeignKey(User, on_delete=RESTRICT)
    img = ImageField(upload_to='posts/%Y/%m/%d', blank=True, null=True)
    img_active = BooleanField(default=True)
    text = TextField()
    date = DateTimeField(auto_now_add=True)
    sub_categories = ManyToManyField(SubCategory)
    category = ForeignKey(Category, on_delete=RESTRICT)
    code = PositiveIntegerField()
    published = BooleanField()



class Comment(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    text = TextField()
    date = DateTimeField(auto_now_add=True)
    published = BooleanField(default=True)

