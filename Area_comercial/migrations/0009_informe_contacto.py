# Generated by Django 5.0.6 on 2024-07-17 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area_comercial', '0008_alter_informe_observaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='informe',
            name='Contacto',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
