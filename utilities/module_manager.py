import os


def scan_modules(path):
    """ Scans the given path for .py files except __init__.py, the scan is not recursive """
    command_files = []
    for entry in os.scandir(path):
        # A valid module has to be a .py file different from __init__.py
        valid_command_file = entry.is_file()
        valid_command_file = valid_command_file and '.py' in entry.name
        valid_command_file = valid_command_file and '__init__.py' != entry.name
        if valid_command_file:
            module_name = entry.name.replace('.py', '')
            command_files.append(path + '.' + module_name)
    return command_files
