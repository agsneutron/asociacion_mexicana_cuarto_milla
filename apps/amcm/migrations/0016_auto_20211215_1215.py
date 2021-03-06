# Generated by Django 3.2.6 on 2021-12-15 18:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0015_auto_20211201_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='estatus_cuota',
            field=models.CharField(choices=[('PAGADO', 'PAGADO'), ('PENDIENTE', 'PENDIENTE')], default='PAGADO', max_length=15, verbose_name='Estatus de Pago de Cuota'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_pago',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 12, 15, 18, 15, 7, 177844, tzinfo=utc), null=True, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2021, 12, 15, 18, 15, 7, 177844, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='cuentaspago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2021, 12, 15, 18, 15, 7, 176845, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='ejemplar',
            field=smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='cuadra', chained_model_field='cuadra', limit_choices_to={'estatus__nombre': 'ACTIVO'}, null=True, to='amcm.Ejemplares'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaPago',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 12, 15, 18, 15, 7, 175845, tzinfo=utc), null=True, verbose_name='Fecha del Pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2021, 12, 15, 18, 15, 7, 175845, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2021, 12, 15, 18, 15, 7, 176845, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
    ]
