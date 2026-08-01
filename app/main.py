# """
# main.py

# Test retrieving handbook information
# from the Chroma vector database.
# """

# from vector_store import load_vector_store


# def main():

#     vector_store = load_vector_store()

#     collection = vector_store._collection

#     print("=" * 60)
#     print("DOCUMENTS INSIDE CHROMADB")
#     print("=" * 60)
#     print(collection.count())
#     print()

#     question = "How to get access to your calender?"
    

#     results = vector_store.similarity_search(
#         question,
#         k=3
#     )

#     print("=" * 60)
#     print("QUESTION")
#     print("=" * 60)
#     print(question)

#     print("\n")

#     print("=" * 60)
#     print("TOP MATCHES")
#     print("=" * 60)

#     for i, doc in enumerate(results, start=1):
#         print(f"\nMatch {i}")
#         print("-" * 40)

#         print("Metadata:")
#         print(doc.metadata)

#         print("\nContent:")
#         print(doc.page_content[:600])


# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------------------

# TEST 

from models import load_llm


def main():

    llm = load_llm()

    response = llm.invoke("What is Artificial Intelligence?")

    print(response.content)


if __name__ == "__main__":
    main()