from src.dto.predict_request import PredictRequest
from src.dpo.predict_response import PredictResponse
from src.adapter.ai_model.model_abstract import AIModel

from src.utils.imutils import decode_b64_to_image

def predict_image(request: PredictRequest, model: AIModel) -> PredictResponse:
    image = decode_b64_to_image(b64str=request.b64)
    class_label, class_conf = model.predict(image=image)

    return PredictResponse(
        class_label=class_label,
        class_conf=class_conf
    )
