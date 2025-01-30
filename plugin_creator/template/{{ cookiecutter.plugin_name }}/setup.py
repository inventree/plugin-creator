# -*- coding: utf-8 -*-

import importlib
import importlib.util
import os
import setuptools


def get_plugin_version() -> str:
    """Read the plugin version from the source code."""
    module_path = os.path.join(
        os.path.dirname(__file__),
        "{{ cookiecutter.package_name }}",
        "__init__.py"
    )

    spec = importlib.util.spec_from_file_location(
        "{{ cookiecutter.package_name }}",
        module_path
    )

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module) 

    return module.PLUGIN_VERSION

PLUGIN_VERSION = get_plugin_version()

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version=PLUGIN_VERSION,
    author="{{ cookiecutter.author_name }}",
    {%- if cookiecutter.author_email %}
    author_email="{{ cookiecutter.author_email }}",
    {% endif -%}
    description="{{ cookiecutter.plugin_description }}",
    long_description=long_description,
    long_description_content_type='text/markdown',
    {%- if cookiecutter.project_url %}
    url="{{ cookiecutter.project_url }}",
    {% endif -%}
    license="{{ cookiecutter.license_key }}",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        # Enter your plugin library dependencies here
    ],
    setup_requires=[
        "wheel",
        "twine",
    ],
    python_requires=">=3.9",
    entry_points={
        "inventree_plugins": [
            "{{ cookiecutter.plugin_name }} = {{ cookiecutter.package_name }}.plugin:{{ cookiecutter.plugin_name }}"
        ]
    },
)
