
import argparse
import os

import license
import questionary
from cookiecutter.main import cookiecutter


from .helpers import error, info, success, warning
from . import mixins
from . import validators


def gather_info() -> dict:
    """Gather project information from the user."""

    context = {}

    info("Enter project information:")

    # Basic project information
    context['plugin_title'] = questionary.text(
        "Enter plugin name",
        default="Custom InvenTree Plugin",
        validate=validators.ProjectNameValidator,
    ).ask().strip()

    context['plugin_description'] = questionary.text(
        "Enter plugin description",
        default="A custom InvenTree plugin",
        validate=validators.NotEmptyValidator,
    ).ask().strip()

    context['plugin_name'] = context['plugin_title'].replace(" ", "")

    # Convert the project name to a package name
    # e.g. 'Custom Plugin' -> 'custom_plugin'
    context['plugin_slug'] = context['plugin_title'].replace(" ", "-").lower()
    context['package_name'] = context['plugin_slug'].replace("-", "_")

    success(f"Generating plugin '{context['plugin_title']}' - {context['plugin_description']}")
    info(f" - Package Name: {context['package_name']}")

    info("Enter author information:")

    context['author_name'] = questionary.text(
        "Author name",
        default="John Doe",
        validate=validators.NotEmptyValidator,
    ).ask().strip()

    context["author_email"] = questionary.text(
        "Author email",
        default="email@domain.org",
    ).ask().strip()

    context["project_url"] = questionary.text(
        "Project URL",
        default="",
    ).ask().strip()

    # Extract license information
    available_licences = [l for l in license.iter()]
    license_keys = [l.id for l in available_licences]

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

    context['plugin_mixins'] = {
        'mixin_list': questionary.checkbox(
            "Select plugin mixins",
            choices=mixins.available_mixins(),
        ).ask()
    }

    return context

def main():
    """Run plugin scaffolding."""

    parser = argparse.ArgumentParser(description="InvenTree Plugin Creator Tool")
    parser.add_argument("--default", action="store_true", help="Use default values for all prompts (non-interactive mode)")
    parser.add_argument("--template", action="store", help="Specify input template file")
    parser.add_argument('--output', action='store', help='Specify output directory', default='.')

    args = parser.parse_args()

    info("InvenTree Plugin Creator Tool")

    if args.default:
        info("Using default values for all prompts...")
        context = {}
        output_dir = os.path.join(args.output, "MyCustomPlugin")
    else:
        context = gather_info()
        output_dir = os.path.join(args.output, context['plugin_name'])

    # Run cookiecutter template
    cookiecutter(
        args.template,
        no_input=True,
        output_dir=output_dir,
        extra_context=context,
        overwrite_if_exists=True
    )

    success(f"Plugin created -> '{output_dir}'")

if __name__ == "__main__":
    main()
