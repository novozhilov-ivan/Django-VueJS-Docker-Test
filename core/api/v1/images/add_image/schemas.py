from pydantic import BaseModel

from core.apps.images.enums import ImageExtension


class AddImageRequestSchema(BaseModel):
    base64_payload: str
    extension: ImageExtension
    description: str
