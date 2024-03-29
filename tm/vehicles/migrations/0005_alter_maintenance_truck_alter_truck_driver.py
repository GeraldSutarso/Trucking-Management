# Generated by Django 5.0 on 2024-01-26 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_admin_user_alter_customer_user_and_more'),
        ('vehicles', '0004_remove_maintenance_status_maintenance_schedule_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='truck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='truck_maintenance', to='vehicles.truck'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='driver',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='truck_driver', to='accounts.driver'),
        ),
    ]
