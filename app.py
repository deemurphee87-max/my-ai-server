from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Prompt(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/chat")
def chat(prompt: Prompt):
    return {
        "response": f"You said: {prompt.text}"
    }
