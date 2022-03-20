from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api import api_v1 as latest_api
from config.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME, 
    openapi_url=f"/redoc",
    docs_url=f"/"
)

# Set all CORS enabled origins
# if settings.BACKEND_CORS_ORIGINS:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # [str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(deprecate_api, prefix=settings.API_V0_STR)
app.include_router(latest_api, prefix=settings.API_V1_STR)
