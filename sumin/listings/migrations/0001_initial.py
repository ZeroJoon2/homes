# Generated by Django 4.2.16 on 2024-11-11 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PropertyListing",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("location", models.CharField(max_length=100)),
                ("bedrooms", models.IntegerField()),
                ("bathrooms", models.IntegerField()),
                ("listed_date", models.DateTimeField(auto_now_add=True)),
                (
                    "house_type",
                    models.CharField(
                        choices=[
                            ("villa", "빌라/주택"),
                            ("officetel", "오피스텔"),
                            ("apartment", "아파트"),
                            ("commercial", "상가/사무실"),
                        ],
                        default="villa",
                        max_length=20,
                    ),
                ),
                (
                    "transaction_type",
                    models.CharField(
                        choices=[
                            ("monthly_rent", "월세"),
                            ("jeonse", "전세"),
                            ("sale", "매매"),
                        ],
                        default="sale",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
