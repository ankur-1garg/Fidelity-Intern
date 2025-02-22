# Generated by Django 5.1.6 on 2025-02-21 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Trip",
            fields=[
                ("trip_id", models.AutoField(primary_key=True, serialize=False)),
                ("pickup_datetime", models.DateTimeField()),
                ("dropoff_datetime", models.DateTimeField()),
                ("passenger_count", models.IntegerField()),
                ("trip_distance", models.DecimalField(decimal_places=2, max_digits=10)),
                ("fare_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("tip_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("pickup_location", models.CharField(max_length=100)),
                ("dropoff_location", models.CharField(max_length=100)),
                ("payment_type", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "TRIPS",
            },
        ),
    ]
