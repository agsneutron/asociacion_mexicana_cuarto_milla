# Generated by Django 3.2.6 on 2022-04-27 17:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0056_auto_20220224_1320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuentascontables',
            options={'ordering': ['codigo'], 'verbose_name': 'Cuenta Contable', 'verbose_name_plural': 'Cuentas Contables'},
        ),
        migrations.AlterModelOptions(
            name='cuentasevento',
            options={'ordering': ['cuenta'], 'verbose_name': 'Cuentas Contables del Evento', 'verbose_name_plural': 'Cuentas Contables del Evento'},
        ),
        migrations.AddField(
            model_name='pago',
            name='tuvo_credito',
            field=models.BooleanField(default=False, verbose_name='tuvo_credito'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_pago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 4, 27, 17, 33, 39, 463454, tzinfo=utc), null=True, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 4, 27, 17, 33, 39, 463441, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='cuentaspago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 4, 27, 17, 33, 39, 453600, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='elegible',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 4, 27, 17, 33, 39, 453872, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='observaciones',
            field=models.TextField(blank=True, max_length=500, verbose_name='Datos del peso'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaPago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 4, 27, 17, 33, 39, 451975, tzinfo=utc), null=True, verbose_name='Fecha del Pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 4, 27, 17, 33, 39, 451990, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 4, 27, 17, 33, 39, 462910, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='referenciaformapago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 4, 27, 17, 33, 39, 462596, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
    ]