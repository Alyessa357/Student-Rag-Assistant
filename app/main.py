"""
main.py

Temporary test script for creating the Chroma vector database.
"""

# Import the function that loads the handbook
from pdf_loader import load_handbook

from text_splitter import split_documents
from vector_store import create_vector_store


def main():
    """
    Load the handbook, split it into chunks,
    create embeddings, and store everything in ChromaDB.
    """

    # Load the handbook
    documents = load_handbook()

    # Split into chunks
    chunks = split_documents(documents)
     
    # Create vector database
    vector_store = create_vector_store(chunks)

    print("=" * 60)
    print("VECTOR DATABASE CREATED SUCCESSFULLY")
    print("=" * 60)

    print(f"Total handbook pages : {len(documents)}")
    print(f"Total chunks stored  : {len(chunks)}")

    print("\nVector Store Type:")
    print(type(vector_store))

if __name__ == "__main__":
    main()