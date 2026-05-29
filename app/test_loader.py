from loaders.document_loader import load_document

file_path = "uploads/NUMPY-2.docx"

documents = load_document(file_path)

print(f"Total Documents Loaded: {len(documents)}")

for i, doc in enumerate(documents):

    print("\n" + "="*50)
    print(f"Document {i+1}")
    print("="*50)

    print("Metadata:")
    print(doc.metadata)

    print("\nContent Preview:")
    print(doc.page_content[:500])