#!/bin/env python3
import sys
import os
import site

if sys.prefix == sys.base_prefix:
    print("\nMATRIX STATUS: You’re still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You’re in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:\n"
          "python -m venv matrix_env"
          "source matrix_env/bin/activate # On Unix\n"
          "matrix_env\\Scripts\\activate # On Windows\n"
          "Then run this program again.")
else:
    venv_path: str | None = os.environ.get("VIRTUAL_ENV")
    print("\nMATRIX STATUS: Welcome to the construct")
    print("Current Python:", sys.executable)
    if isinstance(venv_path, str):
        print("Virtual Environment:", os.path.basename(venv_path))
    print("Environment Path:", venv_path)
    print("\nSUCCESS: You’re in an isolated environment!\n"
          "Safe to install packages without affecting\n"
          "the global system.\n")
    print("Package installation path:", site.getsitepackages()[0])
