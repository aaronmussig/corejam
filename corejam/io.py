import os


def assert_path_exists(path):
    """Create the specified path and raise an exception if it can't be created.

    Parameters
    ----------
    path : str
        The path to the directory that should be created if not exists.

    Raises
    ------
    OSError
        If the directory wasn't created.
    """
    try:
        if not os.path.isdir(path):
            os.makedirs(path)
            if not os.path.isdir(path):
                raise OSError(f'Unable to create the path: {path}')
    except Exception:
        raise OSError
