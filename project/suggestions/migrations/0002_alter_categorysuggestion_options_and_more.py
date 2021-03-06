# Generated by Django 4.0 on 2022-02-21 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorysuggestion',
            options={'verbose_name': 'Sugestão de categoria', 'verbose_name_plural': 'Sugestões de categoria'},
        ),
        migrations.AlterModelOptions(
            name='subcategorysuggestion',
            options={'verbose_name': 'Sugestão de subcategoria', 'verbose_name_plural': 'Sugestões de subcategoria'},
        ),
        migrations.AlterField(
            model_name='categorysuggestion',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='categorysuggestion',
            name='state',
            field=models.CharField(choices=[('invalid', 'INVÁLIDO'), ('reject', 'RECUSADO'), ('loading', 'EM ANDAMENTO'), ('accept', 'ACEITO')], max_length=256, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='subcategorysuggestion',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='subcategorysuggestion',
            name='state',
            field=models.CharField(choices=[('invalid', 'INVÁLIDO'), ('reject', 'RECUSADO'), ('loading', 'EM ANDAMENTO'), ('accept', 'ACEITO')], max_length=256, verbose_name='Estado'),
        ),
    ]
