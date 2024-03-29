# Generated by Django 4.1.7 on 2023-06-02 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
            ],
        ),
        migrations.AddField(
            model_name='precipitationmeasurement',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.country'),
        ),
    ]
