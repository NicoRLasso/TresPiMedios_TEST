import os
from enum import Enum
from functools import lru_cache
from typing import Optional
from pydantic import BaseSettings, PostgresDsn


class EnvironmentEnum(str, Enum):
    PRODUCTION = "production"
    LOCAL = "local"


class GlobalConfig(BaseSettings):
    # Rest API
    TITLE: str = "Tres Pi Medios Test"
    DESCRIPTION: str = "Tres pi medios Test"

    OPENAPI_URL: str = "/openapi.json"
    ENVIRONMENT: EnvironmentEnum
    DEBUG: bool = True
    TIMEZONE: str = "UTC"
    # OPENAPI_TAGS: list = tags_metadata

    DATABASE_URL: Optional[
        PostgresDsn
    ] = "postgresql://postgres:postgres@db:5432/db"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 180
    SECRET_KEY: str = "7b972778f5c13821d65fda077a14933d1aacd3131b1d5994ee38c21f4d617617"
    ALGORITHM = "HS256"

    class Config:
        case_sensitive = True


class LocalConfig(GlobalConfig):
    """Local configurations."""

    DEBUG: bool = True
    ENVIRONMENT: EnvironmentEnum = EnvironmentEnum.LOCAL


class ProdConfig(GlobalConfig):
    """Production configurations."""

    DEBUG: bool = False
    ENVIRONMENT: EnvironmentEnum = EnvironmentEnum.PRODUCTION


class FactoryConfig:
    def __init__(self, environment: Optional[str]):
        self.environment = environment

    def __call__(self) -> GlobalConfig:
        if self.environment == EnvironmentEnum.LOCAL.value:
            return LocalConfig()
        return ProdConfig()


@lru_cache()
def get_configuration() -> GlobalConfig:
    return FactoryConfig(os.environ.get("ENVIRONMENT"))()


settings = get_configuration()
