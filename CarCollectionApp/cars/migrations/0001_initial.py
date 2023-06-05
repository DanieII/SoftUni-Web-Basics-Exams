# Generated by Django 4.2.2 on 2023-06-05 19:13

import cars.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
                ('year', models.IntegerField(validators=[cars.models.car_year_validator])),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]