
# Generated by Django 4.1 on 2023-12-22 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
# Generated by Django 4.1 on 2023-12-22 04:27

from django.db import migrations, models



class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Views",
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
                ("maemul_id", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "maemul_id")},
            },
        ),
    ]
