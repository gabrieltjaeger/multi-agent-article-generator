import os

from dotenv import load_dotenv


def get_gemini_model_name() -> str:
    """
    Get the Gemini model name from environment variables.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Get the model name from the environment variable
    model_name = os.getenv("GEMINI_MODEL_NAME")

    if not model_name:
        raise ValueError("GEMINI_MODEL_NAME not found in environment variables.")

    return model_name