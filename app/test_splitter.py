from loaders.document_loader import load_document
from text_splitter import split_documents

documents = load_document(
    "uploads/Pandas_Full_Notes.pdf"
)

chunks = split_documents(documents)

print(f"Original Documents: {len(documents)}")
print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:5]):

    print("\n" + "=" * 50)

    print(f"Chunk {i+1}")

    print("=" * 50)

    print(chunk.page_content[:300])