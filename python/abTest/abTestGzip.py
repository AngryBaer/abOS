"""
    Test how to handle .json data with gzip archives.
"""


import json
import gzip


# ---------------------------------------------------------------------------------------------- #
def json_read(file_path, mode='r'):
    """ Read .json file and return data as python dict """
    with open(file_path, mode) as json_file:
        json_data = json.load(json_file)

    return json_data


def json_write(file_path, data_dict, mode='w+', indent=0):
    """ write data to file """
    with open(file_path, mode) as json_file:
        json.dump(data_dict, json_file, indent=indent)

    return file_path
# ---------------------------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------------------------- #
def gzip_archive():
    pass


def gzip_unpack():
    pass


def gzip_write(file_path, data_object, mode='wb', indent=None):
    """ Writes an archive file containing json dict data. """
    with gzip.open(file_path, mode) as archive_file:
        archive_file.write(data_object)

    return file_path


def gzip_read(file_path, mode='rb'):
    """ Retrieves the contents of a compressed data file as json dict object. """
    with gzip.open(file_path, mode) as archive_file:
        archive_contents = archive_file.read()

    return archive_contents
# ---------------------------------------------------------------------------------------------- #


if __name__ == '__main__':
    file_path = 'some/file/path.json.gz'
    gzip_file   = gzip_write(file_path, json.dumps(data_dict))
    json_object = json.loads(gzip_read(file_path), encoding="utf-8")
