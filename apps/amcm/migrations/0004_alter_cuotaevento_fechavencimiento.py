# Generated by Django 3.2.8 on 2021-10-24 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amcm', '0003_auto_20211024_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuotaevento',
            name='fechaVencimiento',
            field=models.DateField(verbose_name='Fecha de Vencimiento'),
        ),
    ]
