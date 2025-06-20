"""InvenTree plugin mixin selection."""

import questionary
from questionary.prompts.common import Choice


def available_mixins() -> list:
    """Return a list of available plugin mixin classes."""

    # TODO: Support the commented out mixins

    return [
        # 'ActionMixin',
        # 'APICallMixin',
        # 'AppMixin',
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
