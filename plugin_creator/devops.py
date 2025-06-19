"""DevOps support for the plugin creator."""

import os
import shutil
import subprocess

import questionary

from .helpers import info, success


def get_devops_options() -> list:
    """Return a list of available DevOps options."""

    return [
        "None",
        "GitHub Actions",
        "GitLab CI/CD",
    ]


def get_devops_mode() -> str:
    """Ask user to select DevOps mode."""

    return questionary.select(
        "DevOps support (CI/CD)?",
        choices=get_devops_options(),
        default="GitHub Actions"
    ).ask().split()[0].lower()


def cleanup_devops_files(devops_mode: str, plugin_dir: str) -> None:
    """Cleanup generated DevOps files."""

    devops_mode = devops_mode.lower().split()[0]

    # Remove the .github directory
    if devops_mode != "github":
        github_dir = os.path.join(plugin_dir, ".github")

        if os.path.exists(github_dir):
            info("- Removing .github directory")
            shutil.rmtree(github_dir)

    # Remove the .gitlab-ci.yml file
    if devops_mode != "gitlab":
        gitlab_file = os.path.join(plugin_dir, ".gitlab-ci.yml")

        if os.path.exists(gitlab_file):
            info("- Removing .gitlab-ci.yml file")
            os.remove(gitlab_file)


def git_init(plugin_dir: str) -> None:
    """Initialize git repository."""

    info("Initializing git repository...")
    subprocess.run(
        ["git init -b main"],
        check=True,
        shell=True,
        cwd=plugin_dir
    )

    # Intall pre-commit hooks
    info("Installing pre-commit hooks...")

    subprocess.run(
        ["pip install pre-commit"],
        check=True,
        shell=True,
        cwd=plugin_dir
    )

    subprocess.run(
        ["pre-commit install"],
        check=True,
        shell=True,
        cwd=plugin_dir
    )

    success("Git repository initialized and pre-commit hooks installed.")
