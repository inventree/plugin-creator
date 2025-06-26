"""Custom model definitions for the {{ cookiecutter.plugin_name }} plugin.

This file is where you can define any custom database models.

- Any models defined here will require database migrations to be created.
- Don't forget to register your models in the admin interface if needed!
"""

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class ExampleModel(models.Model):
    """An example model for the {{ cookiecutter.plugin_name }} plugin."""

    class Meta:
        """Meta options for the model."""
        app_label = "{{ cookiecutter.package_name }}"
        verbose_name = _("Example Model")
        verbose_name_plural = _("Example Models")

    user = models.OneToOneField(
        User, unique=True, null=False, blank=False,
        on_delete=models.CASCADE, related_name='example_model',
        help_text=_("The user associated with this example model")
    )
    
    counter = models.IntegerField(
        default=0,
        verbose_name=_("Counter"),
        help_text=_("A simple counter for the example model")
    )
