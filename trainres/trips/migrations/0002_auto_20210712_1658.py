# Generated by Django 3.2.3 on 2021-07-12 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='train',
            old_name='tid',
            new_name='train_id',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='dest',
            new_name='destination',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='reservedSeats',
            new_name='reserved_seats',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='src',
            new_name='source',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='tid',
            new_name='train_id',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='trid',
            new_name='trip_id',
        ),
    ]
