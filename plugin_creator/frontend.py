"""Frontend code generation options for the plugin creator."""

import os
import subprocess

import questionary
from questionary.prompts.common import Choice

from .helpers import info


def remove_frontend(plugin_dir: str) -> None:
    """If frontend code is not required, remove it!"""

    frontend_dir = os.path.join(plugin_dir, "frontend")

    if os.path.exists(frontend_dir):
        info("- Removing frontend code...")
        subprocess.run(["rm", "-r", frontend_dir])


def update_frontend(plugin_dir: str, packages: list = None) -> None:
    """Update the frontend code for the plugin."""

    if not packages:
        return

    info("- Installing frontend dependencies...")

    frontend_dir = os.path.join(plugin_dir, "frontend")

    pkg = ' '.join([f'{package}@latest' for package in packages])

    info(f"-- installing {pkg}")
    subprocess.run(["npm", "install", pkg], cwd=frontend_dir)
    subprocess.run(["npm", "update"], cwd=frontend_dir)


def available_packages() -> list:
    """List of default frontend packages to install."""

    return [
        "react",
        "@mantine/core",
        "@mantine/hooks",
        "@mantine/charts",
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
