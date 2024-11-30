from pydantic_settings import BaseSettings


class DjangoSettings(BaseSettings):
    secret_key: str
