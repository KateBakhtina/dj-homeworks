# Generated by Django 5.0.1 on 2024-02-02 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_alter_measurement_sensors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensors',
            new_name='sensor',
        ),
    ]