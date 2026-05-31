from app.loaders.document_loader import load_document

from app.text_splitter import split_documents

from app.generator import generate_interview_questions
from app.retriever import get_relevant_chunks
from app.vector_store import create_vector_store


def run_rag_pipeline(file_path, query):

    # Step 1
    documents = load_document(file_path)

    # Step 2
    chunks = split_documents(documents)

    # Step 3
    create_vector_store(chunks)

    # Step 4
    docs = get_relevant_chunks(query)

    # Step 5
    context = "\n".join(
        doc.page_content
        for doc in docs
    )

    # Step 6
    response = generate_interview_questions(
        context
    )

    return response