# Generated by Django 5.0.3 on 2024-05-05 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsitter', '0002_alter_payment_change_received'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='baby',
        ),
        migrations.AddField(
            model_name='payment',
            name='baby_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('halfday', 'Half Day'), ('fullday', 'Full Day'), ('monthlypay', 'Monthly Payment')], default='pay', max_length=20),
        ),
        migrations.DeleteModel(
            name='Baby',
        ),
    ]