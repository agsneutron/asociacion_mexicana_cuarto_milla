# Generated by Django 3.2.6 on 2021-10-27 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0009_auto_20211027_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_recibo', models.IntegerField(unique=True, verbose_name='Número de Recibo')),
                ('observaciones', models.CharField(blank=True, max_length=500, null=True, verbose_name='Observaciones')),
                ('fecha_registro', models.DateField(auto_now=True, verbose_name='Fecha de registro')),
                ('pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amcm.pago', verbose_name='Pago')),
            ],
            options={
                'verbose_name': 'Recibo',
                'verbose_name_plural': 'Recibos',
            },
        ),
    ]