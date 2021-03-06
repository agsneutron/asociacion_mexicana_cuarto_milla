# Generated by Django 3.2.8 on 2022-01-06 03:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0036_auto_20220105_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='fecha_pago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 6, 3, 51, 13, 963164, tzinfo=utc), null=True, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 6, 3, 51, 13, 963139, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='cuentaspago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 6, 3, 51, 13, 939820, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='elegible',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 6, 3, 51, 13, 940313, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='descripcion_evento',
            field=models.TextField(blank=True, max_length=2500, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaPago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 6, 3, 51, 13, 936798, tzinfo=utc), null=True, verbose_name='Fecha del Pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 1, 6, 3, 51, 13, 936844, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 6, 3, 51, 13, 962094, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
    ]
