# -*- coding: utf-8 -*-

import importlib
import importlib.util
import os
import setuptools

# Read version number from source code
module_path = os.path.join(os.path.dirname(__file__), "plugin_creator", "__init__.py")
spec = importlib.util.spec_from_file_location("plugin_creator", module_path)
plugin_loader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plugin_loader)

PLUGIN_CREATOR_VERSION = plugin_loader.PLUGIN_CREATOR_VERSION

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="inventree-plugin-creator",
    version=plugin_loader.PLUGIN_CREATOR_VERSION,
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
        'license',
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
