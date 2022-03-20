from tensorflow.keras.models import load_model
from numpy import ndarray, expand_dims, argmax

from typing import Tuple
from ..model_abstract import AIModel

class KerasModel(AIModel):
    def __init__(self, model_path):
        super().__init__(model_path)

    def generate_model(self, model_path):
        model = load_model(model_path, compile=False)
        model.trainable = False

        return model

    def preprocess(self, image: ndarray) -> ndarray:
        local_image = image.copy() / 255.

        local_image = expand_dims(local_image, axis=0)
        return local_image

    def predict(self, image: ndarray) -> Tuple[str, float]:
        preprocessed = self.preprocess(image)

        out = self.model.predict(preprocessed)[0]

        class_label: int = argmax(out)
        class_confidence: float = out[class_label]

        return str(class_label), class_confidence
