from pydantic_settings import BaseSettings, SettingsConfigDict


class ProjectSettings(BaseSettings):
    """
    Here goes any project specific settings.
    """

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DEBUG: bool | None = True
    Environment: str | None = "local"
    RootPath: str | None = None
    SENTRYDSN: str | None = None
    SENTRYRELEASE: str | None = None
    RedisHost: str | None = None


project_settings = ProjectSettings()
