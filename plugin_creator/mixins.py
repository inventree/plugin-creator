"""InvenTree plugin mixin selection."""

import questionary


def available_mixins() -> list:
    """Return a list of available plugin mixin classes."""

    # TODO: Support the commented out mixins

    return [
        # 'APICallMixin',
        # 'ActionMixin',
        # 'AppMixin',
        # 'BarcodeMixin',
        # 'BulkNotificationMethod',
        # 'CurrencyExchangeMixin',
        'EventMixin',
        # 'IconPackMixin',
        # 'LabelPrintingMixin',
        # 'LocateMixin',
        # 'NavigationMixin',
        'ReportMixin',
        'ScheduleMixin',
        'SettingsMixin',
        # 'SupplierBarcodeMixin',
        # 'UrlsMixin',
        'UserInterfaceMixin',
        # 'ValidationMixin',
    ]


def get_mixins() -> list:
    """Ask user to select plugin mixins."""

    return questionary.checkbox(
        "Select plugin mixins",
        choices=available_mixins(),
        default="SettingsMixin"
    ).ask()
