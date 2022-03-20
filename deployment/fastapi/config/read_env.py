import os
from dotenv import load_dotenv

class ReadEnv:
    def __init__(self, env: str):
        self._env_path = env
        load_dotenv(env)
    
    def get(self, key: str):
        value = os.getenv(key, None)
        if not value:
            raise KeyError(f"key {key} not found in {self._env_path}. Please add key {key} with the respective value to {self._env_path} file")

        return value