# Generated by Django 4.0.6 on 2022-09-04 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sea_bathing_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('temp', models.CharField(max_length=50)),
                ('digging', models.CharField(max_length=50)),
                ('wind_speed', models.CharField(max_length=50)),
                ('air_temp', models.CharField(max_length=50)),
                ('rainfall', models.CharField(max_length=50)),
                ('bathing', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='sea_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('temp', models.CharField(max_length=50)),
                ('digging', models.CharField(max_length=50)),
                ('wind_speed', models.CharField(max_length=50)),
                ('air_temp', models.CharField(max_length=50)),
                ('rainfall', models.CharField(max_length=50)),
            ],
        ),
    ]