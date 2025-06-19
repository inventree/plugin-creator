"""DevOps support for the plugin creator."""

import os
import shutil

import questionary

from .helpers import info


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
    os.system(f"git init --initial-branch=main {plugin_dir}")

    # Add all files to the staging area
    os.system(f"git -C {plugin_dir} add .")

    # Commit the changes
    os.system(f"git -C {plugin_dir} commit -m 'Initial plugin commit'")

    # Intall pre-commit hooks
    os.system("pip install pre-commit")
    os.system("pre-commit install")
