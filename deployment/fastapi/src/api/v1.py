from fastapi import APIRouter

from src.controller.predict_image import router as predict_image_router

api_router = APIRouter()

api_router.include_router(predict_image_router, prefix="/predict", tags=["MNIST"])