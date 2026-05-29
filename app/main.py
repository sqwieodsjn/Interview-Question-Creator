from fastapi import FastAPI, UploadFile, File, HTTPException
import os

app = FastAPI(title = "Interview Question Creatot",
              description = "Generate interview questions from  PDFs using LangChain and FAISS",
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