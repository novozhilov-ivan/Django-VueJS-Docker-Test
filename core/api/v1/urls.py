from django.urls import path

from core.api.v1.images.add_image.handlers import add_image_handler
from core.api.v1.images.get_images.handlers import get_images_handler
from core.api.v1.images.remove_images.handlers import remove_image_by_id_handler


urlpatterns = [
    path("image/", add_image_handler, name="add_image"),
    path("image/<int:id>", remove_image_by_id_handler, name="remove_image_by_id"),
    path("images", get_images_handler, name="get_images"),
]
