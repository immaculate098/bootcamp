# Generated by Django 5.0.3 on 2024-05-19 10:30

import django.db.models.deletion
import sitterduty.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[sitterduty.models.validate_letters])),
                ('gender', models.CharField(max_length=10, validators=[sitterduty.models.validate_letters])),
                ('location', models.CharField(max_length=100, validators=[sitterduty.models.validate_letters])),
                ('date_of_birth', models.DateField()),
                ('nin', models.CharField(default='CF', max_length=14, validators=[sitterduty.models.validate_NIN_length])),
                ('religion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Religion (optional)')),
                ('education', models.CharField(max_length=100, validators=[sitterduty.models.validate_letters])),
                ('contact', models.CharField(default='', max_length=15, validators=[sitterduty.models.validate_contact_length])),
                ('sitter_number', models.CharField(max_length=200, null=True, unique=True)),
                ('next_of_kin', models.CharField(max_length=100, validators=[sitterduty.models.validate_letters])),
                ('recommender_name', models.CharField(max_length=100, validators=[sitterduty.models.validate_letters])),
                ('recommender_contact', models.CharField(default='', max_length=15, validators=[sitterduty.models.validate_contact_length])),
            ],
        ),
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
                ('on_duty', models.BooleanField(default=False)),
                ('off_duty', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sitters', to='sitterduty.student')),
            ],
        ),
    ]
