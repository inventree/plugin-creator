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

    # Optionally specify supported InvenTree versions
    # MIN_VERSION = '0.18.0'
    # MAX_VERSION = '2.0.0'

    {% if "UserInterfaceMixin" in cookiecutter.plugin_mixins.mixin_list -%}
    {%- if cookiecutter.frontend.features.settings -%}
    # Render custom UI elements to the plugin settings page
    ADMIN_SOURCE = "Settings.js:renderPluginSettings"
    {%- endif -%}
    {%- endif -%}

    {%- if cookiecutter.plugin_mixins.mixin_list %}
    {% if "ScheduleMixin" in cookiecutter.plugin_mixins.mixin_list %}
    # Scheduled tasks (from ScheduleMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/schedule/
    SCHEDULED_TASKS = {
        # Define your scheduled tasks here...
    }
    {%- endif %}
    {% if "SettingsMixin" in cookiecutter.plugin_mixins.mixin_list %}
    # Plugin settings (from SettingsMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/settings/
    SETTINGS = {
        # Define your plugin settings here...
        'CUSTOM_VALUE': {
            'name': 'Custom Value',
            'description': 'A custom value',
            'validator': int,
            'default': 42,
        }
    }
    {%- endif %}
    {% if "CurrencyExchangeMixin" in cookiecutter.plugin_mixins.mixin_list %}
    # Support for currency exchange rates (from CurrencyExchangeMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/currency/
    def update_exchange_rates(self, base_currency: str, symbols: list[str]) -> dict:
        """Update currency exchange rates for InvenTree."""
        # Example implementation
        return {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.75,
        }
    {%- endif %}
    {% if "EventMixin" in cookiecutter.plugin_mixins.mixin_list %}
    # Respond to InvenTree events (from EventMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/event/
    def wants_process_event(self, event: str) -> bool:
        """Return True if the plugin wants to process the given event."""
        # Example: only process the 'create part' event
        return event == 'part_part.created'
    
    def process_event(self, event: str, *args, **kwargs) -> None:
        """Process the provided event."""
        print("Processing custom event:", event)
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)
    {%- endif %}
    {% if "LocateMixin" in cookiecutter.plugin_mixins.mixin_list %}
    # Perform custom locate operations (from LocateMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/locate/
    def locate_stock_item(self, item_id: int):
        """Attempt to locate a particular StockItem."""
        ...

    def locate_stock_location(self, location_id: int):
        """Attempt to locate a particular StockLocation."""
        ...
    {%- endif %}
    {% if "ReportMixin" in cookiecutter.plugin_mixins.mixin_list %}
    # Custom report context (from ReportMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/report/
    def add_label_context(self, label_instance, model_instance, request, context, **kwargs):
        """Add custom context data to a label rendering context."""
        
        # Add custom context data to the label rendering context
        context['foo'] = 'label_bar'

    def add_report_context(self, report_instance, model_instance, request, context, **kwargs):
        """Add custom context data to a report rendering context."""
        
        # Add custom context data to the report rendering context
        context['foo'] = 'report_bar'

    def report_callback(self, template, instance, report, request, **kwargs):
        """Callback function called after a report is generated."""
        ...

    {%- endif %}
    {% if "UrlsMixin" in cookiecutter.plugin_mixins.mixin_list %}
    # Custom URL endpoints (from UrlsMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/urls/
    def setup_urls(self):
        """Configure custom URL endpoints for this plugin."""
        from django.urls import path
        from .views import ExampleView

        return [
            # Provide path to a simple custom view - replace this with your own views
            path('example/', ExampleView.as_view(), name='example-view'),
        ]

    {%- endif %}
    {% if "UserInterfaceMixin" in cookiecutter.plugin_mixins.mixin_list %}

    # User interface elements (from UserInterfaceMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/ui/
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
    {%- if "ValidationMixin" in cookiecutter.plugin_mixins.mixin_list %}

    # Custom data validation (from ValidationMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/validation/
    def validate_model_deletion(self, instance, **kwargs):
        """Run custom validation when a model instance is being deleted."""
        ...

    def validate_model_instance(self, instance, deltas=None, **kwargs):
        """Run custom validation on a database model instance."""
        ...
    
    def validate_part_name(self, name, part, **kwargs):
        """Perform validation on a proposed Part name."""
        ...

    def validate_part_ipn(self, ipn, part, **kwargs):
        """Perform validation on a proposed Part IPN."""
        ...

    def validate_part_parameter(self, parameter, data, **kwargs):
        """Perform validation on a proposed Part parameter."""
        ...

    def validate_batch_code(self, batch_code, stock_item, **kwargs):
        """Perform validation on a proposed StockItem batch code."""
        ...

    def generate_batch_code(self, **kwargs):
        """Generate a new StockItem batch code."""
        ...

    def validate_serial_number(self, serial, part, stock_item, **kwargs):
        """Perform validation on a proposed StockItem serial number."""
        ...

    def convert_serial_to_int(self, serial, **kwargs) -> int:
        """Convert a serial number to an integer value."""
        return None
        
    def get_latest_serial_number(self, part, **kwargs):
        """Return the latest serial number for a given part."""
        return None

    def increment_serial_number(self, serial, part=None, **kwargs):
        """Increment a serial number."""
        return None
    {%- endif %}
