# Generated by Django 4.0.1 on 2022-01-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_car', models.PositiveIntegerField(blank=True, null=True)),
                ('total_prize', models.PositiveIntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('car', models.ManyToManyField(to='cars.Car')),
            ],
        ),
    ]
