import os


def make_sure_path_exists(path):
    """Create a directory if it does not exist.

    Parameters
    ----------
    path : str
        The path to the directory which should be created.

    Returns
    -------
    bool
        True if the path exists.

    Raises
    ------
    OSError
        If an error was encountered while creating the directory.
    """
    if not path or os.path.isdir(path):
        return True
    try:
        os.makedirs(path)
        return True
    except OSError:
        raise
