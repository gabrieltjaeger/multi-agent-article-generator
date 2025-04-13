from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from core.types.content_request import ContentRequest
from core.types.content_response import ContentResponse

RequestType = TypeVar("RequestType", bound=ContentRequest)
ResponseType = TypeVar("ResponseType", bound=ContentResponse)

class ArticleGeneratorService(ABC, Generic[RequestType, ResponseType]):
    """
    Abstract base class for generating articles.
    """

    async def execute(self, topic: RequestType) -> ResponseType:
        """
        Executes the article generation process.

        Args:
            topic (RequestType): The topic to generate an article for.

        Returns:
            ResponseType: The generated article.
        """
        return await self._generate_article(topic)
      
    @abstractmethod
    async def _generate_article(self, topic: RequestType) -> ResponseType:
        """
        Abstract method to generate an article based on the provided topic.

        Args:
            topic (RequestType): The topic to generate an article for.

        Returns:
            ResponseType: The generated article.
        """
        pass
