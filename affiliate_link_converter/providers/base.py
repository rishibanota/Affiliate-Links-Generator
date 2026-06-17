from abc import ABC, abstractmethod

class BaseProvider(ABC):
    """
    Abstract base class for all affiliate link providers.
    """
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def can_handle(self, url: str) -> bool:
        """
        Check if this provider can handle the given URL.
        """
        pass

    @abstractmethod
    def convert(self, url: str) -> str:
        """
        Convert the URL to an affiliate URL.
        """
        pass
