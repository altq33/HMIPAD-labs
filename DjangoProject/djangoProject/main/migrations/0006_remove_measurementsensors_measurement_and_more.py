# Generated by Django 4.1.7 on 2023-06-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_measurementsensors_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurementsensors',
            name='measurement',
        ),
        migrations.AddField(
            model_name='precipitationmeasurement',
            name='sensors',
            field=models.ManyToManyField(to='main.measurementsensors'),
        ),
    ]