from abc import ABC, abstractmethod
from typing import Iterable

from core.apps.images.entities import ImageEntity


class BaseImagesService(ABC):
    @abstractmethod
    def get_image_list(self) -> Iterable[ImageEntity]:
        raise NotImplementedError

    @abstractmethod
    def add_image(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_image(self) -> None:
        raise NotImplementedError
