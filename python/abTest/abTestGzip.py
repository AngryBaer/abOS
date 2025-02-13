"""
    Test how to handle .json data with gzip archives.
"""
import os
import json
import gzip


# ----------------------------------------------------------------------------------------------- #
def gzip_write(file_path: os.PathLike, data_dict: dict, mode='wb'):
    """ Writes an archive file containing json dict data. """
    with gzip.open(file_path, mode) as archive_file:
        archive_file.write(json.dumps(data_dict).encode("utf-8"))

def gzip_read(file_path, mode='rb') -> dict:
    """ Retrieves the contents of a compressed data file as json dict object. """
    with gzip.open(file_path, mode) as archive_file:
        archive_contents = archive_file.read().decode("utf-8")
        return json.loads(archive_contents)
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    TEST_DATA = {"test": 123}
    TEST_PATH = os.path.join(os.path.dirname(__file__), "results", "gzip_archive_test.json.gz")
    gzip_write(TEST_PATH, TEST_DATA)

    assert gzip_read(TEST_PATH)["test"] == 123
# ----------------------------------------------------------------------------------------------- #
