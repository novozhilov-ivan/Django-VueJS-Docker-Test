from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseEntity:
    id: int | None = None  # noqa
    created_at: datetime | None = None
    updated_at: datetime | None = None


@dataclass(kw_only=True)
class ImageEntity(BaseEntity):
    encoded_image: str
    description: str
