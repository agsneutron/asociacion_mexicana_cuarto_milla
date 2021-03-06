# Generated by Django 3.2.8 on 2021-12-29 08:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0019_auto_20211229_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='fecha_pago',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 12, 29, 8, 34, 25, 826056, tzinfo=utc), null=True, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2021, 12, 29, 8, 34, 25, 826032, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='cuentaspago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2021, 12, 29, 8, 34, 25, 823511, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaPago',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 12, 29, 8, 34, 25, 821984, tzinfo=utc), null=True, verbose_name='Fecha del Pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2021, 12, 29, 8, 34, 25, 822020, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2021, 12, 29, 8, 34, 25, 824081, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.CreateModel(
            name='CuentasEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='amcm.cuentascontables', verbose_name='Cuenta Contable')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amcm.evento', verbose_name='Evento')),
            ],
            options={
                'verbose_name': 'Cuentas Contables del Evento',
                'verbose_name_plural': 'Cuentas Contables del Evento',
            },
        ),
    ]
