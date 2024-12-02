from base64 import b64encode

import pytest

from core.apps.images.entities import ImageEntity
from core.apps.images.enums import ImageExtension
from core.apps.images.services import BaseImagesService, ORMImagesService


def add_images_to_db(
    images_service: BaseImagesService,
    image_entity: ImageEntity,
    image_count: int = 1,
) -> None:
    for i in range(image_count):
        images_service.add_image(image_entity)


@pytest.fixture(scope="session")
def images_service() -> BaseImagesService:
    return ORMImagesService()


@pytest.fixture(scope="session")
def base64_payload() -> bytes:
    return b64encode("base64_encoded_image_payload".encode())


@pytest.fixture(scope="session")
def image_entity(base64_payload: bytes):
    return ImageEntity(
        base64_payload=base64_payload.decode(),
        extension=ImageExtension.png,
        description="some_image_description",
    )
