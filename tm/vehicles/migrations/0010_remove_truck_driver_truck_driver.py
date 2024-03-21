# Generated by Django 5.0 on 2024-03-21 03:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customer_profile_picture_alter_driver_id_card_and_more'),
        ('vehicles', '0009_remove_truck_driver_truck_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truck',
            name='driver',
        ),
        migrations.AddField(
            model_name='truck',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='truck_driver', to='accounts.driver'),
        ),
    ]