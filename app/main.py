"""
main.py

Temporary test file used to verify that the handbook
can be loaded correctly before building the RAG system.
"""

# Import the function that loads the handbook
from pdf_loader import load_handbook

from text_splitter import split_documents
from embeddings import get_embedding_model


def main():
    """
    Test the PDF loader.
    """

    # Load the handbook
    documents = load_handbook()

    # Split into chunks
    chunks = split_documents(documents)

    embedding_model = get_embedding_model()

    print("=" * 60)
    print("HANDBOOK SUCCESSFULLY LOADED")
    print("=" * 60)

    print(f"Total pages loaded: {len(documents)}")
    print(f"Total chunks created: {len(chunks)}")

    print("\nFirst chunk metadata:")
    print(chunks[0].metadata)

    print("\nFirst chunk preview:\n")
    print(chunks[0].page_content)

    print("\nEmbedding model loaded successfully!")
    print(type(embedding_model))

    

if __name__ == "__main__":
    main()