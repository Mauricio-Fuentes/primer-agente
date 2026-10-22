from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from config import Settings


def crear_modelo(settings: Settings) -> GoogleModel:
    provider = GoogleProvider(
        api_key=settings.gemini_api_key.get_secret_value())
    modelo = GoogleModel(provider=provider, model_name=settings.gemini_model)
    return modelo
