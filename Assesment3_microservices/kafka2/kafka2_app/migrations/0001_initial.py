# Generated by Django 5.1.6 on 2025-02-21 07:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "pincode",
                    models.CharField(
                        max_length=6,
                        primary_key=True,
                        serialize=False,
                        validators=[django.core.validators.MinLengthValidator(6)],
                    ),
                ),
                (
                    "district",
                    models.CharField(
                        max_length=100,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                ("state", models.CharField(max_length=50)),
                (
                    "population_density",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Population per square km",
                        max_digits=8,
                    ),
                ),
                ("district_headquarters", models.CharField(max_length=100)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "kafka_topic",
                    models.CharField(
                        default="location-updates",
                        help_text="Kafka topic for location updates",
                        max_length=100,
                    ),
                ),
            ],
            options={
                "ordering": ["state", "district"],
                "indexes": [
                    models.Index(
                        fields=["last_updated"], name="kafka2_app__last_up_9cfa36_idx"
                    )
                ],
                "unique_together": {("district", "state")},
            },
        ),
    ]
