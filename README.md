[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/inventree-plugin-creator)](https://pypi.org/project/inventree-plugin-creator/)

# InvenTree Plugin Creator

Command line tool for scaffolding a new InvenTree plugin.

## Description

This is a command line tool which allows for rapid scaffolding of a new InvenTree plugin.

It uses the [cookiecutter project](https://cookiecutter.readthedocs.io/en/stable/) to generate a new project, based on a custom project template.

## Installation

To install the plugin creator, run:

```bash
pip install -U inventree-plugin-creator
```

## Usage

To create a new plugin, run:

```bash
create-inventree-plugin
```

This will prompt you for required information about the plugin you wish to create.

To view the available options, run:

```bash
create-inventree-plugin --help
```

## Frontend Features

If you are developing a plugin which provides frontend (UI) features, after creating the initial plugin, run the following commands to install and build the initial version of the frontend code:

```bash
cd <myplugin>/frontend
npm install
npm run build
```

This will compile frontend code into the `<myplugin>/static` directory - ready to be packaged and distributed with the python plugin code.

*Note: You must run `npm run build` each time before building and distributing the plugin.*