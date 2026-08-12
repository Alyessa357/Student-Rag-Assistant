# ORIGINAL

# """
# embeddings.py

# This module creates the embedding model used to convert
# text chunks into vector embeddings.
# """

# from langchain_huggingface import HuggingFaceEmbeddings


# def get_embedding_model():
#     """
#     Create and return the embedding model.

#     Returns:
#         HuggingFaceEmbeddings
#     """

#     embedding_model = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )

#     return embedding_model

# --------------------------------------------------------------------------------------------

# TESTING

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