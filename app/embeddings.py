"""
embeddings.py

This module creates the embedding model used to convert
text chunks into vector embeddings.
"""

from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Create and return the embedding model.

    Returns:
        HuggingFaceEmbeddings
    """

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model