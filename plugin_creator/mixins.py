"""InvenTree plugin mixin selection."""

import os

import questionary
from questionary.prompts.common import Choice

from .helpers import info, remove_dir, remove_file


def available_mixins() -> list:
    """Return a list of available plugin mixin classes."""
    # TODO: Support the commented out mixins

    return [
        # 'ActionMixin',
        # 'APICallMixin',
        'AppMixin',
        # 'BarcodeMixin',
        'CurrencyExchangeMixin',
        'EventMixin',
        # 'DataExportMixin',
        # 'IconPackMixin',
        # 'LabelPrintingMixin',
        'LocateMixin',
        # 'MailMixin',
        # 'NavigationMixin',
        # 'NotificationMixin',
        'ReportMixin',
        'ScheduleMixin',
        'SettingsMixin',
        # 'SupplierBarcodeMixin',
        'UrlsMixin',
        'UserInterfaceMixin',
        'ValidationMixin',
    ]


def get_mixins() -> list:
    """Ask user to select plugin mixins."""
    # Default mixins to select
    defaults = ['SettingsMixin', 'UserInterfaceMixin']

    choices = [
        Choice(title=title, checked=title in defaults) for title in available_mixins()
    ]

    return questionary.checkbox('Select plugin mixins', choices=choices).ask()


def cleanup_mixins(plugin_dir: str, context: dict) -> list:
    """Post-build step to remove certain files based on selected mixins."""
    info('Cleaning up Python files...')

    mixins = context['plugin_mixins']['mixin_list']

    src_dir = os.path.join(plugin_dir, context['package_name'])

    if 'AppMixin' not in mixins:
        # Remove files associated with the AppMixin
        remove_dir(src_dir, 'migrations')
        remove_file(src_dir, 'apps.py')
        remove_file(src_dir, 'admin.py')
        remove_file(src_dir, 'models.py')

    if 'UrlsMixin' not in mixins:
        # Remove files associated with the UrlsMixin
        remove_file(src_dir, 'serializers.py')
        remove_file(src_dir, 'views.py')
