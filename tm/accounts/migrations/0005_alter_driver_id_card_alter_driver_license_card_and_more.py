# Generated by Django 5.0 on 2024-01-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_admin_user_alter_customer_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='id_card',
            field=models.ImageField(blank=True, null=True, upload_to='media/driver/id'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='license_card',
            field=models.ImageField(blank=True, null=True, upload_to='media/driver/license'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/driver/face'),
        ),
    ]
