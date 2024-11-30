from dataclasses import dataclass

from core.apps.common.exceptions import ApplicationException


@dataclass(eq=False)
class ImageNotFound(ApplicationException):
    image_id: int

    @property
    def message(self):
        return "Image not found"
