
import argparse
import json
import os

import license
import questionary
from cookiecutter.main import cookiecutter

from . import PLUGIN_CREATOR_VERSION

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
    """Gather project information from the user."""

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

    # Check if we want to add frontend code support
    if questionary.confirm(
        "Add User Interface support?",
        default="UserInterfaceMixin" in plugin_mixins
    ).ask():
        defaults = context.get("frontend", {}).get("packages", None)
        context["frontend"] = {
            "enabled": True,
            # Extra frontend options
            "packages": frontend.select_packages(defaults=defaults),
            "features": frontend.select_features()
        }
    else:
        context["frontend"] = {
            "enabled": False,
            "packages": [],
            "features": frontend.no_features()
        }

    # Devops information
    info("Enter plugin devops support information:")

    context['ci_support'] = devops.get_devops_mode()

    return context


def cleanup(plugin_dir: str, context: dict, skip_install: bool = False) -> None:
    """Cleanup generated files after cookiecutter runs."""
    
    info("Cleaning up generated files...")

    devops.cleanup_devops_files(context['ci_support'], plugin_dir)

    if context['frontend']['enabled']:
        if not skip_install:
            frontend.update_frontend(
                plugin_dir,
                additional_packages=context['frontend']['packages'] or None
            )
    else:
        frontend.remove_frontend(plugin_dir)


def main():
    """Run plugin scaffolding."""

    parser = argparse.ArgumentParser(description="InvenTree Plugin Creator Tool")
    parser.add_argument("--default", action="store_true", help="Use default values for all prompts (non-interactive mode)")
    parser.add_argument('--output', action='store', help='Specify output directory', default='.')
    parser.add_argument('--skip-install', action='store_true', help='Do not install frontend dependencies')
    parser.add_argument('--version', action='version', version=f'%(prog)s {PLUGIN_CREATOR_VERSION}')
    
    args = parser.parse_args()

    info("InvenTree Plugin Creator Tool")

    context = default_values()

    context["plugin_creator_version"] = PLUGIN_CREATOR_VERSION

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
    cleanup(plugin_dir, context, skip_install=args.skip_install)

    success(f"Plugin created -> '{output_dir}'")


if __name__ == "__main__":
    main()
