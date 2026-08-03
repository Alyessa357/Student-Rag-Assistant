"""
api.py

FastAPI application for the Student Handbook RAG Assistant.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from rag import ask_question

app = FastAPI(
    title="Student Handbook RAG API",
    version="1.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Student Handbook RAG API is running."
    }


@app.post("/ask")
def ask(request: QuestionRequest):

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    result = ask_question(question)

    return result