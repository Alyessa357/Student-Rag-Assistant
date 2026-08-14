"""
vector_store.py

This module is responsible for creating a ChromaDB vector database
from the handbook chunks.
"""

from functools import lru_cache
from pathlib import Path

from langchain_chroma import Chroma

from embeddings import get_embedding_model

CHROMA_DIR = str(Path(__file__).resolve().parent.parent / "chroma_db")
COLLECTION_NAME = "student_handbook"


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

    embedding_model = get_embedding_model()

    existing = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embedding_model,
        collection_name=COLLECTION_NAME,
    )

    try:
        existing.delete_collection()
    except Exception:
        pass

    load_vector_store.cache_clear()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
        collection_metadata={"hnsw:space": "cosine"},
    )

    return vector_store


@lru_cache(maxsize=1)
def load_vector_store():
    """
    Load the existing Chroma vector database.

    Returns:
        Chroma vector store
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embedding_model,
        collection_name=COLLECTION_NAME,
    )

    return vector_store
