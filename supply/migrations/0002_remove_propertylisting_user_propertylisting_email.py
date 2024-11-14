# Generated by Django 4.2.16 on 2024-11-14 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_tbusers_options"),
        ("supply", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="propertylisting",
            name="user",
        ),
        migrations.AddField(
            model_name="propertylisting",
            name="email",
            field=models.ForeignKey(
                db_column="email",
                default="comboy8231@gmail.com",
                on_delete=django.db.models.deletion.CASCADE,
                to="users.tbusers",
            ),
            preserve_default=False,
        ),
    ]
