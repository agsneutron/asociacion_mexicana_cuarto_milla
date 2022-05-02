# Generated by Django 3.2.6 on 2022-04-27 23:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0058_auto_20220427_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='fecha_pago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 4, 27, 23, 53, 7, 677554, tzinfo=utc), null=True, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 4, 27, 23, 53, 7, 677541, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='cuentaspago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 4, 27, 23, 53, 7, 667967, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='elegible',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 4, 27, 23, 53, 7, 668231, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='estadocuenta',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 27, 23, 53, 7, 677838, tzinfo=utc), editable=False, verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='estadocuentadetalle',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 27, 23, 53, 7, 678164, tzinfo=utc), editable=False, verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaPago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 4, 27, 23, 53, 7, 666469, tzinfo=utc), null=True, verbose_name='Fecha del Pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 4, 27, 23, 53, 7, 666482, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 4, 27, 23, 53, 7, 677018, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='referenciaformapago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 4, 27, 23, 53, 7, 676649, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
    ]
