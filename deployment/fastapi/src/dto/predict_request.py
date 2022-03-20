from pydantic import BaseModel

class PredictRequest(BaseModel):
    b64: str