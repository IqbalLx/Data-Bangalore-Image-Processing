from src.dto.predict_request import PredictRequest
from src.dpo.predict_response import PredictResponse

from src.adapter.ai_model import model
from .post_image import predict_image

def do_predict_image(request: PredictRequest) -> PredictResponse:
    return predict_image(request, model)