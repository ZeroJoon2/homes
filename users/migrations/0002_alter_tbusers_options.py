# Generated by Django 4.2.16 on 2024-11-12 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tbusers",
            options={"verbose_name": "users", "verbose_name_plural": "users"},
        ),
    ]
