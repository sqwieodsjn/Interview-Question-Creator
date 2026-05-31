from retriever import get_relevant_chunks_with_score

query = "What is Numpy?"

results = get_relevant_chunks_with_score(query)

for doc, score in results:

    print("\n" + "=" * 50)

    print(f"Score: {score}")

    print(doc.page_content[:300])