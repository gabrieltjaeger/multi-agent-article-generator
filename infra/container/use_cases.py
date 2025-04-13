from core.use_cases.generate_article_use_case import GenerateArticleUseCase
from infra.container.services import ServicesContainer


class UseCasesContainer():
    generate_article_use_case = GenerateArticleUseCase(
        article_generator_service=ServicesContainer.article_generator_service
    )
