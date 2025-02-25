"""Frontend code generation options for the plugin creator."""

import os
import subprocess

import questionary
from questionary.prompts.common import Choice

from .helpers import info

# Major versions of base packages
# Bump these if the InvenTree core frontend is updated
REACT_VERSION = 18
MANTINE_VERSION = 7


def enforced_packages() -> list:
    """List of frontend packages that are always installed."""

    return [
        f"react@^{REACT_VERSION}",
        f"react-dom@^{REACT_VERSION}",
        f"@mantine/core@^{MANTINE_VERSION}",
    ]


def available_packages() -> list:
    """List of additional frontend packages to install."""

    return [
        f"@mantine/hooks@^{MANTINE_VERSION}",
        f"@mantine/charts@^{MANTINE_VERSION}",
        "@tabler/icons-react@latest",
    ]


def select_packages(defaults: list = None) -> list:
    """Select which packages to install."""

    choices = [
        Choice(
            title=package,
            checked=package in defaults if defaults else False,
        ) for package in available_packages()
    ]

    return questionary.checkbox(
        "Select frontend packages to install",
        choices=choices
    ).ask()


def frontend_features() -> dict:
    """Provide a list of frontend features to enable."""

    return {
        "dashboard": "Custom dashboard items",
        "panel": "Custom panel items",
    }


def all_features() -> dict:
    """Select all features by default."""
    return {
        key: True for key in frontend_features().keys()
    }


def no_features() -> dict:
    """Select no features by default."""
    return {
        key: False for key in frontend_features().keys()
    }


def select_features() -> dict:
    """Select which frontend features to enable."""

    choices = [
        Choice(
            title=title,
            checked=True,
        ) for title in frontend_features().values()
    ]

    selected = questionary.checkbox(
        "Select frontend features to enable",
        choices=choices
    ).ask()

    selected_keys = [key for key, value in frontend_features().items() if value in selected]

    return {
        key: key in selected_keys for key in frontend_features().keys()
    }


def remove_frontend(plugin_dir: str) -> None:
    """If frontend code is not required, remove it!"""

    frontend_dir = os.path.join(plugin_dir, "frontend")

    if os.path.exists(frontend_dir):
        info("- Removing frontend code...")
        subprocess.run(["rm", "-r", frontend_dir])


def update_frontend(plugin_dir: str, features: list, additional_packages: list) -> None:
    """Update the frontend code for the plugin."""

    # Remove features which are not needed
    for feature in frontend_features().keys():
        if not features.get(feature, False):
            info(f"- Removing unused frontend feature: {feature}")

            frontend_file = os.path.abspath(os.path.join(
                plugin_dir,
                'frontend',
                'src',
                f'{feature.capitalize()}.tsx'
            ))

            if os.path.exists(frontend_file):
                subprocess.run(["rm", frontend_file])

    # These packages are *always* installed
    packages = enforced_packages()

    if additional_packages:
        packages += additional_packages

    info("- Installing frontend dependencies...")

    frontend_dir = os.path.join(plugin_dir, "frontend")

    for pkg in packages:
        info(f"-- installing {pkg}")
        subprocess.run(["npm", "install", pkg], cwd=frontend_dir)

    subprocess.run(["npm", "update"], cwd=frontend_dir)
