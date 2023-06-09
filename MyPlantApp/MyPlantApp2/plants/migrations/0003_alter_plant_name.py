# Generated by Django 4.2.2 on 2023-06-20 16:31

import django.core.validators
from django.db import migrations, models
import plants.validators


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_alter_plant_plant_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), plants.validators.name_validator]),
        ),
    ]
