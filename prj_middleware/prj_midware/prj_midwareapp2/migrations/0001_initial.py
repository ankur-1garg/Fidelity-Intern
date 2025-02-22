# Generated by Django 5.1.6 on 2025-02-17 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Manager",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("employee_id", models.IntegerField()),
                ("salary", models.IntegerField()),
                ("doj", models.DateField()),
                ("manages", models.IntegerField()),
            ],
            options={
                "db_table": "manager",
            },
        ),
    ]
