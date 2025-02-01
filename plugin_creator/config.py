"""Handle config management for the plugin creator tool."""

import appdirs
import json
import os


def config_dir():
    """Return the directory where the plugin creator config file is stored."""

    return appdirs.user_config_dir("inventree-plugin-creator")


def config_file():
    """Return the path to the plugin creator config file."""
    
    return os.path.join(config_dir(), "config.json")


def config_keys() -> list:
    """List of keys we wish to store in the config file.
    
    These can be reasonably expected to be set by the user.
    """
    return [
        'author_name',
        'author_email',
        'license_key',
        'ci_support',
    ]


def load_config() -> dict:
    """Load the plugin creator config file."""
    # Ensure the config directory exists
    os.makedirs(config_dir(), exist_ok=True)

    data = {}

    filename = config_file()
   
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)

            for key in config_keys():
                if key in json_data:
                    data[key] = json_data[key]

    return data


def save_config(data: dict):
    """Save the plugin creator config file."""

    filename = config_file()

    json_data = {}

    for key in config_keys():
        if key in data:
            json_data[key] = data[key]

    with open(filename, 'w') as f:
        json.dump(json_data, f)
