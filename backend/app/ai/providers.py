import os
from app.ai.registry import ProviderRegistry
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_models import ChatLiteLLM

def create_openai(model_name: str = "gpt-4-turbo", **kwargs):
    api_key = os.getenv("OPENAI_API_KEY")
    return ChatOpenAI(model=model_name, api_key=api_key, **kwargs)

def create_anthropic(model_name: str = "claude-3-opus-20240229", **kwargs):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    return ChatAnthropic(model_name=model_name, api_key=api_key, **kwargs)

def create_gemini(model_name: str = "gemini-1.5-pro", **kwargs):
    api_key = os.getenv("GEMINI_API_KEY")
    return ChatGoogleGenerativeAI(model=model_name, google_api_key=api_key, **kwargs)

def create_openrouter(model_name: str = "openrouter/mistralai/mistral-7b-instruct:free", **kwargs):
    api_key = os.getenv("OPENROUTER_API_KEY")
    os.environ["OPENROUTER_API_KEY"] = api_key or ""
    return ChatLiteLLM(model=model_name, **kwargs)

def create_llama_local(model_name: str = "llama3", **kwargs):
    api_base = os.getenv("LLAMA_API_BASE", "http://localhost:11434/v1")
    return ChatOpenAI(model=model_name, api_key="not-needed", base_url=api_base, **kwargs)

ProviderRegistry.register("openai", create_openai)
ProviderRegistry.register("anthropic", create_anthropic)
ProviderRegistry.register("gemini", create_gemini)
ProviderRegistry.register("openrouter", create_openrouter)
ProviderRegistry.register("llama_local", create_llama_local)
