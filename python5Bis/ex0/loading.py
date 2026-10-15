import importlib

if __name__ == "__main__":
    names = ["pandas", "numpy"]
    all_present = True
    for name in names:
        try:
            module = importlib.import_module(name)
            print(f"[OK] {name}: ({module.__version__})", end=' - ')
            if name == 'pandas':
                print("Data manipulation ready")
            elif name == 'numpy':
                print("Numerical computation ready")

        except ModuleNotFoundError:
            all_present = False
            print(
                f"\nMissing dependency: {name}\n"
                "Install with pip:\n"
                f"pip install {name}\n"
                "or\n"
                "pip install -r ex0/requirements.txt # For all requirements\n"
                "\nInstall with Poetry:\n"
                f"poetry add {name}\n"
                "or\n"
                "poetry install # For all requirements\n"
            )

    print("\npip vs Poetry:")
    print(
        "requirements.txt declares what to install; "
        "pip resolves it at install time.\n"
        "pyproject.toml declares the same constraints,"
        "and Poetry pins the resolved\n"
        "versions in poetry.lock so every install is identical."
    )

    if all_present:
        print("\nAll reagents present and accounted for.")
