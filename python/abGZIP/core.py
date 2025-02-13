"""
    Wrapper for the GZIP library.
"""
import os
import json
import gzip


# ----------------------------------------------------------------------------------------------- #
def write(file_path: os.PathLike, data_dict: dict, mode='wb'):
    """ Writes an archive file containing json dict data. """
    with gzip.open(file_path, mode) as archive_file:
        archive_file.write(json.dumps(data_dict).encode("utf-8"))

def read(file_path, mode='rb') -> dict:
    """ Retrieves the contents of a compressed data file as json dict object. """
    with gzip.open(file_path, mode) as archive_file:
        return json.loads(archive_file.read().decode("utf-8"))
# ----------------------------------------------------------------------------------------------- #
