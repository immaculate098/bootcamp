# Generated by Django 5.0.3 on 2024-04-16 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitterform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='nin',
            field=models.CharField(max_length=12),
        ),
    ]
