# Generated by Django 5.0.6 on 2024-07-12 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area_comercial', '0005_informe_canal_medio'),
    ]

    operations = [
        migrations.AddField(
            model_name='informe',
            name='contador',
            field=models.IntegerField(default=0),
        ),
    ]