from .read_env import ReadEnv
from pydantic import BaseSettings

env = ReadEnv(".env")

class Settings(BaseSettings):
    PROJECT_NAME: str = "MNIST Deployment"
    API_V1_STR: str = "/v1"

    AI_MODEL_PATH: str = env.get("AI_MODEL_PATH")

    class Config:
        case_sensitive: bool = True


settings = Settings()
