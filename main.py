## web- backend
## main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Web App AI Backend")

# ---------------------------------------
# Enable CORS
# ---------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------
# Data Models
# ---------------------------------------
class ChatRequest(BaseModel):
    message: str

# ---------------------------------------
# Routes
# ---------------------------------------
@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "reply": f"You said: {req.message}"
    }

@app.get("/search")
def search(q: str):
    dummy_docs = [
        "AI is transforming education",
        "FastAPI is a Python web framework",
        "JavaScript connects frontend and backend",
        "Exam is scheduled on Friday.",
        "Niagara University is located in NY, USA.",
        "Library is a good place to study, open from 7am-11am everyday.",
        "Purple Eagles are fun!"
    ]

    results = [d for d in dummy_docs if q.lower() in d.lower()]

    return {
        "query": q,
        "results": results
    }