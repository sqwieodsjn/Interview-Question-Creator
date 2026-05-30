from loaders.document_loader import load_document
from text_splitter import split_documents
from vector_store import create_vector_store


documents = load_document(
    "uploads/Pandas_Full_Notes.pdf"
)

chunks = split_documents(documents)

vector_store = create_vector_store(chunks)

print("Vector database created successfully!")
print(f"Total Chunks Stored: {len(chunks)}")