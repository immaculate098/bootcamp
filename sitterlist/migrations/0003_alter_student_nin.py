# Generated by Django 5.0.3 on 2024-05-16 19:33

import sitterlist.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitterlist', '0002_alter_student_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='nin',
            field=models.CharField(default='CF', max_length=14, validators=[sitterlist.models.validate_NIN_length]),
        ),
    ]
