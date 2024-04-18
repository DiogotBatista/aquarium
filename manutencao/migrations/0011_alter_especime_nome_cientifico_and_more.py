# Generated by Django 4.2.9 on 2024-03-13 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manutencao', '0010_alter_manutencao_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especime',
            name='nome_cientifico',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome científico'),
        ),
        migrations.AlterField(
            model_name='especime',
            name='nome_popular',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nome popular'),
        ),
    ]