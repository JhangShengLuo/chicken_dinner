from fastapi import APIRouter
from app.ai.registry import ProviderRegistry
import app.ai.providers

router = APIRouter()

@router.get("/providers")
def get_providers():
    return {"providers": ProviderRegistry.list_providers()}
