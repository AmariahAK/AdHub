# Generated by Django 4.1 on 2022-08-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="LikePost",
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
                ("post_id", models.CharField(max_length=500)),
                ("username", models.CharField(max_length=100)),
            ],
        ),
    ]
