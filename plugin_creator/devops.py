"""DevOps support for the plugin creator."""

import subprocess

import questionary

from .helpers import info, remove_dir, remove_file, success


def get_devops_options() -> list:
    """Return a list of available DevOps options."""
    return ['None', 'GitHub Actions', 'GitLab CI/CD']


def get_devops_mode() -> str:
    """Ask user to select DevOps mode."""
    return (
        questionary.select(
            'DevOps support (CI/CD)?',
            choices=get_devops_options(),
            default='GitHub Actions',
        )
        .ask()
        .split()[0]
        .lower()
    )


def cleanup_devops_files(devops_mode: str, plugin_dir: str) -> None:
    """Cleanup generated DevOps files."""
    devops_mode = devops_mode.lower().split()[0]

    # Remove the .github directory
    if devops_mode != 'github':
        remove_dir(plugin_dir, '.github')

    # Remove the .gitlab-ci.yml file
    if devops_mode != 'gitlab':
        remove_file(plugin_dir, '.gitlab-ci.yml')


def git_init(plugin_dir: str) -> None:
    """Initialize git repository."""
    info('Initializing git repository...')
    subprocess.run(['git init -b main'], check=True, shell=True, cwd=plugin_dir)

    # Intall pre-commit hooks
    info('Installing pre-commit hooks...')

    subprocess.run(['pip install pre-commit'], check=True, shell=True, cwd=plugin_dir)

    subprocess.run(['pre-commit install'], check=True, shell=True, cwd=plugin_dir)

    success('Git repository initialized and pre-commit hooks installed.')
