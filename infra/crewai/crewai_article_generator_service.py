from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from core.services.article_generator_service import ArticleGeneratorService
from core.types.article_content_response import ArticleContentResponse
from infra.crewai.llms.gemini_llm import GEMINI_LLM
from infra.crewai.tools.wikipedia_api_tool import WikipediaAPITool
from infra.types.wikipedia_content_request import WikipediaContentRequest


@CrewBase
class CrewAIArticleGeneratorService(
    ArticleGeneratorService[WikipediaContentRequest, ArticleContentResponse]
):
    """
    Service for generating articles using CrewAI.
    """
    
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self, language: str = "en"):
        """
        Initializes the CrewAIArticleGeneratorService.
        Args:
            language (str): The language code for CrewAI (default is "en" for English).
        """
        super().__init__()
        self.language = language
        
    @agent
    def article_researcher(self) -> Agent:
        """
        Agent for researching the topic.
        """
        return Agent(
          llm=GEMINI_LLM,
          config=self.agents_config["article_researcher"],
          tools=[WikipediaAPITool()],
          verbose=True,
        )
      
    @agent
    def article_reviewer(self) -> Agent:
        """
        Agent for reviewing the generated article.
        """
        return Agent(
          llm=GEMINI_LLM,
          config=self.agents_config["article_reviewer"],
          verbose=True,
        )
        
    @agent
    def article_writer(self) -> Agent:
        """
        Agent for writing the article.
        """
        return Agent(
          llm=GEMINI_LLM,
          config=self.agents_config["article_writer"],
          verbose=True,
        )
    
    @agent
    def markdown_enforcer(self) -> Agent:
        """
        Agent for enforcing markdown formatting.
        """
        return Agent(
          llm=GEMINI_LLM,
          config=self.agents_config["markdown_enforcer"],
          verbose=True,
        )
    
    @task
    def research_topic(self) -> Task:
        """
        Task for researching the topic.
        """
        return Task(
          config=self.tasks_config["research_topic"],
          agent=self.article_researcher(),
        )
      
    @task
    def review_article(self) -> Task:
        """
        Task for reviewing the article.
        """
        return Task(
          config=self.tasks_config["review_article"],
          agent=self.article_reviewer(),
        )
        
    @task
    def write_article(self) -> Task:
        """
        Task for writing the article.
        """
        return Task(
          config=self.tasks_config["write_article"],
          agent=self.article_writer(),
        )
    
    @task
    def enforce_markdown(self) -> Task:
        """
        Task for enforcing markdown formatting.
        """
        return Task(
          config=self.tasks_config["enforce_markdown"],
          agent=self.markdown_enforcer(),
          output_pydantic=ArticleContentResponse,
        )
    
    @crew
    def article_generation_crew(self) -> Crew:
        """
        Crew for generating the article.
        """
        return Crew(
          agents=[
            self.article_researcher(),
            self.article_writer(),
            self.article_reviewer(),
            self.markdown_enforcer(),
            ],
          tasks=[
            self.research_topic(),
            self.write_article(),
            self.review_article(),
            self.enforce_markdown(),
          ],
          process=Process.sequential,
          verbose=True,
        )
       
    async def _generate_article(self, topic: WikipediaContentRequest) -> ArticleContentResponse:
        """
        Generates an article based on the provided topic.
        
        Args:
            topic (WikipediaContentRequest): The topic to generate an article for.
        
        Returns:
            ArticleContentResponse: The generated article.
        """
        crew = self.article_generation_crew()
        result = await crew.kickoff_async(inputs={"topic": topic})
        
        if not result:
            raise ValueError("Failed to generate article.")
          
        return result.pydantic
