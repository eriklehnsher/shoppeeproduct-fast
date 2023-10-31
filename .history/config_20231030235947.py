from re import template
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "API"
    secret_key: str
    # upload_path: str = "/uploads"
    # base_fe_url: str
    uri: str = "mongodb://localhost:27017"
    # send_grid_key: str
    class Config:
        env_file = ".env"


settings = Settings()