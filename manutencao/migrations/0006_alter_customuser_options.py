# Generated by Django 4.2.9 on 2024-03-11 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manutencao', '0005_alter_populacao_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['data_cadastro'], 'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
    ]