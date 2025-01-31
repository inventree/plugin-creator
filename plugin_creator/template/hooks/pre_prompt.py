# custom hook which runs before user input is gathered

import os
import shutil

# Paths to ignore / expunge from the generated directory structure
# We want to be *very sure* that these files are not present!
paths_to_remove = [
    ["{{ cookiecutter.plugin_name }}", "frontend", "node_modules"],
    ["{{ cookiecutter.plugin_name }}", "frontend", "package-lock.json"],
]

here = os.getcwd()

for path in paths_to_remove:
    path = os.path.join(here, *path)

    if os.path.exists(path):
        print(f"- Removing path: {path}")
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)
