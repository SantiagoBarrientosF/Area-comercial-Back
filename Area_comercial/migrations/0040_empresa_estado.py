# Generated by Django 5.0.6 on 2024-08-15 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area_comercial', '0039_ofertas_notas'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='Estado',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]