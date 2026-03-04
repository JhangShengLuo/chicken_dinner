from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.api.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lifetime Financial Consulting AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Lifetime Financial Consulting AI API"}

from app.api.models import router as models_router
app.include_router(models_router, prefix="/api", tags=["models"])

from app.api.chat import router as chat_router
app.include_router(chat_router, prefix="/api/chat", tags=["chat"])
