from pydantic import BaseSettings
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    app_name: str = "TODO LIST"
    secret_key: str | None
    algorithm: str | None
    mongodb_connection: str | None
    access_token_duration: int
    origins: list[str] = ['http://localhost:8000', 'http://127.0.0.1:8000']
    cors_middleware = CORSMiddleware

class Config:
    env_file = '.env'