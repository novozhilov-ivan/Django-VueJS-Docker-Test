import pytest

from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from core.apps.images.entities import ImageEntity
from core.apps.images.services import BaseImagesService
from tests.conftest import add_images_to_db


@pytest.mark.django_db
def test_remove_non_exist_image_by_id(client: APIClient):
    non_exist_image_id = 666
    response: Response = client.delete(
        path=reverse(
            viewname="remove_image_by_id",
            kwargs={"id": non_exist_image_id},
        ),
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == "Image not found"


@pytest.mark.django_db
def test_remove_exist_image_by_id(
    client: APIClient,
    images_service: BaseImagesService,
    image_entity: ImageEntity,
):
    add_images_to_db(images_service, image_entity)
    [image] = images_service.get_image_list()

    response: Response = client.delete(
        path=reverse(
            viewname="remove_image_by_id",
            kwargs={"id": image.id},
        ),
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.data == "Image successfully deleted"

    assert not images_service.get_image_list()
