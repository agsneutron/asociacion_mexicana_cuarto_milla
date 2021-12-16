# Generated by Django 3.2.6 on 2021-12-01 23:00

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0014_auto_20211028_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuentasContables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(verbose_name='Código')),
                ('nombre', models.CharField(max_length=200, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Cuenta Contable',
                'verbose_name_plural': 'Cuentas Contables',
                'ordering': ['nombre'],
            },
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_pago',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 12, 1, 23, 0, 56, 872049, tzinfo=utc), null=True, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2021, 12, 1, 23, 0, 56, 872049, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaPago',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 12, 1, 23, 0, 56, 869033, tzinfo=utc), null=True, verbose_name='Fecha del Pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2021, 12, 1, 23, 0, 56, 869033, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2021, 12, 1, 23, 0, 56, 871032, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.CreateModel(
            name='CuentasPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importe', models.FloatField(default=0, verbose_name='Importe')),
                ('fecha_registro', models.DateField(default=datetime.datetime(2021, 12, 1, 23, 0, 56, 870032, tzinfo=utc), verbose_name='Fecha de Registro')),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amcm.cuentascontables', verbose_name='Cuenta Contable')),
                ('pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amcm.pago', verbose_name='Pago')),
            ],
            options={
                'verbose_name': 'Cuenta - Pago',
                'verbose_name_plural': 'Cuentas - Pago',
            },
        ),
    ]