from src.config import __env
from ..config import api_v3 as v3client


BC_PAGINATION_DEFAULT_LIMIT = __env.get("BC_PAGINATION_DEFAULT_LIMIT", 50)
BC_PAGINATION_DEFAULT_PAGE = __env.get("BC_PAGINATION_DEFAULT_PAGE", 1)


class Paginable:
    """
    Base class for handling pagination in requests.

    This class provides common functionality for paginated requests, including:

    Attributes:
        DEFAULT_LIMIT (int): The default maximum number of records to retrieve per page.
        DEFAULT_PAGE (int): The default page number to retrieve if none is specified.

    Methods:
    """

    PAGINATION_DEFAULT_LIMIT = BC_PAGINATION_DEFAULT_LIMIT
    PAGINATION_DEFAULT_PAGE = BC_PAGINATION_DEFAULT_PAGE

    def __init__(self, base_url, client=v3client):
        """
        Initialize the Paginable class with :

        :param base_url: Base URL for paginated requests.
        :param client: Client for requests (optional).
        """
        self.base_url = base_url
        self.__client = client


class BaseService:
    """
    Base class defining the interface for common repository operations.

    This class provides common functionality for paginated requests, including:

    Attributes:
        client (obj): The default client for request

    Methods:
    """

    def __init__(self, client=v3client):
        """
        Initialize the BaseService class with:

        :param client: Client for requests (optional).
        """
        self.client = client
