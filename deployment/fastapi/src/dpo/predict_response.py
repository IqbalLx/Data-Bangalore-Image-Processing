from pydantic import BaseModel

class PredictResponse(BaseModel):
    class_label: str
    class_conf: float