from crewai import LLM

from infra.utils import get_gemini_api_key, get_gemini_model_name

GEMINI_LLM = LLM(
    model=get_gemini_model_name(),
    temperature=0.7,
    api_key=get_gemini_api_key(),
)