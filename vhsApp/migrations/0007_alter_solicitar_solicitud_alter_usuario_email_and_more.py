# Generated by Django 4.1.5 on 2023-01-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vhsApp', '0006_solicitar_rename_facturacion_membresia_facturacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitar',
            name='solicitud',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='video',
            name='descripcion',
            field=models.TextField(max_length=500),
        ),
    ]