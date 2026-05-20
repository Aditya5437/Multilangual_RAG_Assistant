from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

import shutil
import os

from backend.rag.rag_pipeline import ingest_pdf, ask_question

router = APIRouter()

UPLOAD_DIR = "backend/uploaded_pdfs"

os.makedirs(UPLOAD_DIR, exist_ok=True)


# =========================
# Request Model
# =========================

class QueryRequest(BaseModel):
    question: str


# =========================
# Health Check
# =========================

@router.get("/health")
def health_check():

    return {
        "status": "OK"
    }


# =========================
# Upload PDF
# =========================

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks_created = ingest_pdf(file_path)

    return {
        "message": "PDF uploaded successfully",
        "chunks_created": chunks_created,
        "filename": file.filename
    }


# =========================
# Ask Question
# =========================

@router.post("/ask")
def ask(query_request: QueryRequest):

    response = ask_question(query_request.question)

    return response

