from typing import Any, Type

from crewai.tools import BaseTool
from pydantic import BaseModel as PydanticBaseModel

from infra.services.wikipedia_content_fetcher_service import \
    WikipediaContentFetcherService
from infra.types.wikipedia_content_request import WikipediaContentRequest
from infra.types.wikipedia_content_response import WikipediaContentResponse


class WikipediaAPITool(BaseTool):
  name: str = "Wikipedia API Tool"
  description: str = "A tool to fetch content from Wikipedia."
  args_schema: Type[PydanticBaseModel] = WikipediaContentRequest
  
  def _run(self, topic: str) -> WikipediaContentResponse:
    """
    Fetches content from Wikipedia for the given topic.

    Args:
        topic (str): The topic to fetch content for.

    Returns:
        str: The fetched content.
    """
    wikipedia_service = WikipediaContentFetcherService()
    request = WikipediaContentRequest(topic=topic)

    return wikipedia_service.execute(request)
