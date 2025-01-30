"""InvenTree plugin mixin selection."""


def available_mixins() -> list:
    """Return a list of available plugin mixin classes."""
    return [
        'APICallMixin',
        'ActionMixin',
        'AppMixin',
        'BarcodeMixin',
        # 'BulkNotificationMethod',
        'CurrencyExchangeMixin',
        'EventMixin',
        'IconPackMixin',
        'LabelPrintingMixin',
        'LocateMixin',
        # 'NavigationMixin',
        'ReportMixin',
        'ScheduleMixin',
        'SettingsMixin',
        # 'SingleNotificationMethod',
        'SupplierBarcodeMixin',
        'UrlsMixin',
        'UserInterfaceMixin',
        'ValidationMixin',
    ]