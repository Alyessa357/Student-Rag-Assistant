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