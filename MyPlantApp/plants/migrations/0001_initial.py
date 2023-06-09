# Generated by Django 4.2.2 on 2023-06-09 19:28

import django.core.validators
from django.db import migrations, models
import plants.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinValueValidator(2), plants.models.name_validator])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
