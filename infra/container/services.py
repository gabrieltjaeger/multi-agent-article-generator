from infra.crewai.crewai_article_generator_service import \
    CrewAIArticleGeneratorService


class ServicesContainer():
    article_generator_service = CrewAIArticleGeneratorService()
