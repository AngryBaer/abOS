"""
    Wrapper for the JSON library.
"""
import os
import json


# ----------------------------------------------------------------------------------------------- #
def read(file_path: os.PathLike, mode: str = 'r') -> dict:
    """ Returns the contents of a .json file as dict object. """
    with open(file_path, mode, encoding="utf=8") as json_file:
        return json.load(json_file)


def write(file_path: os.PathLike, json_data: dict, mode: str = 'w+'):
    """ Writes a .json file containing the given data. """
    with open(file_path, mode, encoding="utf=8") as json_file:
        json.dump(json_data, json_file, indent=2)
# ----------------------------------------------------------------------------------------------- #
