# Generated by Django 4.1.3 on 2022-11-28 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_reserva_fecha_inicial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='fecha_devolucion',
            field=models.DateField(default='2022-12-10', verbose_name='Fecha devolución'),
            preserve_default=False,
        ),
    ]
