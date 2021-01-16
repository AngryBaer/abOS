"""
    Path conversion tools
"""


# IMPORTS --------------------------------------------------------------------------------------- #
import os
# import platform
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
def conform(*args):
    """
    Change all slash characters to forward slashes.
    Compliant with python path format to prevent shell script errors.

    :param args:  path components
                   - str, str, ...

    :return path: joined path
                   - str
    """
    return os.path.join(*args).replace('\\', '/') 


def resolve(*args):
    # TODO: resolve paths between Windows & Linux mounts
    raise NotImplemented

# ----------------------------------------------------------------------------------------------- #
