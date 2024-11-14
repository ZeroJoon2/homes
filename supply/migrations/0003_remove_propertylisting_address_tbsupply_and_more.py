# Generated by Django 4.2.16 on 2024-11-14 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_tbusers_options"),
        ("supply", "0002_remove_propertylisting_user_propertylisting_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="propertylisting",
            name="address",
        ),
        migrations.CreateModel(
            name="tbSupply",
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
                (
                    "post_title",
                    models.CharField(default="제목을 입력해주세요", max_length=100),
                ),
                (
                    "house_type_code",
                    models.IntegerField(choices=[(1, "월세"), (2, "전세")]),
                ),
                ("house_type_name", models.CharField(max_length=100)),
                (
                    "house_transaction_code",
                    models.IntegerField(
                        choices=[
                            (1, "아파트"),
                            (2, "빌라"),
                            (3, "단독주택"),
                            (4, "다가구주택"),
                            (5, "오피스텔"),
                        ],
                        default=1,
                    ),
                ),
                ("house_transaction_name", models.CharField(max_length=100)),
                (
                    "house_location_code",
                    models.IntegerField(
                        choices=[
                            (1, "강남구"),
                            (2, "강동구"),
                            (3, "강북구"),
                            (4, "강서구"),
                            (5, "관악구"),
                            (6, "광진구"),
                            (7, "구로구"),
                            (8, "금천구"),
                            (9, "노원구"),
                            (10, "도봉구"),
                            (11, "동대문구"),
                            (12, "동작구"),
                            (13, "마포구"),
                            (14, "서대문구"),
                            (15, "서초구"),
                            (16, "성동구"),
                            (17, "성북구"),
                            (18, "송파구"),
                            (19, "양천구"),
                            (20, "영등포구"),
                            (21, "용산구"),
                            (22, "은평구"),
                            (23, "종로구"),
                            (24, "중구"),
                            (25, "중랑구"),
                        ]
                    ),
                ),
                ("house_location_name", models.CharField(max_length=100)),
                (
                    "email",
                    models.ForeignKey(
                        db_column="email",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.tbusers",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="propertylisting",
            name="list_id",
            field=models.ForeignKey(
                db_column="supply_id",
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="supply.tbsupply",
            ),
            preserve_default=False,
        ),
    ]
