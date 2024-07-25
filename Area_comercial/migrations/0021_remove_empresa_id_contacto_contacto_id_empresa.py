# Generated by Django 5.0.6 on 2024-07-24 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area_comercial', '0020_alter_informe_id_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='Id_contacto',
        ),
        migrations.AddField(
            model_name='contacto',
            name='Id_empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Area_comercial.empresa'),
        ),
    ]