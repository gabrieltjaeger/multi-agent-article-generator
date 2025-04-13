from fastapi import APIRouter, Query

from core.types.article_content_response import ArticleContentResponse
from infra.http.controllers.generate_article_controller import \
    generate_article_controller
from infra.types.wikipedia_content_request import WikipediaContentRequest

router = APIRouter()

@router.get("/article/generate", response_model=ArticleContentResponse)
async def generate_article(
    topic: WikipediaContentRequest = Query(...),
) -> ArticleContentResponse:
    """
    Endpoint to generate an article based on the provided topic.
    
    Args:
        topic (WikipediaContentRequest): The topic for the article to be generated.
    
    Returns:
        ArticleContentResponse: The generated article content.
    """
    return await generate_article_controller(topic)