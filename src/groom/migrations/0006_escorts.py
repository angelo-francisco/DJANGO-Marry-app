# Generated by Django 5.1.2 on 2024-11-07 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("groom", "0005_gift_reservated_by"),
    ]

    operations = [
        migrations.CreateModel(
            name="Escorts",
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
                ("escort", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "guest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="groom.guest"
                    ),
                ),
            ],
        ),
    ]
