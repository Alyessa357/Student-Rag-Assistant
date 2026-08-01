"""
prompt.py

This module contains the prompt template
used by the RAG assistant.
"""

from langchain_core.prompts import PromptTemplate


def get_prompt():

    template = """
You are a helpful AI assistant.

Answer the student's question ONLY using the handbook context below.

If the answer cannot be found in the handbook, reply exactly:

"I could not find that information in the handbook."

Context:
{context}

Question:
{question}

Answer:
"""

    return PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )