from pydantic import BaseSettings


class Settings(BaseSettings):
    AOC_SESSION: str = None

    class Config:
        env_file = ".env"


settings = Settings()
