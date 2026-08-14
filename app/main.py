# """
# main.py

# Simple test script for the Student RAG Assistant.
# """

# from rag import ask_question


# def main():

#     question = "How long is the bootcamp?"

#     result = ask_question(question)

#     print("\nRESULT")
#     print(result)


# if __name__ == "__main__":
#     main()


# ----------------------------------------------------------------------------------

"""
main.py

Debug script for testing RAG retrieval.
"""

from rag import retrieve_documents, ask_question


def main():

    question = "What are the hardware requirements?"

    print("\n" + "=" * 80)
    print("QUESTION:")
    print(question)
    print("=" * 80)

    documents = retrieve_documents(question)

    print(f"\nRetrieved {len(documents)} documents:\n")

    for i, (doc, score) in enumerate(documents, start=1):
        print("-" * 80)
        print(f"RESULT {i}")
        print(f"Score: {score:.4f}")
        print(f"Page: {doc.metadata.get('page_label', 'Unknown')}")
        print("-" * 80)
        print(doc.page_content[:1500])
        print()

    result = ask_question(question)
    print("=" * 80)
    print("ANSWER")
    print(result)


if __name__ == "__main__":
    main()
