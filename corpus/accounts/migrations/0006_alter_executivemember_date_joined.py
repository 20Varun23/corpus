# Generated by Django 4.2.7 on 2024-07-12 05:54
import datetime

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_alter_executivemember_date_joined_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="executivemember",
            name="date_joined",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 12, 5, 54, 40, 426496, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Date Joined",
            ),
        ),
    ]
