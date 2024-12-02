from abc import ABC, abstractmethod

from core.apps.images.entities import ImageEntity
from core.apps.images.exceptions import ImageNotFound
from core.apps.images.models import ORMImages


class BaseImagesService(ABC):
    @staticmethod
    @abstractmethod
    def get_image_list() -> list[ImageEntity]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def add_image(image: ImageEntity) -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def remove_image_by_id(image_id: int) -> None:  # noqa
        raise NotImplementedError


class ORMImagesService(BaseImagesService):
    @staticmethod
    def get_image_list() -> list[ImageEntity]:
        query_set = ORMImages.objects.all()
        return [image.to_entity() for image in query_set]

    @staticmethod
    def add_image(image: ImageEntity) -> None:
        ORMImages.objects.create(
            encoded_image=image.encoded_image,
            description=image.description,
        )

    @staticmethod
    def remove_image_by_id(image_id: int) -> None:  # noqa
        try:
            image_to_remove = ORMImages.objects.get(id=image_id)
        except ORMImages.DoesNotExist:
            raise ImageNotFound(image_id=image_id)

        image_to_remove.delete()
