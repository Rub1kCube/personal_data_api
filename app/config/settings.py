from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import RedisDsn

from functools import lru_cache


root_project_path = Path(__file__).absolute().parent.parent.parent


def _get_env_path():
    return (
        root_project_path / ".example_env",
        root_project_path / ".test_env",
        root_project_path / ".prod_env",
    )


class SettingApp(BaseSettings):
    title_app: str = "backend"
    port: int = 8080
    host: str = "localhost"
    test: bool = False
    logging_level: Literal["INFO", "DEBUG"] = "INFO"


class SettingRedis(BaseSettings):
    redis_main_dsn: RedisDsn


class Settings(SettingApp, SettingRedis):

    model_config = SettingsConfigDict(
        env_file=_get_env_path(),
        env_file_encoding="utf-8",
    )

    @property
    def url(self):
        return f"{self.host}:{self.port}"


@lru_cache
def get_settings():
    return Settings()
