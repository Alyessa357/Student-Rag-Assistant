"""
text_splitter.py

This module is responsible for splitting the loaded handbook
into smaller chunks that can later be embedded into the vector database.
"""

# Import LangChain's RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Split a list of LangChain Documents into smaller chunks.

    Args:
        documents (list):
            List of LangChain Document objects.

    Returns:
        list:
            List of chunked Document objects.
    """

    # Create the text splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    # Split the documents
    chunks = splitter.split_documents(documents)

    return chunks