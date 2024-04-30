# Generated by Django 5.0.3 on 2024-04-25 07:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sitterduty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('fee_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('parent_names', models.CharField(blank=True, max_length=100)),
                ('baby_deliverer', models.CharField(blank=True, max_length=100)),
                ('period_of_stay', models.CharField(max_length=100)),
                ('baby_number', models.IntegerField(default=0)),
                ('arrival_time', models.TimeField(auto_now_add=True)),
                ('departure_time', models.TimeField(auto_now=True)),
                ('assigned_sitter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sitterduty.sitter')),
            ],
        ),
    ]