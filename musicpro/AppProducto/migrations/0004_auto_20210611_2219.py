# Generated by Django 3.2.3 on 2021-06-12 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppProducto', '0003_auto_20210611_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='nombre',
            new_name='nombre_genero',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='nombre',
            new_name='nombre_marca',
        ),
    ]
