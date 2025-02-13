"""
    Wrapper for the YAML library
    https://pyyaml.org/wiki/PyYAMLDocumentation
"""
import os
import yaml


# ----------------------------------------------------------------------------------------------- #
def read(file_path: os.PathLike, mode: str = 'r'):
    """ Returns the contents of a .yml file. """
    with open(file_path, mode, encoding="utf-8") as yaml_file:
        return yaml.load(yaml_file, Loader=yaml.FullLoader)


def write(file_path: os.PathLike, yaml_data: dict, mode: str = 'w+'):
    """ Writes a .yml file containing the given data. """
    with open(file_path, mode, encoding="utf-8") as yaml_file:
        yaml.dump(yaml_data, yaml_file)
# ----------------------------------------------------------------------------------------------- #
