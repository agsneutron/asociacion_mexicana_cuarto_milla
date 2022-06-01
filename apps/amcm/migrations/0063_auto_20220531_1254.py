# Generated by Django 3.2.6 on 2022-05-31 17:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0062_auto_20220506_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='fecha_pago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 31, 17, 54, 33, 359754, tzinfo=utc), null=True, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 5, 31, 17, 54, 33, 359741, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='cuentaspago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 5, 31, 17, 54, 33, 349913, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='elegible',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 5, 31, 17, 54, 33, 350178, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='estadocuenta',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 17, 54, 33, 360038, tzinfo=utc), editable=False, verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='estadocuentadetalle',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 17, 54, 33, 360390, tzinfo=utc), editable=False, verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='estatus_credito',
            field=models.CharField(choices=[('PAGADO', 'PAGADO'), ('CREDITO', 'CREDITO'), ('ANTICIPO', 'ANTICIPO'), ('PAGO TOTAL', 'PAGO TOTAL')], default='PAGADO', max_length=15, verbose_name='Estatus del Pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaPago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 31, 17, 54, 33, 348256, tzinfo=utc), null=True, verbose_name='Fecha del Pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 5, 31, 17, 54, 33, 348269, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 5, 31, 17, 54, 33, 359236, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='referenciaformapago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 5, 31, 17, 54, 33, 358878, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
    ]