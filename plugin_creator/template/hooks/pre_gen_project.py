# Custom hook which runs before the project is generated


from collections import OrderedDict

data = {{ cookiecutter }}

# Debug if needed
if False:
    print("Cookiecutter data:")
    for k, v in data.items():
        print(f" - {k}: {v}")
