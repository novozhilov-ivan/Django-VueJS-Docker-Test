import pytest

from core.apps.images.entities import ImageEntity
from core.apps.images.enums import ImageExtension
from core.apps.images.exceptions import ValidateBase64PayloadException


def test_create_image_entity_from_correct_base64_payload(base64_payload: bytes):
    assert ImageEntity(
        base64_payload=base64_payload.decode(),
        extension=ImageExtension.jpeg,
        description="some_description",
    )


def test_image_entity_base64_validator_exception():
    with pytest.raises(ValidateBase64PayloadException):
        ImageEntity(
            base64_payload="not_base64_encoded_image",
            extension=ImageExtension.jpeg,
            description="some_description",
        )
