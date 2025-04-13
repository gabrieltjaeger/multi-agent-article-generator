
from pydantic import Field

from core.types.content_response import ContentResponse


class WikipediaContentResponse(ContentResponse):
    """
    Represents the response model for Wikipedia content generation.
    
    Attributes:
        content (str): The generated Wikipedia article content.
    """
    content: str = Field(
        ...,
        title="Generated Wikipedia Article Content",
        description="The generated Wikipedia article content.",
    )
