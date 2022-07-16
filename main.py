"""sample fastapi project
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Number(BaseModel):
    x: int


@app.get('/')
def hello_world():
    """hello world api
    """
    return {'message': 'Hello, World!'}


@app.get('/greeting/{name}')
def greeting_user(name: str):
    """greeting to user with name
    """
    return {'message': f'Hello, {name}'}


@app.post('/power')
def power_of_number(data: Number):
    """return power of number
    """
    x = data.x
    return {'result': x*x}
