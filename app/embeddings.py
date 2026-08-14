"""
embeddings.py

This module creates the embedding model used to convert
text chunks into vector embeddings.
"""

from functools import lru_cache
from langchain_huggingface import HuggingFaceEmbeddings


@lru_cache(maxsize=1)
def get_embedding_model():
    """
    Create and cache the embedding model.

    The model is loaded once and reused for subsequent requests.

    Returns:
        HuggingFaceEmbeddings
    """

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )