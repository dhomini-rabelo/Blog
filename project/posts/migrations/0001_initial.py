# Generated by Django 4.0 on 2021-12-08 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('img', models.ImageField(blank=True, null=True, upload_to='posts/%Y/%m/%d')),
                ('img_active', models.BooleanField(default=True)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('code', models.PositiveIntegerField()),
                ('published', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounts.user')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='categories.category')),
                ('sub_categories', models.ManyToManyField(to='categories.SubCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]