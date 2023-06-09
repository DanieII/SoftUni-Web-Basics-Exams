# Generated by Django 4.2.1 on 2023-06-03 16:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True)),
                ('genre', models.CharField(choices=[('pop', 'Pop Music'), ('jazz', 'Jazz Music'), ('rnb', 'R&B Music'), ('rock', 'Rock Music'), ('country', 'Country Music'), ('dance', 'Dance Music'), ('hiphop', 'Hip Hop Music'), ('other', 'Other')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
