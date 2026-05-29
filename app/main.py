from fastapi import FastAPI

app = FastAPI(title = "Interview Question Creatot",
              description = "Generate interview questions from  PDFs using LangChain and FAISS",
              version = "1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Interview Question Creator API is running!"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }