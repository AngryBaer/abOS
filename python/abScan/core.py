"""
    Recursive wrappers for scandir.
"""
import os
import re


# ----------------------------------------------------------------------------------------------- #
def iter_files(root: os.PathLike, pattern: re.Pattern | None = None, symlinks: bool = False):
    """ Recursive files generator. """
    for item in os.scandir(root):
        if item.is_file(follow_symlinks=symlinks):
            if pattern and pattern.search(item.name) is None:
                continue
            yield item

        elif item.is_dir(follow_symlinks=symlinks):
            yield from iter_files(item.path, pattern, symlinks)


def iter_dirs(root: os.PathLike, pattern: re.Pattern | None = None, symlinks: bool = False):
    """ Recursive directories generator. """
    for item in os.scandir(root):
        if item.is_dir(follow_symlinks=symlinks):
            if not pattern:
                yield item
            elif pattern.search(item.name):
                yield item

            yield from iter_dirs(item.path, pattern, symlinks)


def dir_entry(file_path: os.PathLike):
    """ Return a single DirEntry object for the given path. """
    return next(e for e in os.scandir(os.path.dirname(file_path)) if e.path == file_path)


def make_pattern(pattern_string: str) -> re.Pattern:
    """ Convenience wrapper for `re.compile()`. """
    return re.compile(pattern_string)
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
if __name__ == "__main__":
    print(dir_entry(__file__))  # >>> <DirEntry 'core.py'>
# ----------------------------------------------------------------------------------------------- #
