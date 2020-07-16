"""
    Wrapper for the JSON library
"""


# ----------------------------------------------------------------------------------------------- #
# IMPORTS
import os
from json import load, dump
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
def read(file_path, mode='r'):
    """
    Returns the contents of a .json data file.

    :param   file_path:  (str) path to the file
    :return  json_data: (dict) data contained in the .json file
    """
    assert os.path.exists(file_path), 'target path does not exist: \n'  \
                                      '{}'.format(file_path)

    with open(file_path, mode) as json_file:
        json_data = load(json_file)

    return json_data


def write(file_path, json_data, mode='w+'):
    """
    Writes a .json file containing the given data.

    :param  file_path:  (str) absolute path to file
    :param  json_data: (dict) data contained in the .json file
    :return          : (bool) confirmation of transaction
    """
    target_folder = os.path.dirname(file_path)

    assert os.path.exists(target_folder), 'target folder does not exist: \n'  \
                                          '{}'.format(target_folder)
    assert isinstance(json_data, dict),   'requires dict data type, given '   \
                                          '{}'.format(type(json_data))

    with open(file_path, mode) as json_file:
        dump(json_data, json_file, indent=2)

    return True
# ----------------------------------------------------------------------------------------------- #
