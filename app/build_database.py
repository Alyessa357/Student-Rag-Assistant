from pdf_loader import load_handbook
from text_splitter import split_documents
from vector_store import create_vector_store


def main():
    print("Loading handbook...")

    documents = load_handbook()

    print(f"Loaded {len(documents)} pages.")

    print("Splitting handbook into chunks...")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("Creating Chroma vector database...")

    create_vector_store(chunks)

    print("Vector database created successfully.")


if __name__ == "__main__":
    main()

