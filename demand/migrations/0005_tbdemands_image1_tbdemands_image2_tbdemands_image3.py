# Generated by Django 4.2.16 on 2024-11-13 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demand", "0004_tbdemands_post_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="tbdemands",
            name="image1",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="tbdemands",
            name="image2",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="tbdemands",
            name="image3",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]