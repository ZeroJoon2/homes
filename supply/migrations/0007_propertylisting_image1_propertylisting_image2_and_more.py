# Generated by Django 4.2.16 on 2024-11-14 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("supply", "0006_remove_propertylisting_unique_list_id_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="propertylisting",
            name="image1",
            field=models.ImageField(null=True, upload_to="supply_images/"),
        ),
        migrations.AddField(
            model_name="propertylisting",
            name="image2",
            field=models.ImageField(null=True, upload_to="supply_images/"),
        ),
        migrations.AddField(
            model_name="propertylisting",
            name="image3",
            field=models.ImageField(null=True, upload_to="supply_images/"),
        ),
        migrations.AddField(
            model_name="propertylisting",
            name="image4",
            field=models.ImageField(null=True, upload_to="supply_images/"),
        ),
        migrations.AddField(
            model_name="propertylisting",
            name="image5",
            field=models.ImageField(null=True, upload_to="supply_images/"),
        ),
        migrations.AddField(
            model_name="propertylisting",
            name="image6",
            field=models.ImageField(null=True, upload_to="supply_images/"),
        ),
        migrations.AddField(
            model_name="propertylisting",
            name="image7",
            field=models.ImageField(null=True, upload_to="supply_images/"),
        ),
    ]