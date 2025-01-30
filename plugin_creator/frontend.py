"""Frontend code generation options for the plugin creator."""

import os
import subprocess

from .helpers import info


def update_frontend(plugin_dir: str, install=True) -> None:
    """Update the frontend code for the plugin."""

    frontend_dir = os.path.join(plugin_dir, "frontend")

    info("- Updating frontend dependencies...")

    # Run npm update
    subprocess.run(["npm", "update"], cwd=frontend_dir)

    if install:
        info("- Installing frontend dependencies...")
        subprocess.run(["npm", "install"], cwd=frontend_dir)
