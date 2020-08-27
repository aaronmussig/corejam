

class JAMException(Exception):
    """ Base exception for all JAM exceptions thrown in this project. """

    def __init__(self, message=''):
        Exception.__init__(self, message)


class JAMExit(Exception):
    """Raised when JAM is to quietly exit."""

    def __init__(self, message=''):
        Exception.__init__(self, message)
