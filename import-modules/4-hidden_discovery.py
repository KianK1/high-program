#!/usr/bin/python3
import importlib.util
import sys
import os

def print_module_names():
    module_name = "hidden_4"
    pyc_path = "./hidden_4.pyc"

    if not os.path.exists(pyc_path):
        print(f"Error: {pyc_path} not found.")
        sys.exit(1)

    spec = importlib.util.spec_from_file_location(module_name, pyc_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = [name for name in dir(module) if not name.startswith('__')]
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    print_module_names()
