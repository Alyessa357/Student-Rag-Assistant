# Student-Rag-Assistant

A Retrieval-Augmented Generation (RAG) AI assistant that answers student questions using information retrieved directly from a Student Handbook PDF.

The application uses semantic search with ChromaDB and HuggingFace embeddings to retrieve relevant handbook content before generating responses with a local Llama 3.2 model running through Ollama.

---

##  Project Overview

This project was developed as part of an AI Engineering assignment to demonstrate the complete Retrieval-Augmented Generation (RAG) pipeline.

Instead of relying on an AI model's general knowledge, the assistant first searches a vector database containing the student handbook and then generates answers using only the retrieved context.

If the requested information cannot be found within the handbook, the assistant returns:

> "I could not find that information in the handbook."

---

##  Features

- Load a Student Handbook PDF
- Extract text from every page
- Split the handbook into semantic chunks
- Generate embeddings using HuggingFace
- Store embeddings in ChromaDB
- Retrieve relevant handbook sections
- Generate answers using Ollama (Llama 3.2)
- Return the handbook source page
- REST API using FastAPI
- Prevent hallucinations by restricting answers to handbook content

---

##  Project Structure

Student-Rag-Assistant/

├── app/

│ ├── api.py

│ ├── config.py

│ ├── embeddings.py

│ ├── main.py

│ ├── models.py

│ ├── pdf_loader.py

│ ├── prompt.py

│ ├── rag.py

│ ├── routes.py

│ ├── text_splitter.py

│ ├── utils.py

│ └── vector_store.py

│

├── chroma_db/

├── handbook/

│ └── student_handbook.pdf

├── tests/

│ └── test_results.md

├── .gitignore

├── README.md

└── requirements.txt

---

##  Technologies Used

- Python
- FastAPI
- LangChain
- Ollama
- Llama 3.2
- HuggingFace Embeddings
- ChromaDB
- PyPDF
- Uvicorn

---

##  How the RAG Pipeline Works

1. Load the student handbook PDF.
2. Extract text from every page.
3. Split the text into smaller chunks.
4. Generate embeddings for each chunk.
5. Store embeddings in ChromaDB.
6. Receive a student's question.
7. Generate an embedding for the question.
8. Search ChromaDB for the most relevant handbook chunks.
9. Send the retrieved context to Llama 3.2.
10. Return the generated answer together with its handbook source page.

---

##  Example API Request

POST /ask

```json
{
    "question": "How long is the bootcamp?"
}
```

Example Response

```json
{
    "answer": "The bootcamp lasts for 7.5 months.",
    "source": "Page 8"
}
```

---

##  Sample Questions

The assistant was tested using questions including:

- How long is the bootcamp?
- What are the hardware requirements?
- When are the live classes?
- What are the communication channels?
- What are the payment options?
- What is the grade breakdown?
- Will there be tutor support?
- How does the placement & career opportunities work?
- What are the outcomes for this bootcamp?
- Who won the FIFA World Cup?

The final question intentionally verifies that the assistant does not hallucinate answers outside of the handbook.

---

##  Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Ollama

Download and install Ollama:

https://ollama.com

Pull the Llama model

```bash
ollama pull llama3.2
```

Create the vector database

Run the script responsible for loading the handbook, splitting it into chunks, generating embeddings, and creating the ChromaDB vector database.

Example:

```bash
python main.py
```
(Note: This assumes `main.py` is being used as your database creation script during setup.)

Run the API

```bash
uvicorn api:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

to access the Swagger API documentation.

---

##  Author

Developed by:

**Alyessa Moodley**

AI Engineering Assignment
