"""Frontend code generation options for the plugin creator."""

import questionary
from questionary.prompts.common import Choice

from .helpers import info
from .helpers import remove_file, remove_dir


# Minimum version requirements for core frontend libraries
MIN_REACT_VERSION = "19.1.1"
MIN_MANTINE_VERSION = "8.2.7"


def frontend_features() -> dict:
    """Provide a list of frontend features to enable."""

    return {
        "dashboard": "Custom dashboard items",
        "panel": "Custom panel items",
        "settings": "Custom settings display",
    }


def all_features() -> dict:
    """Select all features by default."""
    return {key: True for key in frontend_features().keys()}


def no_features() -> dict:
    """Select no features by default."""
    return {key: False for key in frontend_features().keys()}


def enable_translation() -> bool:
    """Ask the user if they want to enable translation support."""
    return questionary.confirm(
        "Enable translation support?",
        default=True,
    ).ask()


def select_features() -> dict:
    """Select which frontend features to enable."""

    choices = [
        Choice(
            title=title,
            checked=True,
        )
        for title in frontend_features().values()
    ]

    selected = questionary.checkbox(
        "Select frontend features to enable", choices=choices
    ).ask()

    selected_keys = [
        key for key, value in frontend_features().items() if value in selected
    ]

    return {key: key in selected_keys for key in frontend_features().keys()}


def remove_frontend(plugin_dir: str) -> None:
    """If frontend code is not required, remove it!"""
    remove_dir(plugin_dir, "frontend")


def define_frontend(enabled: bool, defaults: bool = False) -> dict:
    """Define the frontend code options for the plugin."""

    frontend = {
        "react_version": MIN_REACT_VERSION,
        "mantine_version": MIN_MANTINE_VERSION,
    }

    if enabled:
        frontend.update({
            "enabled": True,
            "features": all_features() if defaults else select_features(),
            "translation": True if defaults else enable_translation(),
        })
    else:
        frontend.update({
            "enabled": False,
            "translation": False,
            "features": no_features(),
        })

    return frontend


def update_frontend(plugin_dir: str, context: dict) -> None:
    """Update the frontend code for the plugin."""

    info("Cleaning up frontend files...")

    features = context["frontend"]["features"] or []
    translation = context["frontend"].get("translation", False)

    # Remove features which are not needed
    for feature in frontend_features().keys():
        if not features.get(feature, False):
            info(f"- Removing unused frontend feature: {feature}")

            remove_file(plugin_dir, "frontend", "src", f"{feature.capitalize()}.tsx")

    if not translation:
        remove_dir(plugin_dir, "frontend", "src", "locales")
        remove_file(plugin_dir, "frontend", "src", "locales.tsx")
        remove_file(plugin_dir, "frontend", ".linguirc")
