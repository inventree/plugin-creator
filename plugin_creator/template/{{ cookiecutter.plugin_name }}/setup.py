# -*- coding: utf-8 -*-

import setuptools

from src.{{ cookiecutter.package_name }} import PLUGIN_VERSION

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
        # Enter your dependencies here
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
