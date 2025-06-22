"""Custom model definitions for the {{ cookiecutter.plugin_name }}} plugin.

This file is where you can define any custom database models.

- Any models defined here will require database migrations to be created.
- Don't forget to register your models in the admin interface if needed!
"""

from django.contrib.auth.models import User
from django.db import models


class ExampleModel(models.Model):
    """An example model for the {{ cookiecutter.plugin_name }} plugin."""

    class Meta:
        """Meta options for the model."""
        verbose_name = "Example Model"
        verbose_name_plural = "Example Models"

    user = models.ForeignKey(
        User, unique=True, null=False, blank=False,
        on_delete=models.CASCADE, related_name='example_models',
        help_text="The user associated with this example model"
    )
    
    counter = models.IntegerField(
        default=0, label="Counter",
        help_text="A simple counter for the example model"
    )
