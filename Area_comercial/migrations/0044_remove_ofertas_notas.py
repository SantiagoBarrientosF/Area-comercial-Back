# Generated by Django 5.0.6 on 2024-08-16 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Area_comercial', '0043_empresa_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ofertas',
            name='notas',
        ),
    ]