# {{ cookiecutter.plugin_title }}- Frontend Code

This directory contains the frontend code for the {{ cookiecutter.plugin_title }} plugin.

## Architecture

The frontend code is designed to integrate natively with the InvenTree user interface.

### Frameworks

We use Mantine, running on React, to match the InvenTree stack.

- [React](https://react.dev/)
- [Mantine](https://mantine.dev/)

### Project Setup

This project uses [Vite](https://vitejs.dev/) as the build tool. We followed [this guide](https://vitejs.dev/guide/#scaffolding-your-first-vite-project) to scaffold the project.

### Building

*Note: Assumed you are already in the `frontend` directory.*

To compile the frontend code, run:

```bash
npm run build --emptyOutDir
```

This will compile the frontend into the `../{{ cookiecutter.package_name}}/static` directory (ready for distribution).

Note: The target directory is intentionally outside of the frontend directory, so that the compiled files are correctly bundled into the python package install.

### Testing

To test the frontend code, run:

```bash
npm run dev
```

This will start a development server (usually on `localhost:5173`) which will automatically reload when changes are made to the source code.

The development server provides some "dummy" harness data to test the frontend code.
