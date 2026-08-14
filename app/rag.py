"""
rag.py

This module performs Retrieval-Augmented Generation (RAG).
"""

from embeddings import get_embedding_model
from vector_store import load_vector_store
from prompt import get_prompt
from models import load_llm

# Retrieve a small number of highly relevant chunks so the LLM
# is not distracted by unrelated handbook pages.
TOP_K = 4
# Keep extra candidates only if they are close to the best match.
MAX_SCORE_GAP = 0.10


def _filter_relevant_chunks(documents):
    """
    Drop chunks that are much less relevant than the top match.
    This stops unrelated pages from polluting the LLM context.
    """

    if not documents:
        return documents

    best_score = documents[0][1]
    return [
        (doc, score)
        for doc, score in documents
        if score <= best_score + MAX_SCORE_GAP
    ]


def retrieve_documents(question, k=TOP_K):
    """
    Generate an embedding for the question and search the vector
    database for the most relevant handbook chunks.

    Returns:
        list[tuple]: (Document, distance_score) pairs.
        Lower scores mean a closer match.
    """

    vector_store = load_vector_store()
    embedding_model = get_embedding_model()

    question_embedding = embedding_model.embed_query(question)

    documents = vector_store.similarity_search_by_vector_with_relevance_scores(
        question_embedding,
        k=max(k, 8),
    )

    return _filter_relevant_chunks(documents)[:k]


def retrieve_context(question):
    """
    Retrieve the most relevant handbook chunks as a single context string.
    """

    documents = retrieve_documents(question)

    context = "\n\n".join(
        f"[Page {doc.metadata.get('page_label', 'Unknown')}]\n{doc.page_content}"
        for doc, _score in documents
    )

    return context


def build_prompt(question):
    """
    Create the final prompt sent to the LLM.
    """

    context = retrieve_context(question)
    prompt = get_prompt()

    return prompt.format(
        context=context,
        question=question,
    )


def ask_question(question):
    """
    Retrieve handbook information and generate an answer.

    Returns:
        dict containing:
        - answer
        - source page
    """

    documents = retrieve_documents(question)

    context = "\n\n".join(
        f"[Page {doc.metadata.get('page_label', 'Unknown')}]\n{doc.page_content}"
        for doc, _score in documents
    )

    prompt = get_prompt()

    final_prompt = prompt.format(
        context=context,
        question=question,
    )

    llm = load_llm()
    response = llm.invoke(final_prompt)

    if documents:
        source = documents[0][0].metadata.get("page_label", "Unknown")
    else:
        source = "Unknown"

    return {
        "answer": response.content,
        "source": f"Page {source}",
    }


