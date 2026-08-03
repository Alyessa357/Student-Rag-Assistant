"""
pdf_loader.py

This module is responsible for loading the student handbook PDF,
extracting the text from each page, and returning it in a structured format.
"""

# Import the PDF loader from LangChain
from langchain_community.document_loaders import PyPDFLoader

# Import Path so we can work with file paths safely
from pathlib import Path


def load_handbook():
    """
    Load the student handbook PDF and return the extracted pages.

    Returns:
        list: A list of LangChain Document objects.
    """

    # Get the root project directory
    project_root = Path(__file__).resolve().parent.parent

    # Build the full path to the handbook
    pdf_path = project_root / "handbook" / "student_handbook.pdf"

    # Check whether the handbook exists
    if not pdf_path.exists():
        raise FileNotFoundError(
            f"Handbook not found at: {pdf_path}"
        )

    # Create the PDF loader
    loader = PyPDFLoader(str(pdf_path))

    # Load every page of the handbook
    documents = loader.load()


    for doc in documents:
        doc.page_content = " ".join(doc.page_content.split())

    return documents