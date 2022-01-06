# Generated by Django 3.2.8 on 2022-01-06 02:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0032_auto_20220104_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='fecha_pago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 6, 2, 39, 32, 735124, tzinfo=utc), null=True, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 6, 2, 39, 32, 735099, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='cuentaspago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 6, 2, 39, 32, 718489, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='elegible',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 6, 2, 39, 32, 719879, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaPago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 6, 2, 39, 32, 717032, tzinfo=utc), null=True, verbose_name='Fecha del Pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 1, 6, 2, 39, 32, 717064, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 6, 2, 39, 32, 734069, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
    ]
