from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"mensagem": "Olá mundo, FastAPI 2024"}

# uvicorn server:app --reload