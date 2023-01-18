# Generated by Django 4.1.5 on 2023-01-18 12:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vhsApp', '0005_alter_video_autoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solicitud', models.TextField(default='')),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='membresia',
            old_name='Facturacion',
            new_name='facturacion',
        ),
        migrations.RemoveField(
            model_name='video',
            name='autoria',
        ),
        migrations.RemoveField(
            model_name='video',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='video',
            name='fecha',
        ),
        migrations.AddField(
            model_name='video',
            name='autor',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='año',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='descripcion',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='miembro_desde',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Opcion',
        ),
        migrations.DeleteModel(
            name='Pregunta',
        ),
    ]