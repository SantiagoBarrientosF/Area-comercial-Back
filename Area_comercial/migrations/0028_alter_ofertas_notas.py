# Generated by Django 5.0.6 on 2024-08-06 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area_comercial', '0027_remove_ofertas_observaciones_alter_ofertas_notas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ofertas',
            name='notas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Area_comercial.notas'),
        ),
    ]
