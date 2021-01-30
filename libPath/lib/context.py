"""
    Context managers for file paths & directories
"""

import os


# ----------------------------------------------------------------------------------------------- #
class BypassPermissions(object):
    """
    Context Manager for temporarily changing path permissions.
    e.g. for saving files in locked folders.
    """
    def __init__(self, path, permissions):
        """
        :param path: directory to unlock/lock
                      - str
        """
        pass

    def __enter__(self):
        pass

    def __exit__(self, ex_type, ex_value, ex_traceback):
        pass

# ----------------------------------------------------------------------------------------------- #
