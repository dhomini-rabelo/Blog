# Generated by Django 4.0 on 2022-03-05 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0002_alter_categorysuggestion_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorysuggestion',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='categorysuggestion',
            name='state',
            field=models.CharField(choices=[('invalid', 'INVÁLIDO'), ('reject', 'RECUSADO'), ('loading', 'EM ANDAMENTO'), ('accept', 'ACEITO')], default='loading', max_length=256, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='subcategorysuggestion',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='subcategorysuggestion',
            name='state',
            field=models.CharField(choices=[('invalid', 'INVÁLIDO'), ('reject', 'RECUSADO'), ('loading', 'EM ANDAMENTO'), ('accept', 'ACEITO')], default='loading', max_length=256, verbose_name='Estado'),
        ),
    ]
