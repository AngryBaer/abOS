"""
    Path conversion tools
"""


# IMPORTS --------------------------------------------------------------------------------------- #
import os
import platform
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
def merge(path_in):
    return os.path.join(paths_in[0], paths_in[1]).replace('\\', '/') 


def resolve(path_in):
    raise NotImplemented

# ----------------------------------------------------------------------------------------------- #
