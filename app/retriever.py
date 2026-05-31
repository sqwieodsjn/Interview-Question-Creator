from langchain_community.vectorstores import FAISS

from app.embedding_model1 import get_embedding_model


def load_vector_store():

    embeddings = get_embedding_model()

    vector_store = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store


def get_relevant_chunks(query, k=3):

    vector_store = load_vector_store()

    results = vector_store.similarity_search(
        query,
        k=k
    )

    return results