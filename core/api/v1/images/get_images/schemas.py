from typing import ClassVar

from pydantic import BaseModel, ConfigDict


class ImageResponseSchema(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(from_attributes=True)

    id: int
    base64_payload: str
    extension: str
    description: str
