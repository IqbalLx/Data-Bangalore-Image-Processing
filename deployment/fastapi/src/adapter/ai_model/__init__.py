from config.settings import settings

from .keras.keras_model import KerasModel

model = KerasModel(settings.AI_MODEL_PATH)