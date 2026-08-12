# ORIGINAL

# """
# models.py

# Loads the local Ollama language model.
# """

# from langchain_ollama import ChatOllama


# def load_llm():
#     """
#     Load the local Ollama model.

#     Returns:
#         ChatOllama
#     """

#     llm = ChatOllama(
#         model="llama3.2",
#         temperature=0
#     )

#     return llm

# ---------------------------------------------------------------------------------------------

# TESTING

"""
models.py

Loads the local Ollama language model.
"""

from functools import lru_cache
from langchain_ollama import ChatOllama


@lru_cache(maxsize=1)
def load_llm():
    """
    Load and cache the local Ollama language model.

    The model is loaded once and reused for subsequent requests.

    Returns:
        ChatOllama
    """

    return ChatOllama(
        model="llama3.2",
        temperature=0
    )