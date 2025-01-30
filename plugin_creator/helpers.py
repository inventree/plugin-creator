import questionary
import sys


def pretty_print(*args, color='green'):
    """Print a message with a color."""
    questionary.print(" ".join(args), style=f'fg:{color}')


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
