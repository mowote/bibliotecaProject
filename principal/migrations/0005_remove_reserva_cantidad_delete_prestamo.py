# Generated by Django 4.1.3 on 2022-11-28 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_remove_reserva_cantidad_dias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='cantidad',
        ),
        migrations.DeleteModel(
            name='Prestamo',
        ),
    ]