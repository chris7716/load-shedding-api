from pydantic import BaseSettings


class Settings(BaseSettings):
    db_server: str
    db_cluster: str

    class Config:
        env_file = ".env"

settings = Settings()
