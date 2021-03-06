# Generated by Django 3.2.8 on 2022-01-03 06:49

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0025_auto_20211230_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elegible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('fecha_registro', models.DateField(default=datetime.datetime(2022, 1, 3, 6, 49, 58, 335119, tzinfo=utc), verbose_name='Fecha de registro')),
            ],
            options={
                'verbose_name': 'Elegible',
                'verbose_name_plural': 'Elegibles',
            },
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_pago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 3, 6, 49, 58, 337848, tzinfo=utc), null=True, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 3, 6, 49, 58, 337827, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='cuentaspago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 3, 6, 49, 58, 333643, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='elegibles_evento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amcm.evento', verbose_name='Elegibles de Evento '),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaPago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 3, 6, 49, 58, 332010, tzinfo=utc), null=True, verbose_name='Fecha del Pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 1, 3, 6, 49, 58, 332046, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 3, 6, 49, 58, 337016, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.CreateModel(
            name='ListadoElegibles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuadra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amcm.cuadras', verbose_name='Cuadra')),
                ('ejemplar', smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='cuadra', chained_model_field='cuadra', limit_choices_to={'estatus__nombre': 'ACTIVO'}, null=True, related_name='ejemplar_related_elegible', to='amcm.Ejemplares')),
                ('elegible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amcm.elegible')),
            ],
            options={
                'verbose_name': 'Listado de Elegibles',
                'verbose_name_plural': 'Listados de Elegibles',
            },
        ),
    ]
