from fastapi import FastAPI

app = FastAPI(title='Api Crossfit')


@app.get('/')
def read_get():
    return {'msg': 'Olá Atleta'}
