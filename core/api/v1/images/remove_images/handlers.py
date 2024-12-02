from pydantic import ValidationError as PydanticValidationError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from core.api.v1.images.remove_images.schemas import RemoveImageByIdRequestSchema
from core.apps.common.exceptions import ApplicationException
from core.apps.images.services import BaseImagesService
from core.project.containers import get_container


@api_view(http_method_names=["DELETE"])
def remove_image_by_id_handler(_: Request, id: int) -> Response:  # noqa
    try:
        schema = RemoveImageByIdRequestSchema(id=id)
    except PydanticValidationError as error:
        raise ValidationError(
            detail=error,
            code=status.HTTP_400_BAD_REQUEST,
        )

    container = get_container()
    image_service: BaseImagesService = container.resolve(BaseImagesService)
    try:
        image_service.remove_image_by_id(image_id=schema.id)
    except ApplicationException as exception:
        return Response(data=exception.message, status=status.HTTP_400_BAD_REQUEST)

    return Response(
        data="Image successfully deleted",
        status=status.HTTP_204_NO_CONTENT,
    )
