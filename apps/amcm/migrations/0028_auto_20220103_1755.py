# Generated by Django 3.2.8 on 2022-01-03 23:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0027_auto_20220103_0103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='limite',
            options={'ordering': ['nombre'], 'verbose_name': 'Tipo de Condición', 'verbose_name_plural': 'Tipo de Condiciones'},
        ),
        migrations.AlterModelOptions(
            name='tipocondicion',
            options={'ordering': ['nombre'], 'verbose_name': 'Limite ', 'verbose_name_plural': 'Limite'},
        ),
        migrations.AlterField(
            model_name='condicionesevento',
            name='limite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amcm.limite', verbose_name='Tipo de Condición'),
        ),
        migrations.AlterField(
            model_name='condicionesevento',
            name='tipoCondicion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amcm.tipocondicion', verbose_name='Límite'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_pago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 3, 23, 55, 33, 882793, tzinfo=utc), null=True, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 3, 23, 55, 33, 882766, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='cuentaspago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 3, 23, 55, 33, 867126, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='elegible',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 3, 23, 55, 33, 868345, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaPago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 3, 23, 55, 33, 865594, tzinfo=utc), null=True, verbose_name='Fecha del Pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 1, 3, 23, 55, 33, 865627, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 3, 23, 55, 33, 870538, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('telefono', models.CharField(blank=True, max_length=15, verbose_name='Teléfono')),
                ('cuadra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amcm.cuadras', verbose_name='Cuadra')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
    ]
