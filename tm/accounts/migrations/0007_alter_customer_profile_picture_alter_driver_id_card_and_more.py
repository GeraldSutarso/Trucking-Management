# Generated by Django 5.0 on 2024-03-04 07:04

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customer_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.customer_directory_path),
        ),
        migrations.AlterField(
            model_name='driver',
            name='id_card',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.driver_id_card_directory_path),
        ),
        migrations.AlterField(
            model_name='driver',
            name='license_card',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.driver_license_card_directory_path),
        ),
        migrations.AlterField(
            model_name='driver',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.driver_profile_directory_path),
        ),
    ]