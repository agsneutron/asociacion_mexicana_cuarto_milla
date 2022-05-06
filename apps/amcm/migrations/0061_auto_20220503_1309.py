# Generated by Django 3.2.6 on 2022-05-03 18:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0060_auto_20220427_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadocuentadetalle',
            name='ejemplares',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Ejemplares'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_pago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 3, 18, 9, 50, 205944, tzinfo=utc), null=True, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 5, 3, 18, 9, 50, 205930, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='cuentaspago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 5, 3, 18, 9, 50, 196461, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='elegible',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 5, 3, 18, 9, 50, 196723, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='estadocuenta',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 18, 9, 50, 206228, tzinfo=utc), editable=False, verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='estadocuentadetalle',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 18, 9, 50, 206578, tzinfo=utc), editable=False, verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaPago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 3, 18, 9, 50, 194908, tzinfo=utc), null=True, verbose_name='Fecha del Pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 5, 3, 18, 9, 50, 194923, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 5, 3, 18, 9, 50, 205417, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='referenciaformapago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 5, 3, 18, 9, 50, 205052, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
    ]