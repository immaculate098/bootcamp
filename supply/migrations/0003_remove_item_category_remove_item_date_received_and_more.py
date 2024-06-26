# Generated by Django 5.0.3 on 2024-05-03 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0002_item_remove_procurementrecord_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='date_received',
        ),
        migrations.RemoveField(
            model_name='item',
            name='details',
        ),
        migrations.RemoveField(
            model_name='item',
            name='quantity_received',
        ),
        migrations.RemoveField(
            model_name='item',
            name='unit_price',
        ),
        migrations.CreateModel(
            name='Issuing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('date_issued', models.DateField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supply.item')),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('date_received', models.DateField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supply.item')),
            ],
        ),
    ]
