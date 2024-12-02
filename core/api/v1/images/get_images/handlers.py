from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from core.api.v1.images.get_images.schemas import ImageResponseSchema
from core.apps.images.services import BaseImagesService
from core.project.containers import get_container


@api_view(http_method_names=["GET"])
def get_images_handler(_: Request) -> Response:
    container = get_container()
    image_service: BaseImagesService = container.resolve(BaseImagesService)

    images = image_service.get_image_list()

    return Response(
        data=[
            ImageResponseSchema.model_validate(image).model_dump()
            for image in images
        ],
        status=status.HTTP_200_OK,
    )
