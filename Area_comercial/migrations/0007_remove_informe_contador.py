# Generated by Django 5.0.6 on 2024-07-12 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Area_comercial', '0006_informe_contador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informe',
            name='contador',
        ),
    ]
