# Generated by Django 5.0.3 on 2024-05-06 20:17

import sitterlist.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitterlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='education',
            field=models.CharField(max_length=100, validators=[sitterlist.models.validate_letters]),
        ),
    ]