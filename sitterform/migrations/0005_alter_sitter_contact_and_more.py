# Generated by Django 5.0.3 on 2024-04-17 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitterform', '0004_alter_sitter_nin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='contact',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='recommender_contact',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='sitter_number',
            field=models.IntegerField(max_length=10),
        ),
    ]
