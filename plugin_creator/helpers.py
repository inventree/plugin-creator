"""Helper functions for the InvenTree Plugin Creator."""

import os
import shutil
import sys

import questionary


def pretty_print(*args, color='green'):
    """Print a message with a color."""
    questionary.print(' '.join(args), style=f'fg:{color}')


def error(*args, exit=True):
    """Print an error message."""
    pretty_print(*args, color='red')

    if exit:
        sys.exit(1)


def warning(*args):
    """Print a warning message."""
    pretty_print(*args, color='yellow')


def success(*args):
    """Print a success message."""
    pretty_print(*args, color='green')


def info(*args):
    """Print an info message."""
    pretty_print(*args, color='blue')


def remove_file(*args):
    """Remove a file if it exists."""
    file_path = os.path.join(*args)

    if os.path.exists(file_path) and os.path.isfile(file_path):
        info(f'Removing file: {file_path}')
        os.remove(file_path)


def remove_dir(*args):
    """Remove a directory if it exists."""
    dir_path = os.path.join(*args)

    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        info(f'Removing directory: {dir_path}')
        shutil.rmtree(dir_path)
