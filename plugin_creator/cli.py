
import argparse
import json
import os

import license
import questionary
from cookiecutter.main import cookiecutter

from . import PLUGIN_CREATOR_VERSION

from . import config
from . import devops
from . import frontend
from . import mixins
from . import validators

from .helpers import info, success


def default_values() -> dict:
    """Read default values out from the cookiecutter.json file."""
    fn = os.path.join(
        os.path.dirname(__file__),
        "template",
        "cookiecutter.json"
    )

    with open(fn, "r") as f:
        return json.load(f)


def gather_info(context: dict) -> dict:
    """Gather project information from the user.
    
    There are some conventions regarding naming:

    - Plugin title: The human-readable name of the plugin (e.g., "Custom Plugin").
    - Plugin name: The Python class name for the plugin (e.g., "CustomPlugin").
    - Plugin slug: A URL-friendly version of the plugin title (e.g., "custom-plugin").
    - Package name: The Python package name for the plugin (e.g., "custom_plugin").
    - Distribution name: The name used for the Python package distribution (e.g., "inventree-custom-plugin").
    """

    info("Enter project information:")

    # Basic project information
    context['plugin_title'] = questionary.text(
        "Enter plugin name",
        default=context['plugin_title'],
        validate=validators.ProjectNameValidator,
    ).ask().strip()

    context['plugin_description'] = questionary.text(
        "Enter plugin description",
        default=context['plugin_description'],
        validate=validators.NotEmptyValidator,
    ).ask().strip()

    context['plugin_name'] = context['plugin_title'].replace(" ", "")

    # Convert the project name to a package name
    # e.g. 'Custom Plugin' -> 'custom_plugin'
    context['plugin_slug'] = context['plugin_title'].replace(" ", "-").lower()
    context['package_name'] = context['plugin_slug'].replace("-", "_")

    # Convert the package slug to a distribution name
    # e.g. 'custom-plugin' -> 'inventree-custom-plugin'
    pkg = context['plugin_slug']
    
    if not pkg.startswith("inventree-"):
        pkg = f"inventree-{pkg}"

    context['distribution_name'] = pkg

    success(f"Generating plugin '{context['package_name']}' - {context['plugin_description']}")

    info("Enter author information:")

    context['author_name'] = questionary.text(
        "Author name",
        default=context['author_name'],
        validate=validators.NotEmptyValidator,
    ).ask().strip()

    context["author_email"] = questionary.text(
        "Author email",
        default=context["author_email"],
    ).ask().strip()

    context["project_url"] = questionary.text(
        "Project URL",
        default=context['project_url'],
    ).ask().strip()

    # Extract license information
    available_licences = [lic for lic in license.iter()]
    license_keys = [lic.id for lic in available_licences]

    context['license_key'] = questionary.select(
        "Select a license",
        default="MIT",
        choices=license_keys,
    ).ask()

    context['license_text'] = license.find(
        context['license_key']
    ).render(
        name=context['author_name'],
        email=context['author_email'],
    )

    # Plugin structure information
    info("Enter plugin structure information:")

    plugin_mixins = mixins.get_mixins()

    context['plugin_mixins'] = {
        'mixin_list': plugin_mixins
    }

    # If we want to add frontend code support
    if 'UserInterfaceMixin' in plugin_mixins:
        context["frontend"] = {
            "enabled": True,
            "features": frontend.select_features()
        }
    else:
        context["frontend"] = {
            "enabled": False,
            "features": frontend.no_features()
        }

    # Devops information
    info("Enter plugin devops support information:")

    git_support = context["git_support"] = questionary.confirm(
        "Enable Git integration?",
        default=True,
    ).ask()

    context['ci_support'] = devops.get_devops_mode() if git_support else "None"

    return context


def cleanup(plugin_dir: str, context: dict) -> None:
    """Cleanup generated files after cookiecutter runs."""
    
    info("Cleaning up generated files...")

    devops.cleanup_devops_files(context['ci_support'], plugin_dir)

    # Remove frontend code entirely if not enabled
    if context['frontend']['enabled']:
        frontend.update_frontend(
            plugin_dir,
            context['frontend']['features'] or []
        )
    else:
        frontend.remove_frontend(plugin_dir)

    # Cleanup mixins
    mixins.cleanup_mixins(plugin_dir, context)

    if context["git_support"]:
        devops.git_init(plugin_dir)


def main():
    """Run plugin scaffolding."""

    parser = argparse.ArgumentParser(description="InvenTree Plugin Creator Tool")
    parser.add_argument("--default", action="store_true", help="Use default values for all prompts (non-interactive mode)")
    parser.add_argument('--output', action='store', help='Specify output directory', default='.')
    parser.add_argument('--version', action='version', version=f'%(prog)s {PLUGIN_CREATOR_VERSION}')
    
    args = parser.parse_args()

    info("InvenTree Plugin Creator Tool")

    context = default_values()
    context.update(config.load_config())

    # Set version information
    context["plugin_creator_version"] = PLUGIN_CREATOR_VERSION

    context["frontend"]["react_version"] = frontend.REACT_VERSION
    context["frontend"]["mantine_version"] = frontend.MANTINE_VERSION

    if args.default:
        info("- Using default values for all prompts")
    else:
        context = gather_info(context)

    src_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "template"
    )

    output_dir = os.path.abspath(args.output)
    plugin_dir = os.path.join(output_dir, context['plugin_name'])

    # Save the user config
    config.save_config(context)

    info("- output:", plugin_dir)

    # Run cookiecutter template
    cookiecutter(
        src_path,
        no_input=True,
        output_dir=output_dir,
        extra_context=context,
        overwrite_if_exists=True
    )

    # Cleanup files after cookiecutter runs
    cleanup(plugin_dir, context)

    success(f"Plugin created -> '{plugin_dir}'")


if __name__ == "__main__":
    main()
