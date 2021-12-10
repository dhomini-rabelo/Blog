# Generated by Django 4.0 on 2021-12-08 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='a', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(default='a', max_length=256),
            preserve_default=False,
        ),
    ]