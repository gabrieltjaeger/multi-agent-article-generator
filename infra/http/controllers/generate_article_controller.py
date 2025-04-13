from pydantic import ValidationError

from core.types.article_content_response import ArticleContentResponse
from core.use_cases.generate_article_use_case import GenerateArticleUseCase
from infra.container import AppContainer
from infra.types.wikipedia_content_request import WikipediaContentRequest


class GenerateArticleParams(WikipediaContentRequest):
  pass
  

async def generate_article_controller(request: GenerateArticleParams) -> ArticleContentResponse:
  """
  Controller function to handle the generation of an article based on the provided topic.
  
  Args:
      request (GenerateArticleParams): The request object containing the topic for the article.
  
  Returns:
      str: The generated article content.
  """
  try:
    # Validate the request
    topic = request.topic
    
    generate_article_use_case: GenerateArticleUseCase = AppContainer.use_cases.generate_article_use_case
    
    response = await generate_article_use_case.execute(topic)
    return response
  except ValidationError as e:
    raise e
  except Exception as e:
    raise e
