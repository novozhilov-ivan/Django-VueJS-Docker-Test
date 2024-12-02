from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.images.entities import ImageEntity
from core.apps.images.enums import ImageExtension


class ORMImages(TimedBaseModel):
    base64_payload = models.TextField(null=False, blank=False)
    extension = models.CharField(
        max_length=5,
        choices=((ext.value, ext.value) for ext in ImageExtension),
        default=ImageExtension.jpeg,
    )
    description = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.description

    def to_entity(self) -> ImageEntity:
        return ImageEntity(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            base64_payload=self.base64_payload,
            extension=self.extension,
            description=self.description,
        )

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
