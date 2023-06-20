# Generated by Django 4.2.2 on 2023-06-20 16:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]