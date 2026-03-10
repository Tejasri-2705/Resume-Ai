from fastapi import APIRouter, UploadFile, File
import pdfplumber
import shutil

from app.services.resume_parser import parse_resume
from app.services.rag_engine import store_resume_text, ask_question

router = APIRouter(prefix="/resume")

UPLOAD_FOLDER = "uploads"


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    parsed_data = parse_resume(text)

    store_resume_text(text)

    return {
        "message": "Resume processed successfully",
        "parsed_data": parsed_data
    }


@router.post("/ask")
def ask_resume(question: str):

    answer = ask_question(question)

    return {
        "question": question,
        "answer": answer
    }