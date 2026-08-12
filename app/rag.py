"""
rag.py

This module performs Retrieval-Augmented Generation (RAG).
"""

from vector_store import load_vector_store
from prompt import get_prompt
from models import load_llm


def retrieve_context(question):
    """
    Retrieve the most relevant handbook chunks.
    """

    vector_store = load_vector_store()

    documents = vector_store.similarity_search_with_score(
        question,
        k=15
    )

    context = "\n\n".join(
        doc.page_content
        for doc, score in documents
    )

    return context


def build_prompt(question):
    """
    Create the final prompt sent to the LLM.
    """

    context = retrieve_context(question)

    prompt = get_prompt()

    final_prompt = prompt.format(
        context=context,
        question=question
    )

    return final_prompt


def ask_question(question):
    """
    Retrieve handbook information and generate an answer.

    Returns:
        dict containing:
        - answer
        - source page
    """

    vector_store = load_vector_store()

    documents = vector_store.similarity_search_with_score(
        question,
        k=15
    )
    
    context = "\n\n".join(
        doc.page_content
        for doc, score in documents
    )

    prompt = get_prompt()

    final_prompt = prompt.format(
        context=context,
        question=question
    )

    llm = load_llm()

    response = llm.invoke(final_prompt)

    if documents:
        source = documents[0][0].metadata.get("page_label", "Unknown")
    else:
        source = "Unknown"

    return {
        "answer": response.content,
        "source": f"Page {source}"
    }



