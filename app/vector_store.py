from langchain_community.vectorstores import FAISS

from app.embedding_model1 import get_embedding_model


def create_vector_store(chunks):

    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    vector_store.save_local("vector_db")

    return vector_store