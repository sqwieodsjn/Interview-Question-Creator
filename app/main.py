import email
from urllib import request, response
from datetime import datetime
from fastapi import FastAPI, UploadFile, File, HTTPException
import os
from pydantic import BaseModel
from app.rag_pipeline import run_rag_pipeline
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi.responses import RedirectResponse
from app.pdf_generator import generate_pdf
from app.reviews import save_review
from app.reviews import get_reviews
from app.auth import (create_user, verify_user)
from app.auth import get_user_by_email
from app.reviews import get_user_pdf_count
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI(title = "Interview Question Creator",
              description = "Generate interview questions from any files using LangChain and FAISS",
              version = "1.0.0"
)

app.add_middleware(
    SessionMiddleware,
    secret_key="my_super_secret_key_123"
)

# Static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)
app.mount(
    "/generated_pdfs",
    StaticFiles(
        directory="generated_pdfs"
    ),
    name="generated_pdfs"
)

# Templates
templates = Jinja2Templates(
    directory="templates"
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
def landing_page(request: Request):

    return templates.TemplateResponse(
        "landing.html",
        {
            "request": request
        }
    )

@app.get("/login")
def login_page(request: Request):

    return templates.TemplateResponse(
        "login.html",
        {
            "request": request
        }
    )

@app.post("/login")
def login_user(

    request: Request,

    email: str = Form(...),

    password: str = Form(...)

):

    valid = verify_user(
        email,
        password
    )

    if not valid:

        return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "error": True
        }
    )

    request.session["user_email"] = email

    return RedirectResponse(
    url="/home",
    status_code=303
)


@app.get("/signup")
def signup_page(request: Request):

    return templates.TemplateResponse(
        "signup.html",
        {
            "request": request
        }
    )

@app.post("/signup")
def signup_user(

    name: str = Form(...),

    profession: str = Form(...),

    email: str = Form(...),

    password: str = Form(...)

):

    success = create_user(
    name,
    profession,
    email,
    password
)

    if not success:

        return {
        "message":
        "Email already exists"
    }

    return RedirectResponse(
    url="/login",
    status_code=303
)

@app.get("/home")
def home_page(request: Request):

    if "user_email" not in request.session:

        return RedirectResponse(
            "/login",
            status_code=303
        )

    response = templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "questions": None,
            "pdf_file": None
        }
    )

    response.headers["Cache-Control"] = (
        "no-store, no-cache, must-revalidate"
    )

    return response

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

@app.post("/generate")
async def generate_questions_page(

    request: Request,

    file: UploadFile = File(...),

    difficulty: str = Form(...)

):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    content = await file.read()

    with open(
        file_path,
        "wb"
    ) as f:

        f.write(content)

    query = f"""
    Generate {difficulty}
    level interview questions
    and answers.
    """

    response = run_rag_pipeline(
        file_path,
        query
    )

    pdf_name = f"Interview_Questions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    pdf_path = os.path.join(
    "generated_pdfs",
    pdf_name
)

    generate_pdf(
    response,
    pdf_path
)
    email = request.session.get(
    "user_email"
)

    save_review(
    email,
    file.filename,
    pdf_name
)
    return templates.TemplateResponse(
    "home.html",
    {
        "request": request,
        "questions": response,
        "pdf_file": pdf_name
    }
)

@app.get("/reviews")
def reviews_page(request: Request):

    if "user_email" not in request.session:

        return RedirectResponse(
            "/login",
            status_code=303
        )

    email = request.session.get(
        "user_email"
    )

    reviews = get_reviews(
        email
    )

    response = templates.TemplateResponse(
        "reviews.html",
        {
            "request": request,
            "reviews": reviews
        }
    )

    response.headers["Cache-Control"] = (
        "no-store, no-cache, must-revalidate"
    )

    return response

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

@app.get("/account")
def account_page(
    request: Request
):

    email = request.session.get(
    "user_email"
)

    if not email:

        return RedirectResponse(
           "/login",
           status_code=303
    )

    user = get_user_by_email(
    email
)

    total_pdfs = get_user_pdf_count(
    email
)

    response = templates.TemplateResponse(
    "account.html",
    {
        "request": request,
        "user": user,
        "total_pdfs": total_pdfs
    }
)

    response.headers["Cache-Control"] = (
    "no-store, no-cache, must-revalidate"
)

    return response

@app.get("/logout")
def logout(request: Request):

    request.session.clear()

    response = RedirectResponse(
        "/login",
        status_code=303
    )

    response.delete_cookie("session")

    return response