from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.images.entities import ImageEntity


class Images(TimedBaseModel):
    encoded_image = models.TextField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

    def to_entity(self) -> ImageEntity:
        return ImageEntity(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            encoded_image=self.encoded_image,
            description=self.description,
        )

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
