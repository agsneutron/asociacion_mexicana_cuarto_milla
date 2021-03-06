# Generated by Django 3.2.6 on 2021-10-27 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0010_recibo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstatusEjemplar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Estatus')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Estatus de Ejemplar',
                'verbose_name_plural': 'Estatus de Ejemplares',
                'ordering': ['nombre'],
            },
        ),
        migrations.AlterField(
            model_name='cuadras',
            name='celular',
            field=models.CharField(blank=True, max_length=15, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='cuadras',
            name='correoElectronico',
            field=models.CharField(blank=True, max_length=100, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='cuadras',
            name='observaciones',
            field=models.TextField(blank=True, max_length=500, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='cuadras',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='observaciones',
            field=models.TextField(blank=True, max_length=500, verbose_name='Observaciones'),
        ),
        migrations.CreateModel(
            name='ReasignaEjemplar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuadra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amcm.cuadras', verbose_name='Cuadra')),
                ('ejemplar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amcm.ejemplares', verbose_name='Ejemplar')),
            ],
        ),
    ]
