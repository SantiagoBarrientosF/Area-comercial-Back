# Generated by Django 5.0.6 on 2024-07-24 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area_comercial', '0021_remove_empresa_id_contacto_contacto_id_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='Id_empresa',
        ),
        migrations.AddField(
            model_name='empresa',
            name='Id_contacto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Area_comercial.contacto'),
        ),
    ]
