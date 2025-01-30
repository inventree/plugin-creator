# -*- coding: utf-8 -*-

import setuptools

PLUGIN_CREATOR_VERSION = "0.1.0"

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="inventree-plugin-creator",
    version=PLUGIN_CREATOR_VERSION,
    author="Oliver Walters",
    author_email="oliver.henry.walters@gmail.com",
    description="InvenTree plugin creator",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="inventree plugin scaffold",
    url="https://github.com/inventree/plugin-creator",
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'cookiecutter',
        'questionary',
    ],
    setup_requires=[
        "wheel",
        "twine",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "create-inventree-plugin = plugin_creator.cli:main"
        ]
    }
)
