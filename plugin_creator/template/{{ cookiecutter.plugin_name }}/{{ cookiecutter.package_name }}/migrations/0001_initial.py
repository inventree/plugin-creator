# Generated by Django 4.2.22 on 2025-06-23 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ExampleModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "counter",
                    models.IntegerField(
                        default=0,
                        help_text="A simple counter for the example model",
                        verbose_name="Counter",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        help_text="The user associated with this example model",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="example_model",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Example Model",
                "verbose_name_plural": "Example Models",
            },
        ),
    ]
