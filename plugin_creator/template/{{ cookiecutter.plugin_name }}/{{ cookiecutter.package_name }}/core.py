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
        # Define your scheduled tasks here...
    }
    {%- endif %}
    {% if "SettingsMixin" in cookiecutter.plugin_mixins.mixin_list %}
    # Plugin settings (from SettingsMixin)
    # Ref: https://docs.inventree.org/en/stable/extend/plugins/settings/
    SETTINGS = {
        # Define your plugin settings here...
        'CUSTOM_VALUE': {
            'name': 'Custom Value',
            'description': 'A custom value',
            'validator': int,
            'default': 42,
        }
    }
    {%- endif -%}
    
    {% if "UserInterfaceMixin" in cookiecutter.plugin_mixins.mixin_list %}

    # User interface elements (from UserInterfaceMixin)
    # Ref: https://docs.inventree.org/en/stable/extend/plugins/ui/
    {% if cookiecutter.frontend.features.panel %}
    # Custom UI panels
    def get_ui_panels(self, request, context: dict, **kwargs):
        """Return a list of custom panels to be rendered in the InvenTree user interface."""

        panels = []

        # Only display this panel for the 'part' target
        if context.get('target_model') == 'part':
            panels.append({
                'key': '{{ cookiecutter.plugin_slug }}-panel',
                'title': '{{ cookiecutter.plugin_title }}',
                'description': 'Custom panel description',
                'icon': 'ti:mood-smile:outline',
                'source': self.plugin_static_file('Panel.js:render{{ cookiecutter.plugin_name }}Panel'),
                'context': {
                    # Provide additional context data to the panel
                    {%- if "SettingsMixin" in cookiecutter.plugin_mixins.mixin_list %}
                    'settings': self.get_settings_dict(),
                    {% endif -%}
                    'foo': 'bar'
                }
            })
        
        return panels
    {% endif %}
    {% if cookiecutter.frontend.features.dashboard -%}
    # Custom dashboard items
    def get_ui_dashboard_items(self, request, context: dict, **kwargs):
        """Return a list of custom dashboard items to be rendered in the InvenTree user interface."""

        # Example: only display for 'staff' users
        if not request.user or not request.user.is_staff:
            return []
        
        items = []

        items.append({
            'key': '{{ cookiecutter.plugin_slug }}-dashboard',
            'title': '{{ cookiecutter.plugin_title }} Dashboard Item',
            'description': 'Custom dashboard item',
            'icon': 'ti:dashboard:outline',
            'source': self.plugin_static_file('Dashboard.js:render{{ cookiecutter.plugin_name }}DashboardItem'),
            'context': {
                # Provide additional context data to the dashboard item
                {%- if "SettingsMixin" in cookiecutter.plugin_mixins.mixin_list %}
                'settings': self.get_settings_dict(),
                {% endif -%}
                'bar': 'foo'
            }
        })

        return items
    {%- endif -%}
    {%- endif -%}
    {%- endif %}
