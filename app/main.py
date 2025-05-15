from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .rag_pipeline import answer_question

app = FastAPI(title="MG ZS Car Assistant API")

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "MG ZS Car Assistant API is running."}

@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        response = answer_question(request.question)
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
