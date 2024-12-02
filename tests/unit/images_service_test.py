import pytest

from core.apps.images.entities import ImageEntity
from core.apps.images.exceptions import ImageNotFound
from core.apps.images.models import ORMImages
from core.apps.images.services import BaseImagesService


def add_images_to_db(
    images_service: BaseImagesService,
    image_entity: ImageEntity,
    image_count: int = 1,
) -> None:
    for i in range(image_count):
        images_service.add_image(image_entity)


@pytest.mark.django_db
def test_add_image(images_service: BaseImagesService, image_entity: ImageEntity):
    assert not ORMImages.objects.all()

    images_service.add_image(image_entity)

    query_set = ORMImages.objects.filter(id=image_entity.id)
    assert len(query_set) == 1


@pytest.mark.django_db
def test_get_empty_image_list(images_service: BaseImagesService):
    assert not ORMImages.objects.all()

    images = images_service.get_image_list()

    assert isinstance(images, list)
    assert all([isinstance(obj, ImageEntity) for obj in images])


@pytest.mark.parametrize(
    "image_count",
    (1, 5),
)
@pytest.mark.django_db
def test_get_image_list_with_images(
    images_service: BaseImagesService,
    image_entity: ImageEntity,
    image_count: int,
):
    assert not ORMImages.objects.all()

    add_images_to_db(images_service, image_entity, image_count)

    images = images_service.get_image_list()

    assert len(images) == image_count
    assert all([isinstance(obj, ImageEntity) for obj in images])


@pytest.mark.django_db
def test_try_remove_non_exist_image_by_image_id(
    images_service: BaseImagesService,
    image_entity: ImageEntity,
):
    assert not ORMImages.objects.all()

    with pytest.raises(ImageNotFound):
        images_service.remove_image_by_id(image_entity.id)


@pytest.mark.django_db
def test_remove_exist_image_by_image_id(
    images_service: BaseImagesService,
    image_entity: ImageEntity,
):
    assert not ORMImages.objects.all()

    add_images_to_db(images_service, image_entity)

    query_set = ORMImages.objects.filter(encoded_image=image_entity.encoded_image)
    assert query_set
    image_in_db: ORMImages
    image_in_db, *_ = query_set

    images_service.remove_image_by_id(image_in_db.id)

    assert not ORMImages.objects.all()
