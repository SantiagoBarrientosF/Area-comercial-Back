# Generated by Django 5.0.6 on 2024-08-06 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area_comercial', '0025_remove_ofertas_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notas', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='ofertas',
            name='notas',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Area_comercial.notas'),
        ),
    ]
