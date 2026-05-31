from fastapi import FastAPI, UploadFile, File, HTTPException
import os
from pydantic import BaseModel
from app.rag_pipeline import run_rag_pipeline

app = FastAPI(title = "Interview Question Creator",
              description = "Generate interview questions from any files using LangChain and FAISS",
              version = "1.0.0"
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".txt",
    ".docx",
    ".png",
    ".jpg",
    ".jpeg"
}

class QuestionRequest(BaseModel):
    filename: str
    query: str = "Generate interview questions"

@app.get("/")
def home():
    return {
        "message": "Interview Question Creator API is running!"
    }

@app.post("/upload-file")
async def upload_pdf(file:UploadFile = File(...)):
    file_extension = os.path.splitext(file.filename)[1].lower()
    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Unsupported file type. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}")
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)
    return {
        "filename": file.filename,
        "file_type": file_extension,
        "message": "File uploaded successfully!"
    }

@app.post("/generate-questions")
def generate_questions(request: QuestionRequest):

    file_path = os.path.join(
        UPLOAD_DIR,
        request.filename
    )

    if not os.path.exists(file_path):

        raise HTTPException(
        status_code=400,
        detail=f"Unsupported file type. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
        )

    response = run_rag_pipeline(
        file_path,
        request.query
    )

    return {
        "filename": request.filename,
        "questions": response
    }