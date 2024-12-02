from functools import lru_cache

from punq import Container

from core.apps.images.services import BaseImagesService, ORMImagesService


@lru_cache(1)
def get_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container.register(BaseImagesService, ORMImagesService)

    return container
