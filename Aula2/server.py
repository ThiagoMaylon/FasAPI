from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'msg': 'ola FastAPI'}

@app.get('/profile')
async def profile():
    return {'Nome': 'Thiago', 'Idade': 19}