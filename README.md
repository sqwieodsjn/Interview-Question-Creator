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

Signup_page:
<img width="1366" height="768" alt="Screenshot 2026-06-01 124706" src="https://github.com/user-attachments/assets/ac0fd208-664e-4a37-b988-bf1c57b3ef3e" />

Login_page:
<img width="1366" height="768" alt="Screenshot 2026-06-01 124713" src="https://github.com/user-attachments/assets/196cd245-a6fa-41fe-ad6e-daf9028c92d2" />

Home_page:
<img width="1366" height="768" alt="Screenshot 2026-06-01 124730" src="https://github.com/user-attachments/assets/3d463be0-beae-4b66-be5a-dc80badb7414" />

Generate_Question:
<img width="1366" height="768" alt="Screenshot 2026-06-01 124751" src="https://github.com/user-attachments/assets/30a3098f-e332-4b45-9bf5-2785b7e34c27" />

Questions_and_answers:
<img width="1366" height="768" alt="Screenshot 2026-06-01 125107" src="https://github.com/user-attachments/assets/09c46db5-27c7-470e-a4a7-e40c1e19bcd3" />

Account:
<img width="1366" height="768" alt="Screenshot 2026-06-01 125157" src="https://github.com/user-attachments/assets/baba33ee-9a1d-412e-88bd-2eec1f4eae2a" />

Reviews:
<img width="1366" height="768" alt="Screenshot 2026-06-01 125226" src="https://github.com/user-attachments/assets/bf7b2827-f1d9-4b01-bef9-7502c33c8c29" />

About:
<img width="1366" height="768" alt="Screenshot 2026-06-01 125251" src="https://github.com/user-attachments/assets/31061e87-f9c6-486e-ae91-b03f9a082254" />

## Future Improvements

* Deployment on Render
* PostgreSQL Database
* Email Verification
* Resume Scoring
* AI Mock Interviews
* Chat-Based Interview Practice

## Author

Shibin T
