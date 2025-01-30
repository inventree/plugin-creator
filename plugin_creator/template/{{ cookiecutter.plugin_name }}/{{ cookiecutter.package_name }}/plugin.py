"""{{ cookiecutter.plugin_description }}"""

from plugin import InvenTreePlugin
{% if cookiecutter.plugin_mixins.mixin_list %}
from plugin.mixins import {{ cookiecutter.plugin_mixins.mixin_list | map('trim') | join(', ') }}
{% endif %}
from . import PLUGIN_VERSION

{% if cookiecutter.plugin_mixins.mixin_list %}
class {{ cookiecutter.plugin_name }}({{ cookiecutter.plugin_mixins.mixin_list | map('trim') | join(', ') }}, InvenTreePlugin):
{% else %}
class {{ cookiecutter.plugin_name }}(InvenTreePlugin):
    {% endif %}
    """{{ cookiecutter.plugin_name }} - custom InvenTree plugin."""

    # Plugin metadata
    TITLE = "{{ cookiecutter.plugin_title }}"
    NAME = "{{ cookiecutter.plugin_name }}"
    SLUG = "{{ cookiecutter.plugin_slug }}"
    DESCRIPTION = "{{ cookiecutter.plugin_description }}"
    VERSION = PLUGIN_VERSION

    # Additional project information
    AUTHOR = "{{ cookiecutter.author_name }}"
    {% if cookiecutter.project_url -%}
    WEBSITE = "{{ cookiecutter.project_url }}"
    {%- endif %}
    LICENSE = "{{ cookiecutter.license_key }}"

    {%- if cookiecutter.plugin_mixins.mixin_list %}
    {% if "ScheduleMixin" in cookiecutter.plugin_mixins.mixin_list %}
    # Scheduled tasks (from ScheduleMixin)
    # Ref: https://docs.inventree.org/en/stable/extend/plugins/schedule/
    SCHEDULED_TASKS = {
        # Define your scheduled tasks here
    }
    {%- endif %}
    {% if "SettingsMixin" in cookiecutter.plugin_mixins.mixin_list %}
    # Plugin settings (from SettingsMixin)
    # Ref: https://docs.inventree.org/en/stable/extend/plugins/settings/
    SETTINGS = {
        # Define your plugin settings here...
    }
    {%- endif -%}
    {%- endif %}
