# Generated by Django 4.2.9 on 2024-03-11 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manutencao', '0007_alter_customuser_options_alter_tipo_aquario_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manutencao',
            options={'ordering': ['data'], 'verbose_name': 'Manutenção', 'verbose_name_plural': 'Manutenções'},
        ),
    ]
