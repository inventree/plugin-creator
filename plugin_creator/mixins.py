"""InvenTree plugin mixin selection."""

import os
import shutil

import questionary
from questionary.prompts.common import Choice

from .helpers import info


def available_mixins() -> list:
    """Return a list of available plugin mixin classes."""

    # TODO: Support the commented out mixins

    return [
        # 'ActionMixin',
        # 'APICallMixin',
        'AppMixin',
        # 'BarcodeMixin',
        # 'BulkNotificationMethod',
        # 'CurrencyExchangeMixin',
        'EventMixin',
        # 'DataExportMixin',
        # 'IconPackMixin',
        # 'LabelPrintingMixin',
        'LocateMixin',
        # 'MailMixin',
        # 'NavigationMixin',
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
        Choice(
            title=title,
            checked=title in defaults,
        ) for title in available_mixins()
    ]

    return questionary.checkbox(
        "Select plugin mixins",
        choices=choices
    ).ask()


def cleanup_mixins(plugin_dir: str, context: dict) -> list:
    """Post-build step to remove certain files based on selected mixins."""

    mixins = context['plugin_mixins']['mixin_list']

    src_dir = os.path.join(
        plugin_dir,
        context['package_name'],
    )

    to_remove = []

    if "AppMixin" not in mixins:
        # Remove files associated with the AppMixin
        to_remove.extend([
            'migrations',
            'apps.py',
            'admin.py',
            'models.py',
        ])

    if "UrlsMixin" not in mixins:
        # Remove files associated with the UrlsMixin
        to_remove.extend([
            'serializers.py',
            'views.py',
        ])

    for fn in to_remove:
        file_path = os.path.join(src_dir, fn)
        if os.path.exists(file_path):

            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
                info(f"- Removed dir  {file_path}")
            else:
                os.remove(file_path)
                info(f"- Removed file {file_path}")
