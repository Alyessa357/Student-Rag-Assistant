"""
main.py

Simple test script for the Student RAG Assistant.
"""

from rag import ask_question


def main():

    question = "How long is the bootcamp?"

    result = ask_question(question)

    print("\nRESULT")
    print(result)


if __name__ == "__main__":
    main()
