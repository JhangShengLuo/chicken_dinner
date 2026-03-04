from abc import ABC, abstractmethod
from typing import Dict, Type, Any
from langchain_core.language_models.chat_models import BaseChatModel

class ProviderRegistry:
    """Registry pattern for AI Model Providers."""
    _providers: Dict[str, Any] = {}

    @classmethod
    def register(cls, name: str, provider_factory):
        cls._providers[name] = provider_factory

    @classmethod
    def get_provider(cls, name: str, **kwargs) -> BaseChatModel:
        if name not in cls._providers:
            raise ValueError(f"Provider '{name}' not found. Available: {list(cls._providers.keys())}")
        return cls._providers[name](**kwargs)

    @classmethod
    def list_providers(cls) -> list[str]:
        return list(cls._providers.keys())
