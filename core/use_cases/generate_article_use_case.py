from core.services.article_generator_service import ArticleGeneratorService
from core.types.article_content_response import ArticleContentResponse
from core.types.content_request import ContentRequest
from core.types.content_response import ContentResponse


class GenerateArticleUseCase:
    def __init__(self, article_generator_service: ArticleGeneratorService[ContentRequest, ArticleContentResponse]):
        """
        Initializes the GenerateArticleUseCase with the provided article generator service.

        Args:
            article_generator_service (ArticleGeneratorService): The service used to generate articles.
        """
        self.article_generator_service = article_generator_service
        
    async def execute(self, topic: ContentRequest) -> ArticleContentResponse:
        """
        Executes the article generation process.
        Args:
            topic (ContentRequest): The topic to generate an article for.
        Returns:
            ContentResponse: The generated article.
        """
        content: ArticleContentResponse = await self.article_generator_service.execute(topic)
        return content
