import pytest

from core.apps.images.entities import ImageEntity
from core.apps.images.services import BaseImagesService, ORMImagesService


@pytest.fixture(scope="session")
def images_service() -> BaseImagesService:
    return ORMImagesService()


@pytest.fixture(scope="session")
def image_entity():
    return ImageEntity(
        id=1,
        encoded_image="encoded_base64_image",
        description="some_image_description",
    )
