"""Django config for the {{ cookiecutter.plugin_name }} plugin."""

from django.apps import AppConfig

class {{ cookiecutter.plugin_name }}Config(AppConfig):
    """Config class for the {{ cookiecutter.plugin_name }} plugin."""

    name = '{{ cookiecutter.package_name }}'

    def ready(self):
        """This function is called whenever the {{ cookiecutter.plugin_name }} plugin is loaded."""
        ...
