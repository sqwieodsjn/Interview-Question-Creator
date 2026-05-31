from rag_pipeline import run_rag_pipeline


response = run_rag_pipeline(
    "uploads/NUMPY-2.docx",
    "Generate interview questions"
)

print(response)