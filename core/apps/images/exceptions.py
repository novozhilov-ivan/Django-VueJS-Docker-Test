from dataclasses import dataclass

from core.apps.common.exceptions import ApplicationException


@dataclass(eq=False)
class ImageNotFoundException(ApplicationException):
    image_id: int

    @property
    def message(self):
        return "Image not found"


@dataclass(eq=False)
class ValidateImageException(ApplicationException):
    base64_payload: str

    @property
    def message(self):
        return "Validate image encoding exception occurred"


@dataclass(eq=False)
class ValidateBase64PayloadException(ValidateImageException):
    base64_payload: str

    @property
    def message(self):
        return "Decode base64 image payload exception occurred"
