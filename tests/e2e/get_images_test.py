from tests.conftest import add_images_to_db

import pytest

from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from core.api.v1.images.get_images.schemas import ImageResponseSchema
from core.apps.images.entities import ImageEntity
from core.apps.images.services import BaseImagesService


@pytest.mark.django_db
def test_get_images_empty_list(client: APIClient):
    response: Response = client.get(reverse("get_images"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data == []


@pytest.mark.parametrize(
    "image_count",
    (1, 5),
)
@pytest.mark.django_db
def test_get_images_empty_list(
    client: APIClient,
    images_service: BaseImagesService,
    image_entity: ImageEntity,
    image_count: int,
):
    add_images_to_db(images_service, image_entity, image_count)

    response: Response = client.get(reverse("get_images"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data == [
        ImageResponseSchema.model_validate(image).model_dump()
        for image in images_service.get_image_list()
    ]
