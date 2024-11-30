from typing import ClassVar

from pydantic_settings import SettingsConfigDict

from core.project.settings.configs.database import PostgresSettings
from core.project.settings.configs.django import DjangoSettings


class Settings(PostgresSettings, DjangoSettings):
    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
