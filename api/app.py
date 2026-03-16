from fastapi import FastAPI
from src.rag_pipeline import create_rag_chain

app = FastAPI()

@app.get("/chat")
def chat(query: str):
    answer = rag_chain.invoke(query)
    return {"response": answer}
