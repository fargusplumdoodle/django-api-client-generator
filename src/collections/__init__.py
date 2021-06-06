from src.util import HTTPMethod


class Group:
    """
    Group of endpoints
    """

    pass


class Endpoint:
    """
    Group of Methods
    """

    path: str


class Method:
    """
    Information for a specific method
    """

    method: HTTPMethod
    pass
