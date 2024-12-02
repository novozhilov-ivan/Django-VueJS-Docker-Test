from abc import ABC, abstractmethod
from base64 import b64decode
from dataclasses import dataclass
from datetime import datetime

from core.apps.images.enums import ImageExtension
from core.apps.images.exceptions import ValidateBase64PayloadException


@dataclass(kw_only=True)
class BaseEntity(ABC):
    id: int | None = None  # noqa
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def __post_init__(self) -> None:
        self.validate()

    @abstractmethod
    def validate(self) -> None:
        raise NotImplementedError


@dataclass(kw_only=True)
class ImageEntity(BaseEntity):
    base64_payload: str
    extension: ImageExtension
    description: str

    def validate(self) -> None:
        try:
            b64decode(self.base64_payload.encode(), validate=True)
        except ValueError:
            raise ValidateBase64PayloadException(self.base64_payload)
