from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # ===== DB
    DBProtocol: str | None = None
    DBUser: str | None = None
    DBPassword: str | None = None
    DBHost: str | None = None
    DBName: str | None = None
    DBConnectionString: str | None = None


db_settings = DBSettings()
