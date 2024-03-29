# Generated by Django 5.0 on 2024-03-21 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0007_truck_overall_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='truck_accepted',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='truck',
            name='truck_available',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
