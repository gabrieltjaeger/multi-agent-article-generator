from typing import Any, ClassVar

from pydantic import ValidationError, model_validator
from pydantic_core import ErrorDetails

from core.types.content_request import ContentRequest


class WikipediaContentRequest(ContentRequest):
  MAX_TOPIC_BYTES: ClassVar[int] = 255
  
  @model_validator(mode="before")
  @classmethod
  def validate_topic_byte_length(
    cls, values: dict[str, Any]
  ) -> dict[str, Any]:
    """
    Validates the byte length of the topic, ensuring it does not exceed the maximum limit imposed by Wikipedia.
    This is done by encoding the topic in UTF-8 and checking its byte length.
    Reference: https://en.wikipedia.org/wiki/Wikipedia:Naming_conventions_(technical_restrictions)#Title_length
    """
    topic = values.get("topic", "")
    
    if len(topic.encode("utf-8")) > cls.MAX_TOPIC_BYTES:
      raise ValidationError.from_exception_data(
        title="Topic Validation Error",
        line_errors=[
          ErrorDetails(
            type="value_error",
            loc=("topic",),
            input=topic,
            ctx={"byte_length": len(topic.encode("utf-8")), "error": f"Topic exceeds maximum byte length of {cls.MAX_TOPIC_BYTES} bytes."},
          )
        ]
      )
    
    return values
  
  
  
  
