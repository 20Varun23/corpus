# Generated by Django 4.2.7 on 2024-07-13 06:05
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_post_published_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="description",
            field=models.CharField(max_length=400),
        ),
    ]