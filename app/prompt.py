"""
prompt.py

This module contains the prompt template
used by the RAG assistant.
"""

from langchain_core.prompts import PromptTemplate


def get_prompt():
    """
    Return the prompt template used by the RAG assistant.
    """

    template = """
    You are an AI assistant that answers questions ONLY using the provided handbook context.

    Rules:
    1. Use ONLY the information in the context below.
    2. Do NOT use your own knowledge.
    3. Do NOT guess or make up information.
    4. If the answer cannot be found in the context, reply EXACTLY with:

    I could not find that information in the handbook.

    Handbook Context:
    -----------------
    {context}

    Student Question:
    -----------------
    {question}

    Answer:
    """

    return PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )
