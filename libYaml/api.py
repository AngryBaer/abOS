"""
    Wrapper for the YAML library
    https://pyyaml.org/wiki/PyYAMLDocumentation
"""


# ----------------------------------------------------------------------------------------------- #
# IMPORTS
import os
from yaml import load, load_all, dump, FullLoader
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
def read(file_path, mode='r'):
    """
    Returns the contents of a single .yml document file.

    :param file_path:  path to the file
                        - str

    :return yaml_data: data contained in the .yml file
                        - dict
    """
    assert os.path.exists(file_path), 'target path does not exist: \n{}'.format(file_path)

    with open(file_path, mode) as yaml_file:
        yaml_data = load(yaml_file, Loader=FullLoader)

    return yaml_data


def read_docs(file_path, mode='r'):
    """
    Returns multiple .yml document files.

    :param file_path:  path to the file
                        - str

    :return yaml_docs: generator that yields each document
                        - generator object
    """
    assert os.path.exists(file_path), 'target path does not exist: \n{}'.format(file_path)

    with open(file_path, mode) as yaml_file:
        yaml_docs = load_all(yaml_file, Loader=FullLoader)

    return yaml_docs
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
def write(file_path, yaml_data, mode='w+'):
    """
    Writes a .yml file containing the given data.

    :param file_path: absolute path to file
                       - str
    :param yaml_data: data contained in the .yml file
                       - dict

    :return:          confirmation of transaction
                       - bool
    """
    target_folder = os.path.dirname(file_path)

    assert os.path.exists(target_folder), 'target folder does not exist: \n{}'.format(target_folder)
    assert isinstance(yaml_data, dict),   'requires dict data type, given: {}'.format(type(yaml_data))

    with open(file_path, mode) as yaml_file:
        dump(yaml_data, yaml_file)

    return True


def write_docs(file_path, yaml_docs, mode='w+'):
    """
    Writes a .json file containing the given data.

    :param file_path: absolute path to file
                       - str

    :param yaml_docs: multiple yaml documents
                       - list [dict, dict, ...]

    :return:          confirmation of transaction
                       - bool
    """
    target_folder = os.path.dirname(file_path)

    assert os.path.exists(target_folder), 'target folder does not exist: \n{}'.format(target_folder)
    assert isinstance(yaml_docs, list),   'requires list data type, given: {}'.format(type(yaml_docs))

    doc_check = all([isinstance(x, dict) for x in yaml_docs])
    assert doc_check, 'requires all docs to be of type dict'

    with open(file_path, mode) as yaml_file:
        dump(yaml_docs, yaml_file)

    return True
# ----------------------------------------------------------------------------------------------- #
