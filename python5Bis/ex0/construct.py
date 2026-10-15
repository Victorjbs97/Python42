import sys
import os
import site


def ft_no_ve_status() -> None:
    print("\nLABORATORY STATUS: You are working in the open\n")

    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.\n")

    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate # On Unix")
    print("lab_env\\Scripts\\activate # On Windows\n")

    print("Then run this program again.")


def ft_with_ve_status() -> None:
    name_ve = os.path.basename(sys.prefix)
    print("\nLABORATORY STATUS: The laboratory is sealed\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {name_ve}")
    print(f"Environment Path: {sys.prefix}\n")

    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting")
    print("the global system.")

    print("\nReagent installation path:")
    print(site.getsitepackages()[0])


if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        ft_with_ve_status()
    else:
        ft_no_ve_status()
