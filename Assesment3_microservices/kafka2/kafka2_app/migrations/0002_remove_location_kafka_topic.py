# Generated by Django 5.1.6 on 2025-02-21 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kafka2_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="location",
            name="kafka_topic",
        ),
    ]
