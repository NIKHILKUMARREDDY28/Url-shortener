import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str
    base_url: str
    db_url: str

    class Config:
        env_file = None


def get_settings() -> Settings:
    env_file = f""".env.{os.getenv("AI_ENV", "local")}"""
    settings = Settings(_env_file=env_file)
    print(f"Loading settings for: {settings.env_name}")
    return settings
