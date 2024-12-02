import pytest

from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_add_correct_image(client: APIClient, image_data_use_case_dict: dict):
    response: Response = client.post(
        path=reverse("add_image"),
        data=image_data_use_case_dict,
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == "Image added successfully"


@pytest.mark.parametrize(
    "field",
    (
        "base64_payload",
        "extension",
        "description",
    ),
)
@pytest.mark.django_db
def test_add_image_without_one_field(
    client: APIClient,
    field: str,
    image_data_use_case_dict: dict,
):
    image_data_use_case_dict.pop(field)

    response: Response = client.post(
        path=reverse("add_image"),
        data=image_data_use_case_dict,
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data


@pytest.mark.django_db
def test_add_image_with_wrong_base64_payload(
    client: APIClient,
    image_data_use_case_dict: dict,
):
    image_data_use_case_dict["base64_payload"] = "**"

    response: Response = client.post(
        path=reverse("add_image"),
        data=image_data_use_case_dict,
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST

    expected_detail_message = "Decode base64 image payload exception occurred"

    assert response.data == expected_detail_message, response.data
