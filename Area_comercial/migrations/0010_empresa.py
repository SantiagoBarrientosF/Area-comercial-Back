# Generated by Django 5.0.6 on 2024-07-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area_comercial', '0009_informe_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_empresa', models.CharField(max_length=200)),
                ('Encargado', models.CharField(max_length=200)),
                ('Telefono', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
            ],
        ),
    ]
