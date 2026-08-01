"""
models.py

Loads the local Ollama language model.
"""

from langchain_ollama import ChatOllama


def load_llm():
    """
    Load the local Ollama model.

    Returns:
        ChatOllama
    """

    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    return llm