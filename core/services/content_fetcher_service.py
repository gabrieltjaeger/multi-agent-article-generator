from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from core.types.content_request import ContentRequest
from core.types.content_response import ContentResponse

RequestType = TypeVar("RequestType", bound=ContentRequest)
ResponseType = TypeVar("ResponseType", bound=ContentResponse)

class ContentFetcherService(ABC, Generic[RequestType, ResponseType]):
    """
    Abstract base class for fetching content from different sources.
    """

    def execute(self, topic: RequestType) -> ResponseType:
        """
        Executes the content fetching process.

        Args:
            topic (str): The topic to fetch content for.

        Returns:
            str: The fetched content.
        """
        return self._fetch_content(topic)
      
    @abstractmethod
    def _fetch_content(self, topic: RequestType) -> ResponseType:
        """
        Abstract method to fetch content from a specific source.

        Args:
            topic (str): The topic to fetch content for.

        Returns:
            str: The fetched content.
        """
        pass
