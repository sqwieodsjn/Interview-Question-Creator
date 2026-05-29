from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI(title = "Interview Question Creatot",
              description = "Generate interview questions from  PDFs using LangChain and FAISS",
              version = "1.0.0"
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {
        "message": "Interview Question Creator API is running!"
    }

@app.post("/upload-pdf")
async def upload_pdf(file:UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    return {
        "filename": file.filename,
        "message": "File uploaded successfully!"
    }