# Generated by Django 3.2.6 on 2021-10-27 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0011_auto_20211027_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejemplares',
            name='estatus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='amcm.estatusejemplar', verbose_name='Estatus del Ejemplar'),
            preserve_default=False,
        ),
    ]
