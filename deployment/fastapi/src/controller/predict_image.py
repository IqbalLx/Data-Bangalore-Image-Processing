from fastapi import APIRouter

from src.business.predict_image import do_predict_image
from src.dto.predict_request import PredictRequest
from src.dpo.predict_response import PredictResponse

router = APIRouter()

@router.post("/", response_model=PredictResponse)
async def route_optimizer(request: PredictRequest):
    return do_predict_image(request)
