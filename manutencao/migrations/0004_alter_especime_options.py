# Generated by Django 4.2.9 on 2024-03-11 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manutencao', '0003_aviso'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='especime',
            options={'ordering': ['nome_popular'], 'verbose_name': 'Espécime', 'verbose_name_plural': 'Espécimes'},
        ),
    ]