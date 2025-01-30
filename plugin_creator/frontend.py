"""Frontend code generation options for the plugin creator."""

import os
import subprocess

from .helpers import info

def remove_frontend(plugin_dir: str) -> None:
    """If frontend code is not required, remove it!"""

    frontend_dir = os.path.join(plugin_dir, "frontend")

    if os.path.exists(frontend_dir):
        info("- Removing frontend code...")
        subprocess.run(["rm", "-r", frontend_dir])


def update_frontend(plugin_dir: str, install=True) -> None:
    """Update the frontend code for the plugin."""

    frontend_dir = os.path.join(plugin_dir, "frontend")

    info("- Updating frontend dependencies...")

    # Run npm update
    subprocess.run(["npm", "update"], cwd=frontend_dir)

    if install:
        info("- Installing frontend dependencies...")
        subprocess.run(["npm", "install"], cwd=frontend_dir)
