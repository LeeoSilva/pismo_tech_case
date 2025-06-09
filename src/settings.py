import functools
import pydantic
import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    db_host: str = pydantic.Field(alias="POSTGRES_HOST", default="host.docker.internal")
    db_port: int = pydantic.Field(alias="POSTGRES_PORT", default=5432)
    db_user: str = pydantic.Field(alias="POSTGRES_USER", default="postgres")
    db_password: str = pydantic.Field(alias="POSTGRES_PASSWORD", default="postgres")
    db_name: str = pydantic.Field(alias="POSTGRES_DB", default="pismo_tech_case")


@functools.lru_cache()
def settings() -> Settings:
    return Settings()
