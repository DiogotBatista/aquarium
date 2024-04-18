# Generated by Django 4.2.9 on 2024-03-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manutencao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Data de cadastro'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_access',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Último Acesso'),
        ),
    ]