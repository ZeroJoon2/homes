# Generated by Django 4.2.16 on 2024-11-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demand", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tbdemands",
            options={"verbose_name": "Demand", "verbose_name_plural": "Demands"},
        ),
        migrations.AddField(
            model_name="tbdemands",
            name="house_transaction_code",
            field=models.IntegerField(
                choices=[
                    (1, "아파트"),
                    (2, "빌라"),
                    (3, "단독주택"),
                    (4, "다가구주택"),
                    (5, "오피스텔"),
                ],
                default=0,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tbdemands",
            name="house_transaction_name",
            field=models.CharField(default=1, editable=False, max_length=100),
            preserve_default=False,
        ),
    ]
