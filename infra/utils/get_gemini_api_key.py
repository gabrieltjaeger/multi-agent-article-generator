import os

from dotenv import load_dotenv


def get_gemini_api_key() -> str:
    """
    Get the Gemini API key from environment variables.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Get the API key from the environment variable
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    return api_key
