"""
Directory module
"""
import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination: str):
    """
    sets destination for exported files
    Args:
        destination (str):

    Returns:

    """
    cwd = os.getcwd()
    try:
        __dest = os.path.realpath(destination)
        if not os.path.exists(__dest):
            os.mkdir(__dest)
        os.chdir(__dest)
        yield
    finally:
        os.chdir(cwd)
