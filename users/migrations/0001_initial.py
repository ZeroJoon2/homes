# Generated by Django 4.2.16 on 2024-11-12 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="tbUsers",
            fields=[
                (
                    "email",
                    models.CharField(
                        max_length=40, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("password", models.CharField(max_length=128)),
                ("nickname", models.CharField(max_length=50)),
            ],
        ),
    ]