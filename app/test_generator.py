from retriever import get_relevant_chunks
from generator import generate_interview_questions


query = "What is Numpy?"

docs = get_relevant_chunks(query)

context = "\n".join(
    doc.page_content
    for doc in docs
)

response = generate_interview_questions(
    context
)

print(response)