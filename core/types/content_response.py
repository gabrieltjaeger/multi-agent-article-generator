from pydantic import BaseModel, Field


class ContentResponse(BaseModel):
    content: str
