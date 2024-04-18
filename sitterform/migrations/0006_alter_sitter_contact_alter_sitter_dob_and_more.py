# Generated by Django 5.0.3 on 2024-04-17 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitterform', '0005_alter_sitter_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='contact',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='dob',
            field=models.DateField(default=0),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='recommender_contact',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='sitter_number',
            field=models.CharField(max_length=100),
        ),
    ]