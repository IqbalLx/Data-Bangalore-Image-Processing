from abc import ABC
from numpy import ndarray, expand_dims
from typing import Tuple

class AIModel(ABC):
    model = None

    def __init__(self, model_path: str):
        self.model = self.generate_model(model_path)

    def generate_model(self, model_path):
        """Load model

        Args:
            model_path (_type_): model path in system
        """
        pass
        
    def preprocess(self, image: ndarray) -> ndarray:
        """Preprocessing data

        Args:
            image (ndarray): raw input image

        Returns:
            ndarray: preprocessed input image
        """
        pass

    def predict(self, image: ndarray) -> Tuple[str, float]:
        """Predict input data

        Args:
            image (ndarray): input image data

        Returns:
            Tuple[0] str: class label
            Tuple[1] float: class confidence
        """
        pass