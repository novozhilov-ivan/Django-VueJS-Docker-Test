from dataclasses import dataclass
from datetime import datetime


@dataclass
class ImageEntity:
    id: int  # noqa
    created_at: datetime
    updated_at: datetime
    encoded_image: str
    description: str
