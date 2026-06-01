# AI Interview Question Generator

An AI-powered Interview Preparation Platform that generates interview questions and answers from resumes, PDFs, DOCX files, study materials, and other documents using Retrieval-Augmented Generation (RAG).

## Features

* User Authentication (Signup/Login)
* Password Hashing with bcrypt
* Session-Based Authentication
* Upload PDF, DOCX, TXT, PNG, JPG Files
* RAG Pipeline using LangChain
* FAISS Vector Database
* Hugging Face Inference API Integration
* Difficulty-Based Question Generation

  * Easy
  * Medium
  * Hard
  * All Types
* AI-Generated Interview Questions & Answers
* PDF Export and Download
* User-Specific Reviews and Download History
* User Profile Dashboard
* Responsive Bootstrap UI

## Tech Stack

### Backend

* FastAPI
* Python
* SQLite

### AI / Machine Learning

* LangChain
* FAISS
* Sentence Transformers
* Hugging Face Inference API

### Frontend

* HTML
* CSS
* Bootstrap 5
* JavaScript

### Authentication

* bcrypt
* FastAPI Session Middleware

## Project Architecture

```text
User Upload
    ↓
Document Loader
    ↓
Text Splitter
    ↓
Embeddings
    ↓
FAISS Vector Store
    ↓
Retriever
    ↓
Hugging Face LLM
    ↓
Interview Questions & Answers
    ↓
PDF Download
```

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/AI-Interview-Question-Generator.git

cd AI-Interview-Question-Generator

pip install -r requirements.txt
```

Create `.env`

```env
HF_TOKEN=your_huggingface_token
```

Run

```bash
python -m app.init_db

uvicorn app.main:app --reload
```

Landing_page:
<img width="1347" height="597" alt="Screenshot 2026-06-01 124636" src="https://github.com/user-attachments/assets/85c8e6de-93ab-4666-8244-1d9f92bbdcfc" />


## Future Improvements

* Deployment on Render
* PostgreSQL Database
* Email Verification
* Resume Scoring
* AI Mock Interviews
* Chat-Based Interview Practice

## Author

Shibin T
