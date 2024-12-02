from base64 import b64encode

import pytest

from django.test import Client

from core.apps.images.enums import ImageExtension


@pytest.fixture(scope="session")
def client():
    return Client()


@pytest.fixture(scope="function")
def image_data_use_case_dict() -> dict:
    return {
        "base64_payload": b64encode("some_image".encode()).decode(),
        "extension": ImageExtension.png.value,
        "description": "some_image_description",
    }
