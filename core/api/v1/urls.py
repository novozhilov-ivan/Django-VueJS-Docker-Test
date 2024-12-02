from django.urls import path

from .images.add_image.handlers import add_image_handler
from .images.remove_images.handlers import DeleteImageAPIView
from core.api.v1.images.get_images.handlers import (
    get_images_handler,
)


urlpatterns = [
    path(
        "image/",
        add_image_handler,
        name="add_image",
    ),
    path(
        "image/",
        DeleteImageAPIView.as_view(),
        name="remove_image_by_id",
    ),
    path(
        "images/",
        get_images_handler,
        name="get_images",
    ),
]
