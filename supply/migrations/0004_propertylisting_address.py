# Generated by Django 4.2.16 on 2024-11-14 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("supply", "0003_remove_propertylisting_address_tbsupply_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="propertylisting",
            name="address",
            field=models.TextField(blank=True),
        ),
    ]
