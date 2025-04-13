import re
from typing import Any, ClassVar

from pydantic import ValidationError, model_validator
from pydantic_core import ErrorDetails

from core.types.content_response import ContentResponse


class ArticleContentResponse(ContentResponse):
    MIN_WORDS: ClassVar[int] = 300

    @model_validator(mode="after")
    def validate_content_word_count(self) -> "ArticleContentResponse":
        """
        Ensures the content has at least the minimum number of words
        defined by MIN_WORDS. Word count is calculated by splitting the string.
        """
        word_count = len(re.findall(r'\b\w+\b', self.content))
        if word_count < self.MIN_WORDS:
            raise ValidationError.from_exception_data(
              title="Content Validation Error",
              line_errors=[
                ErrorDetails(
                    type="value_error",
                    loc=("content",),
                    input=self.content,
                    ctx={"word_count": word_count, "error": f"Content must have at least {self.MIN_WORDS} words."},
                )
              ]
            )
        return self
