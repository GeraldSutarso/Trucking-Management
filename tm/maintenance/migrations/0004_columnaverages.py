from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0003_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColumnAverages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altitude_avg', models.FloatField()),
                ('engine_load_avg', models.FloatField()),
                ('barometric_pressure_avg', models.FloatField()),
                ('engine_coolant_temp_avg', models.FloatField()),
                ('ambient_air_temp_avg', models.FloatField()),
                ('engine_rpm_avg', models.FloatField()),
                ('intake_manifold_pressure_avg', models.FloatField()),
                ('maf_avg', models.FloatField()),
                ('air_intake_temp_avg', models.FloatField()),
                ('speed_avg', models.FloatField()),
                ('throttle_pos_avg', models.FloatField()),
                ('engine_runtime_avg', models.FloatField()),
                ('maintenance_status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
