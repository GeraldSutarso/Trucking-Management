# Generated by Django 5.0 on 2024-06-04 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0007_alter_customer_profile_picture_alter_driver_id_card_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/')),
                ('result', models.CharField(max_length=50)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver_face', to='accounts.driver')),
            ],
        ),
    ]
