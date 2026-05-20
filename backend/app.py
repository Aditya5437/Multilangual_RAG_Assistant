from fastapi import FastAPI
from backend.routes.rag_routes import router

app = FastAPI(
    title="Multilingual Government RAG Assistant",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Multilingual Government RAG API Running"
    }
