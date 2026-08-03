"""
vector_store.py

This module is responsible for creating a ChromaDB vector database
from the handbook chunks.
"""

# Import Chroma vector database
from langchain_chroma import Chroma

# Import the embedding model
from embeddings import get_embedding_model


def create_vector_store(chunks):
    """
    Create a ChromaDB vector database from the handbook chunks.

    Args:
        chunks (list):
            List of LangChain Document chunks.

    Returns:
        Chroma:
            The populated vector database.
    """

    # Load the embedding model
    embedding_model = get_embedding_model()

    # Create the vector database
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="../chroma_db"
    )

    return vector_store


def load_vector_store():
    """
    Load the existing Chroma vector database.

    Returns:
        Chroma vector store
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        persist_directory="../chroma_db",
        embedding_function=embedding_model
    )

    return vector_store
