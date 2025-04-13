import requests

from core.services.content_fetcher_service import ContentFetcherService
from infra.types.wikipedia_content_request import WikipediaContentRequest
from infra.types.wikipedia_content_response import WikipediaContentResponse


class WikipediaContentFetcherService(
    ContentFetcherService[WikipediaContentRequest, WikipediaContentResponse]
    ):
    """
    Service for fetching content from Wikipedia.
    """
    
    def __init__(self, language: str = "en"):
        """
        Initializes the WikipediaContentFetcherService.
        Args:
            language (str): The language code for Wikipedia (default is "en" for English).
        """
        super().__init__()
        self.language = language
        

    def _fetch_content(self, request: WikipediaContentRequest) -> WikipediaContentResponse:
        """
        Fetches content from Wikipedia for the given topic.

        Args:
            topic (WikipediaContentRequest): The topic to fetch content for.

        Returns:
            WikipediaContentResponse: The fetched content.
        """
        url = f"https://{self.language}.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "titles": request.topic,
            "prop": "extracts",
            "explaintext": True,
            "redirects": 1
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            page = next(iter(data["query"]["pages"].values()))
            
            if not "extract" in page:
                raise ValueError(f"No content found for topic: {request.topic}")
            
            content = page.get("extract", "")
            if not content:
                raise ValueError(f"No content found for topic: {request.topic}")
            
            return WikipediaContentResponse(content=content)
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Error fetching content from Wikipedia: {e}")
        except ValueError as e:
            raise ValueError(f"Error processing response: {e}")
        except Exception as e:
            raise ValueError(f"An unexpected error occurred: {e}")
    