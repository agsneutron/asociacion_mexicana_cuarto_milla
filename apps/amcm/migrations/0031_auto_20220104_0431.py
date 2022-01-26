# Generated by Django 3.2.8 on 2022-01-04 10:31

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0030_auto_20220104_0425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listadoelegibles',
            name='estaus',
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_pago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 4, 10, 31, 13, 294641, tzinfo=utc), null=True, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 4, 10, 31, 13, 294616, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='cuentaspago',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 4, 10, 31, 13, 276628, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='elegible',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 4, 10, 31, 13, 278598, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.RemoveField(
            model_name='listadoelegibles',
            name='ejemplar',
        ),
        migrations.AddField(
            model_name='listadoelegibles',
            name='ejemplar',
            field=smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='cuadra', chained_model_field='cuadra', limit_choices_to={'estatus__nombre': 'ACTIVO'}, null=True, related_name='ejemplar_related_elegible', to='amcm.Ejemplares'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaPago',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 4, 10, 31, 13, 275000, tzinfo=utc), null=True, verbose_name='Fecha del Pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 1, 4, 10, 31, 13, 275030, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2022, 1, 4, 10, 31, 13, 293389, tzinfo=utc), verbose_name='Fecha de registro'),
        ),
        migrations.CreateModel(
            name='EventoElegibles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estaus', models.BooleanField(default=False, verbose_name='Retirado')),
                ('cuadra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amcm.cuadras', verbose_name='Cuadra')),
                ('ejemplar', smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='cuadra', chained_model_field='cuadra', limit_choices_to={'estatus__nombre': 'ACTIVO'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ejemplar_elegible', to='amcm.ejemplares')),
                ('elegible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amcm.elegible')),
            ],
            options={
                'verbose_name': 'Elegibles para Evento',
                'verbose_name_plural': 'Elegibles para Evento',
            },
        ),
    ]