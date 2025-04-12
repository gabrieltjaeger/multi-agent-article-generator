from pydantic import BaseModel, Field


class ContentRequest(BaseModel):
    topic: str = Field(
        ...,
        description="The topic to fetch content for.",
        example="Python programming",
        min_length=1,
    )

    
    