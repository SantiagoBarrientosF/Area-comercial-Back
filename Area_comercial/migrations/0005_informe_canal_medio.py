# Generated by Django 5.0.6 on 2024-07-12 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area_comercial', '0004_informe_por_campaña'),
    ]

    operations = [
        migrations.AddField(
            model_name='informe',
            name='Canal_medio',
            field=models.CharField(default='l', max_length=200),
        ),
    ]