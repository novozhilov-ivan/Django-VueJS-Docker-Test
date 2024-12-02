from pydantic import ValidationError as PydanticValidationError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from core.api.v1.images.add_image.schemas import AddImageRequestSchema
from core.apps.common.exceptions import ApplicationException
from core.apps.images.entities import ImageEntity
from core.apps.images.services import BaseImagesService
from core.project.containers import get_container


@api_view(http_method_names=["POST"])
def add_image_handler(request: Request):
    try:
        schema = AddImageRequestSchema(
            base64_payload=request.data.get("base64_payload"),
            extension=request.data.get("extension"),
            description=request.data.get("description"),
        )
    except PydanticValidationError as error:
        raise ValidationError(
            detail=error,
            code=status.HTTP_400_BAD_REQUEST,
        )

    container = get_container()
    image_service: BaseImagesService = container.resolve(BaseImagesService)
    try:
        image = ImageEntity(
            base64_payload=schema.base64_payload,
            extension=schema.extension,
            description=schema.description,
        )
        image_service.add_image(image=image)
    except ApplicationException as exception:
        return Response(data=exception.message, status=status.HTTP_400_BAD_REQUEST)

    return Response(
        data="Image added successfully",
        status=status.HTTP_201_CREATED,
    )
