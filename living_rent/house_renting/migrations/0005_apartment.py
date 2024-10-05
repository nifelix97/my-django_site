# Generated by Django 5.1.1 on 2024-10-05 05:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("house_renting", "0004_car_video"),
    ]

    operations = [
        migrations.CreateModel(
            name="Apartment",
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
                ("address", models.CharField(max_length=255)),
                (
                    "type",
                    models.CharField(
                        choices=[("APARTMENT", "Apartment"), ("OFFICE", "Office")],
                        default="APARTMENT",
                        max_length=10,
                    ),
                ),
                ("available", models.BooleanField(default=True)),
                (
                    "rent",
                    models.DecimalField(decimal_places=2, default=0, max_digits=14),
                ),
                ("date_added", models.DateField(auto_now_add=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("main_image", models.ImageField(upload_to="apartments/main/")),
                (
                    "video",
                    models.FileField(
                        blank=True, null=True, upload_to="apartments/videos/"
                    ),
                ),
                (
                    "landlord",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="house_renting.landlord",
                    ),
                ),
            ],
        ),
    ]
