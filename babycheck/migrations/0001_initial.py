# Generated by Django 5.0.3 on 2024-04-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BabyDeparture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baby_name', models.CharField(max_length=100)),
                ('baby_fetcher', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('comment', models.TextField(blank=True)),
            ],
        ),
    ]
