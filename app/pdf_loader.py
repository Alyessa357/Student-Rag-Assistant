"""
pdf_loader.py

This module is responsible for loading the student handbook PDF,
extracting the text from each page, and returning it in a structured format.
"""

import re
from pathlib import Path

import pymupdf
from langchain_core.documents import Document


def collapse_spaced_characters(text):
    """
    Convert spaced-out PDF letters such as 'H A R D W A R E'
    into readable words such as 'HARDWARE'.
    """

    pattern = re.compile(
        r"(?<![A-Za-z0-9])(?:[A-Za-z0-9]\s){2,}[A-Za-z0-9](?![A-Za-z0-9])"
    )

    previous = None
    while previous != text:
        previous = text
        text = pattern.sub(lambda match: match.group(0).replace(" ", ""), text)

    return text


def extract_trailing_heading(text):
    """
    This handbook places section titles at the bottom of each page.
    Pull that heading out so it can be added to the start of the page.
    """

    words = text.split()
    heading_words = []

    for word in reversed(words):
        token = word.strip(".,:;!?")
        letters = re.sub(r"[^A-Za-z]", "", token)

        if not letters:
            if heading_words and token in {"&", "-"}:
                heading_words.append(word)
                continue
            break

        if letters.isupper() and 1 <= len(letters) <= 20:
            heading_words.append(word)
            if len(heading_words) >= 8:
                break
        else:
            break

    heading_words.reverse()

    if 1 <= len(heading_words) <= 8:
        return " ".join(heading_words)

    return ""


def prepare_page_text(text):
    """
    Clean page text and move the section title to the front so
    question embeddings can match the correct handbook section.
    """

    text = collapse_spaced_characters(text)
    text = " ".join(text.split())

    heading = extract_trailing_heading(text)
    if heading:
        compact_heading = heading.replace(" ", "").replace("&", " AND ")
        text = f"{heading}. {compact_heading}. {text}"

    return text


def load_handbook():
    """
    Load the student handbook PDF and return the extracted pages.

    Returns:
        list: A list of LangChain Document objects.
    """

    project_root = Path(__file__).resolve().parent.parent
    pdf_path = project_root / "handbook" / "student_handbook.pdf"

    if not pdf_path.exists():
        raise FileNotFoundError(
            f"Handbook not found at: {pdf_path}"
        )

    pdf = pymupdf.open(str(pdf_path))
    documents = []

    for page_number, page in enumerate(pdf, start=1):
        text = prepare_page_text(page.get_text("text"))

        if not text:
            continue

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "page": page_number,
                    "page_label": str(page_number),
                    "source": str(pdf_path),
                },
            )
        )

    pdf.close()
    return documents
